#!/usr/bin/env python3
"""Colour checks for progressive-design-system (standard library only).

Commands
  info COLOR                 Convert a colour and report sRGB / Display P3 gamut.
  pair TEXT BACKGROUND       WCAG 2 contrast, APCA Lc and grayscale difference for one pair.
  ramp HUE CHROMA            Build an OKLCH ramp at one hue, clamped to sRGB.
  tokens FILE.json           Check every text/background pair in a W3C (DTCG) tokens file,
                             plus a grayscale check on colours that must be told apart.

Colours can be written as #rgb, #rrggbb, "oklch(0.62 0.14 40)", "oklch(62% 0.14 40)"
or "0.62,0.14,40" (OKLCH L, C, H).

Options
  --medium web|app|print     Adds a print warning for high-chroma colours (default: web).
  --pairs FILE.json          For `tokens`: explicit pairs, e.g.
                             [{"text": "color.text", "bg": "color.bg", "use": "body"}].
                             "use" is body, large or ui. Without it, pairs are guessed from names.
  --distinguish FILE.json    For `tokens`: groups of colours that must be told apart in grayscale,
                             e.g. [["color.data.point", "color.data.other"], ["color.card", "color.bg"]].
                             Without it, chart and status colours are grouped by name, plus each
                             text/background pair. Ramp steps are never compared with each other.
  --steps N                  For `ramp`: number of steps (default 11).

Exit code is 1 when any checked pair fails its WCAG threshold, so the script can gate a build.
"""

import argparse
import json
import math
import re
import sys

# ---------------------------------------------------------------- parsing


def parse_color(text):
    """Return OKLab (L, a, b) for a colour string."""
    s = text.strip().lower()
    if s.startswith("#"):
        return srgb_to_oklab(hex_to_srgb(s))
    m = re.match(r"oklch\(\s*([\d.]+)(%?)\s+([\d.]+)\s+([\d.]+)", s)
    if m:
        L = float(m.group(1)) / (100 if m.group(2) else 1)
        return oklch_to_oklab(L, float(m.group(3)), float(m.group(4)))
    parts = [p for p in re.split(r"[,\s]+", s) if p]
    if len(parts) == 3:
        L, C, H = (float(p) for p in parts)
        return oklch_to_oklab(L, C, H)
    raise ValueError(f"Can't read colour: {text!r}")


def hex_to_srgb(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"Bad hex colour: #{h}")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def srgb_to_hex(rgb):
    return "#" + "".join(f"{round(max(0, min(1, c)) * 255):02x}" for c in rgb)


# ---------------------------------------------------------------- conversions
# OKLab matrices from Björn Ottosson; P3 matrices from CSS Color 4.


def _to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _to_gamma(c):
    sign = -1 if c < 0 else 1
    c = abs(c)
    return sign * (12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055)


def srgb_to_oklab(rgb):
    r, g, b = (_to_linear(c) for c in rgb)
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l, m, s = (math.copysign(abs(v) ** (1 / 3), v) for v in (l, m, s))
    return (
        0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
        1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
        0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s,
    )


def oklab_to_linear_srgb(lab):
    L, a, b = lab
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    return (
        4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    )


def oklab_to_srgb(lab):
    return tuple(_to_gamma(c) for c in oklab_to_linear_srgb(lab))


def oklch_to_oklab(L, C, H):
    h = math.radians(H)
    return (L, C * math.cos(h), C * math.sin(h))


def oklab_to_oklch(lab):
    L, a, b = lab
    return (L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360)


def linear_srgb_to_linear_p3(rgb):
    r, g, b = rgb
    x = 0.4123908 * r + 0.3575843 * g + 0.1804808 * b
    y = 0.2126390 * r + 0.7151687 * g + 0.0721923 * b
    z = 0.0193308 * r + 0.1191948 * g + 0.9505322 * b
    return (
        2.4934969 * x - 0.9313836 * y - 0.4027108 * z,
        -0.8294890 * x + 1.7626641 * y + 0.0236247 * z,
        0.0358458 * x - 0.0761724 * y + 0.9568845 * z,
    )


