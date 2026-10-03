# Tinashe Rukasha – portfolio

A single-page digital CV in a 2002 (Windows XP / Aqua) style.

- `index.html` – the built page (open it in a browser)
- `photo.jpg` – wallpaper and TR monogram photo
- `src/template.html` – page source; `{{name:scale}}` marks where a pixel sprite goes
- `src/build.py` – turns the template into `index.html`, drawing the pixel sprites as inline SVG

To change the page, edit `src/template.html` and run `python3 src/build.py`.

The page is a draft: it has `<meta name="robots" content="noindex, nofollow">`.
Remove that line when you are ready to make it public.
