# solarbonstetten Website

Website des Vereins solarbonstetten – gebaut mit [Astro](https://astro.build) und [Sveltia CMS](https://github.com/sveltia/sveltia-cms).

**Live:** https://solarbonstetten.ch

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

### Inhalte

| Collection | Pfad                        | Beschreibung                    |
| :--------- | :-------------------------- | :------------------------------ |
| News       | `src/content/news/`         | Markdown-Artikel                |
| Projekte   | `src/content/projekte/`     | Markdown-Projekte               |
| Solaranlagen | `src/content/solaranlagen/` | Anlage-Daten                  |
| Links      | `src/content/links/`        | Weiterführende Links            |
| Dokumente  | `src/content/dokumente/`    | PDFs (Statuten, Protokolle etc.)|
| Der Verein | `src/content/der-verein/`   | Vereinsseite                    |
| Statuten   | `src/content/statuten/`     | Vereinsstatuten                 |
| Bilder     | `public/images/`            | Medien-Uploads                  |
