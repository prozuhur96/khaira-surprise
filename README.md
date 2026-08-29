# 🎈 Happy 1 Month Milestone Card for Baby Khaira

A simple, responsive, and beautifully styled web-based celebration card built with HTML5 and CSS3. Features a pure CSS 2-layer cake with flickering candle animations, ambient floating elements, and side-by-side message cards for the parents.

---

## ✨ Features

- **Pure CSS Animated Cake:** Two-layer cake design with glowing, animated candlelight flickers.
- **Ambient Floating Animations:** Floating background hearts and sparkles rendered with CSS keyframes.
- **Responsive Layout:** Side-by-side message blocks that adjust dynamically across screen sizes using CSS Flexbox.
- **Modern UI Styling:** Clean typography, soft glassmorphism card effect, and custom color palettes for Hooyo & Aabo.

---

## 📁 Project Structure

```text
BirthdayCard/
├── index.html   # Main HTML markup structure
└── style.css    # Styling, layouts, animations, and color schemes
```

## How to Run
### 1. Web Card (HTML/CSS)
1. Download or Clone the Repo
2. Open the Project:
   - Double-click `index.html` to open it directly in your default web browser.
   - Alternatively, drag and drop `index.html` straight into an open browser tab.
3. Edit & Customise:
    - Modify the names or text inside `index.html` to customise the message.
    - Save the file and refresh your browser to view changes instantly.

### 2. QR Code Generator (Python)
1. Prerequisites: Ensure Python is installed, then install the required libraries:

    `pip install qrcode pillow`

2. Configure Link: Host your card online (GitHub Pages) and paste your live URL into `card_url` variable in `qr_code.py`.

3. Generate Image: (Already done) Run the script to create `khaira_1month.png`:

`python3.13 qr_code.py`


## Built with
- HTML5 - Semantic document structure
- CSS3 - Flexbox layout, keyframe animations, glassmorphism, and custom styling.
- Python 3 - Automated QR Code image generation (qrcode, Pillow)