# solarbonstetten Website

Website des Vereins solarbonstetten – gebaut mit [Astro](https://astro.build) und [Sveltia CMS](https://github.com/sveltia/sveltia-cms).

**Live:** https://solarbonstetten.ch  
**LEG:** https://leg-bonstetten.ch → leitet weiter auf https://solarbonstetten.ch/leg

## 🚀 Commands

| Command             | Action                                     |
| :------------------ | :----------------------------------------- |
| `npm install`       | Install dependencies                       |
| `npm run dev`       | Start local dev server at `localhost:4321` |
| `npm run build`     | Build production site to `./dist/`         |
| `npm run preview`   | Preview build locally                      |

## ✏️ CMS – Sveltia CMS

Der Inhalt wird über [Sveltia CMS](https://github.com/sveltia/sveltia-cms) verwaltet.

**Admin-URL:** https://solarbonstetten.ch/admin/

### Einloggen (GitHub Token)

Da die Site auf GitHub Pages gehostet wird (kein Netlify-OAuth-Server), erfolgt der Login über ein **Fine-grained Personal Access Token** – dieser erlaubt den Zugriff gezielt auf ein einzelnes Repository.

**1. Token erstellen:** [github.com/settings/personal-access-tokens](https://github.com/settings/personal-access-tokens)

- **Token name:** z. B. `sveltia-cms-solarbonstetten`
- **Expiration:** nach Bedarf wählen
- **Resource owner:** `solarbonstetten`
- **Repository access:** → **Only select repositories** → `website` auswählen
- **Permissions → Repository permissions:**
  - `Contents` → **Read and write**
  - `Metadata` → **Read-only** (wird automatisch gesetzt)
- Token generieren und kopieren

**2. Admin öffnen:** https://solarbonstetten.ch/admin/

**3.** **„Sign In with GitHub Using Token"** klicken und Token einfügen.

> **Hinweis:** Den Button „Sign In with GitHub" (ohne Token) **nicht** verwenden – dieser öffnet ein Netlify-OAuth-Fenster, das für diese Konfiguration nicht funktioniert.

### CMS-Collections

| Collection   | Pfad                          | Beschreibung                     |
| :----------- | :---------------------------- | :------------------------------- |
| News         | `src/content/news/`           | Markdown-Artikel                 |
| Solaranlagen | `src/content/solaranlagen/`   | Anlage-Daten inkl. optionalem Bild |
| Links        | `src/content/links/`          | Weiterführende Links             |
| Dokumente    | `src/content/dokumente/`      | PDFs (Statuten, Protokolle etc.) |
| Der Verein   | `src/content/der-verein/`     | Vereinsseite                     |
| Statuten     | `src/content/statuten/`       | Vereinsstatuten                  |
| Bilder       | `public/images/`              | Medien-Uploads                   |

Bilder für Solaranlagen landen unter `public/images/solaranlagen/` – bitte als **WebP** hochladen (spart ~97% Dateigrösse gegenüber PNG).

## 🗺️ LEG – Lokale Elektrizitätsgemeinschaften

Seiten unter `/leg` und `/leg/anmeldung` für die LEG-Verwaltung der Gemeinde Bonstetten.

### Datendateien (`public/leg/data/`)

| Datei               | Beschreibung                                      | Generiert durch        |
| :------------------ | :------------------------------------------------ | :--------------------- |
| `addresses.json`    | 1639 Bonstetter Adressen mit LEG-Zuweisung        | Externes Python-Script |
| `solar_data.json`   | Solardaten pro Adresse (Potenzial, installiert…)  | Externes Python-Script |
| `leg_polygons.json` | GeoJSON-Polygone der 13 LEG-Zonen                 | Externes Python-Script |
| `legs.json`         | Adresslisten pro Zone                             | Externes Python-Script |

> **Hinweis:** Nach Aktualisierung der JSON-Files durch das externe Script müssen diese nach `public/leg/data/` committed werden. Die Karte (`public/leg/legmap.html`) liest die Daten relativ via `data/solar_data.json` und `data/leg_polygons.json`.

## 🐍 Python Scripts (`scripts/`)

| Script                        | Beschreibung                                      |
| :---------------------------- | :------------------------------------------------ |
| `create_beitrittserklarung.py`| Generiert `public/dokumente/vereinsbeitritt.pdf`  |
| `generate_favicon.py`         | Generiert `public/favicon.svg` und `.ico`         |

### Abhängigkeiten installieren

```bash
pip install -r scripts/requirements.txt
```
