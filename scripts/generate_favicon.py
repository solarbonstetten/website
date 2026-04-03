# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pillow",
# ]
# ///
import os
from PIL import Image, ImageDraw, ImageFont

def create_favicons():
    public_dir = os.path.join(os.path.dirname(__file__), "..", "public")
    os.makedirs(public_dir, exist_ok=True)
    
    # 1. GENERATE SVG
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <defs>
    <style>
      .text-gray {
        font-family: "Inter", Arial, "Helvetica Neue", Helvetica, sans-serif;
        font-weight: bold;
        fill: #9b9c9e;
        letter-spacing: -2px;
      }
    </style>
  </defs>

  <!-- Solid yellow bar with rounded top-left corner -->
  <path d="M 15 65 A 15 15 0 0 1 30 50 L 85 50 L 85 90 L 15 90 Z" fill="#fbba00" />
  
  <!-- "sb" in the top half, intersecting the bar -->
  <text x="50" y="60" class="text-gray" font-size="58" text-anchor="middle">sb</text>
</svg>
"""
    svg_path = os.path.join(public_dir, "favicon.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Created {svg_path}")

    # 2. GENERATE ICO
    # We will use Pillow to match the SVG design as closely as possible.
    img = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    yellow = '#fbba00'
    gray = '#9b9c9e'

    # SVG coordinates scaled by 2.56
    # x: 15 to 85 -> 38.4 to 217.6
    # y: 50 to 90 -> 128 to 230.4
    # radius: 15 -> 38.4
    
    x_min = int(15 * 2.56)
    x_max = int(85 * 2.56)
    y_min = int(50 * 2.56)
    y_max = int(90 * 2.56)
    rad = int(15 * 2.56)
    
    # Yellow background shape
    # Main rectangle (skipping the top left corner part)
    draw.rectangle([x_min + rad, y_min, x_max, y_max], fill=yellow)
    draw.rectangle([x_min, y_min + rad, x_min + rad, y_max], fill=yellow)
    # Top-left corner (circle pie slice)
    draw.pieslice([x_min, y_min, x_min + rad * 2, y_min + rad * 2], 180, 270, fill=yellow)
    
    # Text "sb"
    try:
        # User is on Windows, arialbd.ttf is usually available
        font = ImageFont.truetype("arialbd.ttf", int(58 * 2.56))
    except:
        font = ImageFont.load_default()
        
    s_text = "sb"
    
    # To roughly match SVG text-anchor: middle and y=60 (baseline at 60 * 2.56 = 153.6)
    # Pillow's draw.text uses top-left coordinates or specific anchors. 
    # We can use anchor="md" (middle, descending/baseline) to match SVG better.
    # Actually, PIL anchor="ms" (middle, text baseline) is equivalent to SVG text-anchor="middle" + y as baseline.
    
    cx = 128  # 50 * 2.56
    cy = int(60 * 2.56) # 153.6
    
    try:
        draw.text((cx, cy), s_text, fill=gray, font=font, anchor="ms")
    except TypeError:
        # Fallback if Pillow version is very old and doesn't support anchor
        bbox = draw.textbbox((0, 0), s_text, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((cx - tw/2, cy - th), s_text, fill=gray, font=font)

    ico_path = os.path.join(public_dir, "favicon.ico")
    img.save(ico_path, format="ICO", sizes=[(16,16), (32, 32), (48, 48), (64,64)])
    print(f"Created {ico_path}")

if __name__ == "__main__":
    create_favicons()
