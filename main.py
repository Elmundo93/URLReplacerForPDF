import fitz  # PyMuPDF

doc = fitz.open("First Resume (4).pdf") #Filename

replacements = {
    "https://github.com/stars/Elmundo93/lists/masterschool": "Masterschool Projects"
}

fontsize = 11
fontname = "helv"
font = fitz.Font(fontname=fontname)

for page in doc:
    for link in page.get_links():
        uri = link.get("uri", "")
        if uri in replacements:
            label = replacements[uri]
            rect = fitz.Rect(link["from"])

            # Textbereich weiß überdecken
            page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))

            # Textposition leicht abgesenkt
            x = rect.x0
            y = rect.y0 + 11.5

            # Textbreite berechnen
            text_width = font.text_length(label, fontsize=fontsize)
            text_rect = fitz.Rect(x, y, x + text_width, y + fontsize)

            # Text normal einsetzen (nicht fett, nicht unterstrichen)
            page.insert_text(
                (x, y),
                label,
                fontsize=fontsize,
                fontname=fontname,
                color=(0, 0, 0),
                render_mode=0
            )

            # Manuelle Unterstreichung
            underline_y = y + 2
            page.draw_line((x, underline_y), (x + text_width, underline_y), color=(0, 0, 0), width=0.5)

            # Klickbarer Link exakt auf Textgröße
            page.insert_link({
                "from": text_rect,
                "uri": uri,
                "kind": fitz.LINK_URI
            })

doc.save("Resume.pdf")
doc.close()