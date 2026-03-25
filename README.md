# solarbonstetten_poc

POC for Solarbonstetten Hosting – built with [Astro](https://astro.build) and [Sveltia CMS](https://github.com/sveltia/sveltia-cms).

**Live:** https://poc.solarbonstetten.ch

## 🚀 Commands

| Command             | Action                                     |
| :------------------ | :----------------------------------------- |
| `npm install`       | Install dependencies                       |
| `npm run dev`       | Start local dev server at `localhost:4321` |
| `npm run build`     | Build production site to `./dist/`         |
| `npm run preview`   | Preview build locally                      |

## ✏️ CMS – Sveltia CMS

Der Inhalt wird über [Sveltia CMS](https://github.com/sveltia/sveltia-cms) verwaltet (Drop-in-Ersatz für Decap CMS).

**Admin-URL:** https://poc.solarbonstetten.ch/admin/

### Einloggen (GitHub Token)

Da die Site auf GitHub Pages gehostet wird (kein Netlify-OAuth-Server), erfolgt der Login über ein **GitHub Personal Access Token**:

1. Token erstellen: [github.com/settings/tokens](https://github.com/settings/tokens)
   - Typ: **Token (classic)**
   - Scope: **`repo`** aktivieren
   - Token kopieren

2. Admin öffnen: https://poc.solarbonstetten.ch/admin/

3. **„Sign In with GitHub Using Token"** klicken und Token einfügen.

> **Hinweis:** Den Button „Sign In with GitHub" (ohne Token) **nicht** verwenden – dieser öffnet ein Netlify-OAuth-Fenster, das für diese Konfiguration nicht funktioniert.

### Inhalte

| Collection | Pfad                   | Beschreibung        |
| :--------- | :--------------------- | :------------------ |
| News       | `src/content/news/`    | Markdown-Artikel    |
| Projekte   | `src/content/projekte/`| Markdown-Projekte   |
| Bilder     | `public/images/`       | Medien-Uploads      |
