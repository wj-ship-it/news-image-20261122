#!/usr/bin/env python3
"""Render a newspaper front page for 22 November 2026.

Six verified world-news stories, drawn with PIL only. All text is set in
English; figures come straight from the verified brief and are not altered.
Output: news-frontpage.png, 1024 x 1024, RGB.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 236)
INK = (18, 18, 18)
GREY = (92, 88, 80)
RULE = (40, 40, 40)
ACCENT = (142, 24, 24)

FONT_DIR = "/usr/share/fonts/truetype"
SERIF = FONT_DIR + "/liberation/LiberationSerif-Regular.ttf"
SERIF_BOLD = FONT_DIR + "/liberation/LiberationSerif-Bold.ttf"
SERIF_ITALIC = FONT_DIR + "/liberation/LiberationSerif-Italic.ttf"
SANS = FONT_DIR + "/liberation/LiberationSans-Regular.ttf"
SANS_BOLD = FONT_DIR + "/liberation/LiberationSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, color=INK):
    """Draw wrapped paragraph, return y after the last line."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def rule(draw, x0, y, x1, weight=2):
    draw.line([(x0, y), (x1, y)], fill=RULE, width=weight)


def kicker(draw, x, y, text):
    f = font(SANS_BOLD, 17)
    draw.text((x, y), text.upper(), font=f, fill=ACCENT)
    return y + 24


def headline(draw, x, y, text, size, max_w, leading=None):
    f = font(SERIF_BOLD, size)
    lead = leading or int(size * 1.06)
    for line in wrap(draw, text, f, max_w):
        draw.text((x, y), line, font=f, fill=INK)
        y += lead
    return y


def story(draw, x, y, w, tag, title, body, source, title_size=27):
    """One news block: kicker, headline, body, source line. Returns bottom y."""
    y = kicker(draw, x, y, tag)
    y = headline(draw, x, y, title, title_size, w) + 3
    y = para(draw, x, y, body, font(SERIF, 19), w, 25)
    y += 2
    draw.text((x, y), "Source: " + source, font=font(SANS, 14), fill=GREY)
    return y + 16


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    m = 44                      # page margin
    right = W - m

    # ---- Masthead -------------------------------------------------------
    d.text((m, 22), "THE WORLD DISPATCH", font=font(SERIF_BOLD, 56), fill=INK)
    d.text((m, 84), "SUNDAY 22 NOVEMBER 2026  ·  SIX STORIES, ONE PAGE",
           font=font(SANS_BOLD, 18), fill=GREY)
    d.text((right - 250, 88), "WORLD NEWS IN BRIEF",
           font=font(SANS_BOLD, 18), fill=ACCENT)
    rule(d, m, 116, right, 4)
    rule(d, m, 122, right, 1)

    # ---- Lead story: COP31 ----------------------------------------------
    y = 134
    y = kicker(d, m, y, "Climate · Antalya, Turkey")
    y = headline(d, m, y, "COP31 COLLAPSES WITHOUT A DEAL",
                 48, right - m, leading=50) + 4
    y = para(d, m, y,
             "United Nations climate talks in Antalya ended with no agreement "
             "after running two days past schedule. The European Union led a "
             "walkout, refusing to sign a draft text that made no mention of "
             "fossil fuels, and negotiators left the summit with the core "
             "dispute unresolved.",
             font(SERIF, 21), right - m, 28)
    y += 2
    d.text((m, y), "Source: UN climate summit reports, 22 November 2026",
           font=font(SANS, 15), fill=GREY)
    y += 28
    rule(d, m, y, right, 3)
    y += 12

    # ---- Two-column middle rows -----------------------------------------
    col_w = (right - m - 28) // 2
    x2 = m + col_w + 28

    y_top = y
    y_left = story(d, m, y_top, col_w,
                   "AI · Supply chain",
                   "OpenRouter drops three suppliers over stolen prompts",
                   "OpenRouter said on 22 November it had removed three "
                   "inference providers after research by Dragos' canary "
                   "project showed prompts were being stolen, including "
                   "requests marked zero data retention. 125 endpoints lost "
                   "their zero-retention status and affected customers were "
                   "notified.",
                   "OpenRouter, 22 Nov 2026", title_size=27)
    y_right = story(d, x2, y_top, col_w,
                    "Middle East",
                    "Iran strikes Bahrain; two hurt, radars claimed hit",
                    "Iranian missiles and drones struck targets in Bahrain. "
                   "Bahrain said a civilian industrial facility was hit and "
                    "two people were injured. Iran said it had destroyed two "
                    "US Patriot radar units.",
                    "Bahrain / Iran statements", title_size=27)
    y = max(y_left, y_right)
    d.line([(x2 - 14, y_top + 4), (x2 - 14, y - 8)], fill=RULE, width=1)
    rule(d, m, y, right, 1)
    y += 12

    y_top = y
    y_left = story(d, m, y_top, col_w,
                   "Mexico · Sinaloa",
                   "Cartel boss 'El Chapo Isidro' captured",
                   "Special forces captured Fausto Isidro Meza Flores in "
                   "Sinaloa. Eleven people were killed in the fighting, "
                   "including four soldiers.",
                   "Mexican authorities", title_size=27)
    y_right = story(d, x2, y_top, col_w,
                    "Indonesia · Banten",
                    "Candy factory fire kills 3; 36 missing",
                    "A fire swept through a candy factory in Cikande, Banten. "
                   "Three workers were killed and 36 are missing, with rescue "
                    "operations still under way.",
                   "Local officials", title_size=27)
    y = max(y_left, y_right)
    d.line([(x2 - 14, y_top + 4), (x2 - 14, y - 8)], fill=RULE, width=1)
    rule(d, m, y, right, 1)
    y += 12

    # ---- Bottom band: EU-Indonesia trade deal ---------------------------
    y = kicker(d, m, y, "Trade · Brussels / Jakarta")
    y = headline(d, m, y,
                 "EU and Indonesia sign trade deal after nearly a decade of talks",
                 28, right - m, leading=32) + 3
    y = para(d, m, y,
             "The agreement removes tariffs on up to 98.5% of goods, closing "
             "almost ten years of negotiations between the European Union and "
             "Indonesia.",
             font(SERIF, 19), right - m, 25)
    y += 2
    d.text((m, y), "Source: EU / Indonesia joint announcement",
           font=font(SANS, 14), fill=GREY)
    y += 22

    # ---- Footer ----------------------------------------------------------
    rule(d, m, y, right, 3)
    d.text((m, y + 10),
           "THE WORLD DISPATCH — Sunday 22 November 2026 · All six stories "
           "verified from source reports.",
           font=font(SANS, 15), fill=GREY)
    d.text((right - 150, y + 10), "PAGE 1",
           font=font(SANS_BOLD, 15), fill=INK)

    img.save("news-frontpage.png")
    print("saved news-frontpage.png", img.size)


if __name__ == "__main__":
    main()
