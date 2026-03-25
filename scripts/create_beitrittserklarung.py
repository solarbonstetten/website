from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.lib.units import mm

W, H = A4

ORANGE      = HexColor('#F5A800')
ORANGE_DARK = HexColor('#d97706')
DARK        = HexColor('#1a2744')
GREY        = HexColor('#64748b')
LIGHT_BG    = HexColor('#fffbf0')
FIELD_BG    = HexColor('#f8fafc')
BORDER      = HexColor('#e2e8f0')
CREAM       = HexColor('#fef9ee')

OUTPUT = '/Users/Enrico/git/solarbonstetten-website/public/downloads/beitrittserklarung.pdf'

import os
os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

c = canvas.Canvas(OUTPUT, pagesize=A4)
c.setTitle('Beitrittserklärung solarbonstetten')
c.setAuthor('solarbonstetten')
c.setSubject('Beitrittserklärung zum Verein solarbonstetten')

# ── Heller Cream-Header-Bereich ───────────────────────────────────────────────
c.setFillColor(CREAM)
c.rect(0, H - 44*mm, W, 44*mm, fill=1, stroke=0)

# Oranger Akzent-Balken oben
c.setFillColor(ORANGE)
c.rect(0, H - 2*mm, W, 2*mm, fill=1, stroke=0)

# Echtes Logo (PNG)
LOGO = '/Users/Enrico/git/solarbonstetten-website/src/assets/logo.png'
logo_h = 14*mm
from reportlab.lib.utils import ImageReader
from PIL import Image as PILImage
img = PILImage.open(LOGO)
iw, ih = img.size
logo_w = logo_h * (iw / ih)
c.drawImage(LOGO, 18*mm, H - 20*mm - logo_h/2, width=logo_w, height=logo_h, mask='auto')

# Tagline
c.setFillColor(GREY)
c.setFont('Helvetica', 8.5)
c.drawString(18*mm, H - 36*mm, 'Solarenergie und erneuerbare Energien in Bonstetten')

# Trennlinie unterm Header
c.setStrokeColor(BORDER)
c.setLineWidth(0.5)
c.line(18*mm, H - 44*mm, W - 18*mm, H - 44*mm)

# ── Titel ─────────────────────────────────────────────────────────────────────
c.setFillColor(DARK)
c.setFont('Helvetica-Bold', 20)
c.drawString(18*mm, H - 58*mm, 'Beitrittserklärung')

# Orange Akzent-Linie unterm Titel
c.setFillColor(ORANGE)
c.rect(18*mm, H - 61*mm, 40*mm, 1.2*mm, fill=1, stroke=0)

c.setFillColor(GREY)
c.setFont('Helvetica', 9.5)
c.drawString(18*mm, H - 68*mm, 'Ich möchte zur Entwicklung von Solarenergie in Bonstetten beitragen.')

# ── Hilfsfunktionen ───────────────────────────────────────────────────────────
def section_label(c, x, y, text):
    """Abschnitts-Label: uppercase, orange Punkt davor"""
    c.setFillColor(ORANGE)
    c.circle(x + 1.5*mm, y + 2*mm, 1.5*mm, fill=1, stroke=0)
    c.setFillColor(DARK)
    c.setFont('Helvetica-Bold', 8)
    c.drawString(x + 5*mm, y, text.upper())

def field_label(c, x, y, text, required=False):
    c.setFont('Helvetica', 8)
    c.setFillColor(GREY)
    c.drawString(x, y, text)
    if required:
        c.setFillColor(ORANGE)
        c.drawString(x + c.stringWidth(text, 'Helvetica', 8) + 0.5*mm, y, '*')

