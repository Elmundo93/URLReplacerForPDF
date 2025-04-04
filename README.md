# 📄 Replace PDF URLs with PyMuPDF

This script lets you **automatically replace visible URLs in a PDF** with custom text labels, while maintaining the link functionality – clean, clickable, and fully customizable using [PyMuPDF](https://pymupdf.readthedocs.io/).

## ✨ Features
- ✅ Replace visible URLs with readable labels
- ✅ Insert clickable links exactly matching the text width
- ✅ Clean layout: normal font, manual underline, pixel-precise positioning
- ✅ Prevents hover boxes around the links
- 🧩 Easily modifiable for multiple links or styling

## 📸 Before & After

| Before | After |
|--------|-------|
| https://github.com/... | **Masterschool Projects** (black, underlined, clickable) |

## 🚀 Getting Started

### 1. Install PyMuPDF

```bash
pip install pymupdf
```

### 2. Use the script

```python
import fitz  # PyMuPDF

doc = fitz.open(""First Resume (4).pdf"")  # Replace with your file

replacements = {
    ""https://github.com/stars/Elmundo93/lists/masterschool"": ""Masterschool Projects""
}

fontsize = 11
fontname = ""helv""
font = fitz.Font(fontname=fontname)

for page in doc:
    for link in page.get_links():
        uri = link.get(""uri"", """")
        if uri in replacements:
            label = replacements[uri]
            rect = fitz.Rect(link[""from""])

            # White out old link
            page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))

            # Position text slightly lower
            x = rect.x0
            y = rect.y0 + 11.5

            text_width = font.text_length(label, fontsize=fontsize)
            text_rect = fitz.Rect(x, y, x + text_width, y + fontsize)

            # Insert text
            page.insert_text(
                (x, y),
                label,
                fontsize=fontsize,
                fontname=fontname,
                color=(0, 0, 0),
                render_mode=0
            )

            # Underline manually
            underline_y = y + 2
            page.draw_line((x, underline_y), (x + text_width, underline_y), color=(0, 0, 0), width=0.5)

            # Insert new clickable area
            page.insert_link({
                ""from"": text_rect,
                ""uri"": uri,
                ""kind"": fitz.LINK_URI
            })

doc.save(""Resume.pdf"")
doc.close()
```

## 🧠 Why This Exists

I created this tool while working on my own resume – I wanted clean, readable link labels instead of raw URLs, but still clickable like before. This script solves exactly that.

## 📂 Use Cases
- ✍️ Beautify resumes and portfolios
- 📚 Clean up exported Markdown or Notion PDFs
- 📥 Batch-clean links in documentation PDFs

## 🙌 Contribute

Feel free to fork, modify, or submit PRs! If it helped you, consider starring the repo ✨

## 📄 License

MIT License
"