def in_gamut(rgb, eps=1e-4):
    return all(-eps <= c <= 1 + eps for c in rgb)


def clamp_to_srgb(L, C, H):
    """Reduce chroma at fixed L and H until the colour fits sRGB."""
    lo, hi = 0.0, C
    if in_gamut(oklab_to_linear_srgb(oklch_to_oklab(L, C, H))):
        return C
    for _ in range(30):
        mid = (lo + hi) / 2
        if in_gamut(oklab_to_linear_srgb(oklch_to_oklab(L, mid, H))):
            lo = mid
        else:
            hi = mid
    return lo


# ---------------------------------------------------------------- contrast


def wcag_luminance(rgb):
    r, g, b = (_to_linear(max(0, min(1, c))) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def wcag_ratio(text_rgb, bg_rgb):
    a, b = wcag_luminance(text_rgb), wcag_luminance(bg_rgb)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def apca_lc(text_rgb, bg_rgb):
    """APCA 0.0.98G-4g lightness contrast (Lc). Positive: dark text on light; negative: light on dark."""

    def y(rgb):
        r, g, b = (max(0, min(1, c)) ** 2.4 for c in rgb)
        v = 0.2126729 * r + 0.7151522 * g + 0.0721750 * b
        return v + (0.022 - v) ** 1.414 if v < 0.022 else v

    yt, yb = y(text_rgb), y(bg_rgb)
    if abs(yb - yt) < 0.0005:
        return 0.0
    if yb > yt:
        sapc = (yb ** 0.56 - yt ** 0.57) * 1.14
        out = 0 if sapc < 0.1 else sapc - 0.027
    else:
        sapc = (yb ** 0.65 - yt ** 0.62) * 1.14
        out = 0 if sapc > -0.1 else sapc + 0.027
    return out * 100


WCAG_MIN = {"body": 4.5, "large": 3.0, "ui": 3.0}
APCA_MIN = {"body": 75, "large": 60, "ui": 45}


# ---------------------------------------------------------------- reports


def describe(lab, medium):
    L, C, H = oklab_to_oklch(lab)
    lin = oklab_to_linear_srgb(lab)
    srgb_ok = in_gamut(lin)
    p3_ok = in_gamut(linear_srgb_to_linear_p3(lin))
    notes = []
    if not srgb_ok:
        notes.append("outside sRGB (hex is clipped)" + ("; fits Display P3" if p3_ok else "; outside Display P3 too"))
    if medium == "print" and C > 0.15:
        notes.append("high chroma: check against a print proof, it may dull in CMYK")
    return {
        "oklch": f"oklch({L:.3f} {C:.3f} {H:.1f})",
        "hex": srgb_to_hex(oklab_to_srgb(lab)),
        "notes": notes,
    }


def check_pair(text_lab, bg_lab, use="body"):
    t, b = oklab_to_srgb(text_lab), oklab_to_srgb(bg_lab)
    ratio = wcag_ratio(t, b)
    lc = apca_lc(t, b)
    gray_gap = abs(text_lab[0] - bg_lab[0])
    return {
        "use": use,
        "wcag": round(ratio, 2),
        "wcag_pass": ratio >= WCAG_MIN[use],
        "apca_lc": round(lc, 1),
        "apca_ok": abs(lc) >= APCA_MIN[use],
        "lightness_gap": round(gray_gap, 3),
    }


def print_pair(name, r):
    verdict = "PASS" if r["wcag_pass"] else "FAIL"
    apca = "ok" if r["apca_ok"] else "low"
    print(f"{verdict}  {name}  [{r['use']}]  WCAG {r['wcag']}:1 (min {WCAG_MIN[r['use']]})  "
          f"APCA Lc {r['apca_lc']} ({apca}, min {APCA_MIN[r['use']]})  lightness gap {r['lightness_gap']}")


# ---------------------------------------------------------------- tokens


def load_tokens(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    raw = {}

    def walk(node, path_parts, inherited_type):
        if not isinstance(node, dict):
            return
        node_type = node.get("$type", inherited_type)
        if "$value" in node:
            raw[".".join(path_parts)] = (node_type, node["$value"])
            return
        for k, v in node.items():
            if not k.startswith("$"):
                walk(v, path_parts + [k], node_type)

    walk(data, [], None)

    def resolve(value, depth=0):
        if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
            if depth > 20:
                raise ValueError(f"Alias loop at {value}")
            target = value[1:-1]
            if target not in raw:
                raise ValueError(f"Alias points nowhere: {value}")
            return resolve(raw[target][1], depth + 1)
        return value

    colors = {}
    for name, (typ, value) in raw.items():
        value = resolve(value)
        lab = token_color_to_oklab(value) if (typ == "color" or _looks_like_color(value)) else None
        if lab is not None:
            colors[name] = lab
    return colors


def _looks_like_color(value):
    return (isinstance(value, dict) and "colorSpace" in value) or (
        isinstance(value, str) and re.fullmatch(r"#[0-9a-fA-F]{3,8}", value.strip()))


def token_color_to_oklab(value):
    if isinstance(value, str):
        return parse_color(value[:7] if value.startswith("#") else value)
    if isinstance(value, dict):
        space = value.get("colorSpace", "").lower()
        comps = value.get("components", [])
        if space == "oklch" and len(comps) == 3:
            return oklch_to_oklab(*comps)
        if space == "oklab" and len(comps) == 3:
            return tuple(comps)
        if space == "srgb" and len(comps) == 3:
            return srgb_to_oklab(tuple(comps))
        if value.get("hex"):
            return parse_color(value["hex"])
    return None


TEXT_HINTS = ("text", "fg", "foreground", "on-", "on_", "icon")
BG_HINTS = ("bg", "background", "surface", "canvas", "page")


def guess_pairs(colors):
    texts = [n for n in colors if any(h in n.split(".")[-1].lower() for h in TEXT_HINTS)]
    bgs = [n for n in colors if any(h in n.split(".")[-1].lower() for h in BG_HINTS)]
    pairs = []
    for t in texts:
        for b in bgs:
            # Default to the strictest threshold; pass --pairs to mark large text or UI.
            use = "large" if "large" in t.lower() else "body"
            pairs.append({"text": t, "bg": b, "use": use})
    return pairs


DISTINGUISH_HINTS = ("data", "chart", "series", "status", "success", "warning", "error", "danger", "info")


def guess_distinguish_groups(colors):
    """Colours that must be told apart: chart series and status colours, by name."""
    group = [n for n in colors if any(h in n.lower() for h in DISTINGUISH_HINTS)]
    return [group] if len(group) > 1 else []


def grayscale_clashes(colors, groups, threshold=0.04):
    """Within each group of colours that must be told apart, pairs that look
    near-identical in grayscale. Ramp steps and unrelated colours are never
    compared, because they never need to be distinguished from each other."""
    clashes, seen = [], set()
    for group in groups:
        names = [n for n in group if n in colors]
        for i, a in enumerate(names):
            for b in names[i + 1:]:
                key = tuple(sorted((a, b)))
                if key in seen:
                    continue
                seen.add(key)
                gap = abs(colors[a][0] - colors[b][0])
                if gap < threshold:
                    clashes.append((a, b, gap))
    return clashes


# ---------------------------------------------------------------- commands


def cmd_info(args):
    lab = parse_color(args.color)
    d = describe(lab, args.medium)
    print(f"{d['oklch']}  {d['hex']}")
    for n in d["notes"]:
        print(f"  note: {n}")
    return 0


def cmd_pair(args):
    t, b = parse_color(args.text), parse_color(args.bg)
    failed = False
    for use in ("body", "large", "ui"):
        r = check_pair(t, b, use)
        print_pair(f"{args.text} on {args.bg}", r)
        failed |= use == args.use and not r["wcag_pass"]
    for label, lab in (("text", t), ("background", b)):
        for n in describe(lab, args.medium)["notes"]:
            print(f"  {label}: {n}")
    return 1 if failed else 0


def cmd_ramp(args):
    n = max(3, args.steps)
    print(f"Ramp at hue {args.hue}, peak chroma {args.chroma}, clamped to sRGB")
    for i in range(n):
        L = 0.97 - (0.97 - 0.15) * i / (n - 1)
        # Chroma peaks in the mid-tones and tapers toward white and black.
        C = args.chroma * math.sin(math.pi * min(1, max(0, (L - 0.1) / 0.9)))
        C = clamp_to_srgb(L, C, args.hue)
        lab = oklch_to_oklab(L, C, args.hue)
        step = 50 if i == 0 else i * 100 if i < n - 1 else 950
        print(f"  {step:>4}  oklch({L:.3f} {C:.3f} {args.hue:.1f})  {srgb_to_hex(oklab_to_srgb(lab))}")
    return 0


def cmd_tokens(args):
    colors = load_tokens(args.file)
    if not colors:
        print("No colour tokens found.")
        return 0
    if args.pairs:
        with open(args.pairs, encoding="utf-8") as f:
            pairs = json.load(f)
    else:
        pairs = guess_pairs(colors)
        print("Pairs guessed from token names (pass --pairs to set them explicitly).")
    failed = 0
    for p in pairs:
        if p["text"] not in colors or p["bg"] not in colors:
            print(f"SKIP  {p['text']} on {p['bg']}: token not found")
            continue
        r = check_pair(colors[p["text"]], colors[p["bg"]], p.get("use", "body"))
        print_pair(f"{p['text']} on {p['bg']}", r)
        failed += not r["wcag_pass"]
    print()
    print("Gamut and medium:")
    any_note = False
    for name, lab in sorted(colors.items()):
        for n in describe(lab, args.medium)["notes"]:
            print(f"  {name}: {n}")
            any_note = True
    if not any_note:
        print("  all colours fit sRGB")
    print()
    if args.distinguish:
        with open(args.distinguish, encoding="utf-8") as f:
            groups = json.load(f)
    else:
        groups = guess_distinguish_groups(colors)
        # A card or text must also stand apart from the page it sits on.
        groups += [[p["text"], p["bg"]] for p in pairs]
    clashes = grayscale_clashes(colors, groups)
    print("Grayscale (only colours that must be told apart):")
    if clashes:
        for a, b, gap in clashes:
            print(f"  {a} and {b} look almost the same in grayscale (lightness gap {gap:.3f}); "
                  f"add a second cue such as an outline, pattern or label")
    else:
        print("  every group stays distinguishable in grayscale")
    print()
    print(f"{len(pairs)} pairs checked, {failed} failing WCAG.")
    return 1 if failed else 0


def main(argv=None):
    p = argparse.ArgumentParser(description="Colour checks for design systems (OKLCH, WCAG 2, APCA, gamut, grayscale).")
    p.add_argument("--medium", choices=["web", "app", "print"], default="web")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("info")
    s.add_argument("color")
    s.set_defaults(fn=cmd_info)

    s = sub.add_parser("pair")
    s.add_argument("text")
    s.add_argument("bg")
    s.add_argument("--use", choices=["body", "large", "ui"], default="body")
    s.set_defaults(fn=cmd_pair)

    s = sub.add_parser("ramp")
    s.add_argument("hue", type=float)
    s.add_argument("chroma", type=float)
    s.add_argument("--steps", type=int, default=11)
    s.set_defaults(fn=cmd_ramp)

    s = sub.add_parser("tokens")
    s.add_argument("file")
    s.add_argument("--pairs")
    s.add_argument("--distinguish")
    s.set_defaults(fn=cmd_tokens)

    args = p.parse_args(argv)
    try:
        return args.fn(args)
    except (ValueError, OSError, json.JSONDecodeError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