def text_field(c, name, x, y, w, h=6.5*mm):
    """Feld mit hellblauem Hintergrund und feiner Unterlinie statt Box"""
    c.setFillColor(FIELD_BG)
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.4)
    c.roundRect(x, y, w, h, 1.5*mm, fill=1, stroke=0)
    # Nur Unterlinie in Orange
    c.setStrokeColor(ORANGE)
    c.setLineWidth(1.2)
    c.line(x, y, x + w, y)
    c.acroForm.textfield(
        name=name,
        x=x + 1.5*mm, y=y + 1*mm,
        width=w - 3*mm, height=h - 1.5*mm,
        fontSize=10,
        borderColor=None,
        fillColor=None,
        textColor=DARK,
        forceBorder=False,
    )

def checkbox_styled(c, name, x, y, size=4.5*mm):
    c.setFillColor(FIELD_BG)
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.8)
    c.roundRect(x, y, size, size, 1*mm, fill=1, stroke=1)
    c.acroForm.checkbox(
        name=name,
        x=x, y=y,
        size=size,
        borderColor=BORDER,
        fillColor=FIELD_BG,
        textColor=ORANGE,
        forceBorder=True,
        checked=False,
    )

def radio_styled(c, group, value, x, y, size=4.5*mm):
    """Radio Button – Kreis manuell gezeichnet, transparentes Formularfeld drüber"""
    r = size / 2
    cx, cy = x + r, y + r
    # Äusserer Kreis (Hintergrund)
    c.setFillColor(FIELD_BG)
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.8)
    c.circle(cx, cy, r, fill=1, stroke=1)
    # Transparentes AcroForm-Feld (für Interaktivität)
    c.acroForm.radio(
        name=group,
        tooltip=value,
        value=value,
        x=x, y=y,
        size=size,
        borderColor=None,
        fillColor=None,
        textColor=ORANGE,
        forceBorder=False,
        selected=False,
        buttonStyle='circle',
    )

# ── Persönliche Angaben ───────────────────────────────────────────────────────
y = H - 78*mm
section_label(c, 18*mm, y, 'Persönliche Angaben')

y -= 9*mm
field_label(c, 18*mm, y, 'Vorname', required=True)
field_label(c, 110*mm, y, 'Name', required=True)
y -= 9*mm
text_field(c, 'vorname', 18*mm, y, 86*mm)
text_field(c, 'name', 110*mm, y, 82*mm)

y -= 13*mm
field_label(c, 18*mm, y, 'Strasse', required=True)
y -= 9*mm
text_field(c, 'strasse', 18*mm, y, 174*mm)

y -= 13*mm
field_label(c, 18*mm, y, 'PLZ', required=True)
field_label(c, 46*mm, y, 'Ort', required=True)
y -= 9*mm
text_field(c, 'plz', 18*mm, y, 22*mm)
text_field(c, 'ort', 46*mm, y, 146*mm)

y -= 13*mm
field_label(c, 18*mm, y, 'Telefon')
field_label(c, 110*mm, y, 'E-Mail', required=True)
y -= 9*mm
text_field(c, 'telefon', 18*mm, y, 86*mm)
text_field(c, 'email', 110*mm, y, 82*mm)

# ── Mitgliedschaft ────────────────────────────────────────────────────────────
y -= 14*mm
section_label(c, 18*mm, y, 'Mitgliedschaft')

def mitglied_card(c, x, y, w, h, title, price, desc, group, value):
    # Card-Hintergrund
    c.setFillColor(FIELD_BG)
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.4)
    c.roundRect(x, y, w, h, 2*mm, fill=1, stroke=1)
    # Orange Linie links
    c.setFillColor(ORANGE)
    c.roundRect(x, y, 2*mm, h, 1*mm, fill=1, stroke=0)
    # Radio Button (exklusiv durch gemeinsame Gruppe)
    radio_styled(c, group, value, x + 4*mm, y + h/2 - 2.25*mm)
    # Titel
    c.setFillColor(DARK)
    c.setFont('Helvetica-Bold', 10)
    c.drawString(x + 13*mm, y + h - 6*mm, title)
    # Preis
    c.setFillColor(ORANGE)
    c.setFont('Helvetica-Bold', 10)
    c.drawRightString(x + w - 4*mm, y + h - 6*mm, price)
    # Beschreibung
    c.setFillColor(GREY)
    c.setFont('Helvetica', 8)
    c.drawString(x + 13*mm, y + 4*mm, desc)

y -= 9*mm
mitglied_card(c, 18*mm, y - 16*mm, 85*mm, 20*mm,
              'Aktivmitglied', 'CHF 40.– / Jahr',
              'Mit Stimmberechtigung an der Generalversammlung',
              group='mitgliedschaft', value='Aktivmitglied')
mitglied_card(c, 108*mm, y - 16*mm, 84*mm, 20*mm,
              'Gönnermitglied', 'CHF 100.– / Jahr',
              'Unterstützung ohne Stimmberechtigung',
              group='mitgliedschaft', value='Goennermitglied')

# ── Optionale Angaben ─────────────────────────────────────────────────────────
y -= 30*mm
section_label(c, 18*mm, y, 'Optionale Angaben')

y -= 10*mm
checkbox_styled(c, 'solarstrom', 18*mm, y)
c.setFillColor(DARK)
c.setFont('Helvetica', 9.5)
c.drawString(27*mm, y + 1.2*mm, 'Ich möchte von solarbonstetten Solarstrom beziehen.')

y -= 9*mm
checkbox_styled(c, 'aktiv', 18*mm, y)
c.setFillColor(DARK)
c.setFont('Helvetica', 9.5)
c.drawString(27*mm, y + 1.2*mm, 'Ich möchte im Verein solarbonstetten aktiv mitarbeiten.')

# ── Unterschrift ──────────────────────────────────────────────────────────────
y -= 14*mm
section_label(c, 18*mm, y, 'Unterschrift')

y -= 9*mm
field_label(c, 18*mm, y, 'Ort / Datum', required=True)
y -= 9*mm
text_field(c, 'ort_datum', 18*mm, y, 76*mm)

# Unterschriftslinie mit Label
c.setStrokeColor(ORANGE)
c.setLineWidth(1.2)
c.line(108*mm, y, 192*mm, y)
c.setFillColor(GREY)
c.setFont('Helvetica', 8)
c.drawString(108*mm, y + 2*mm, 'Unterschrift')

# Pflichtfeld-Hinweis
c.setFillColor(GREY)
c.setFont('Helvetica', 7.5)
c.drawString(18*mm, y - 7*mm, '* Pflichtfelder')

# ── Footer ────────────────────────────────────────────────────────────────────
footer_h = 20*mm

# Trennlinie
c.setStrokeColor(BORDER)
c.setLineWidth(0.5)
c.line(18*mm, footer_h + 0.5*mm, W - 18*mm, footer_h + 0.5*mm)

# Orange Punkt-Akzent ganz unten
c.setFillColor(ORANGE)
c.rect(0, 0, W, 1.5*mm, fill=1, stroke=0)

c.setFillColor(DARK)
c.setFont('Helvetica-Bold', 8.5)
c.drawString(18*mm, footer_h - 5*mm, 'solarbonstetten')
c.setFont('Helvetica', 8)
c.setFillColor(GREY)
c.drawString(18*mm, footer_h - 10*mm, 'Dorfstrasse 24 · 8906 Bonstetten')
c.drawString(18*mm, footer_h - 15*mm, 'info@solarbonstetten.ch · www.solarbonstetten.ch')

c.setFont('Helvetica', 8)
c.setFillColor(GREY)
c.drawRightString(W - 18*mm, footer_h - 5*mm, 'Postkonto: 60-190129-1')
c.drawRightString(W - 18*mm, footer_h - 10*mm, 'IBAN: CH03 0900 0000 6019 0129 1')
c.setFillColor(ORANGE)
c.drawRightString(W - 18*mm, footer_h - 15*mm, 'poc.solarbonstetten.ch/mitmachen')

c.save()
print(f'PDF erstellt: {OUTPUT}')
