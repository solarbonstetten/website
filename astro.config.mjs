// @ts-check
import { defineConfig, fontProviders } from 'astro/config';

import sitemap from '@astrojs/sitemap';

import tailwindcss from '@tailwindcss/vite';

import { readdirSync, readFileSync } from 'node:fs';

// News-Entwürfe (Frontmatter `entwurf: true`) werden gebaut, aber nicht in die Sitemap aufgenommen.
const newsDir = new URL('./src/content/news/', import.meta.url);
const newsEntwuerfe = readdirSync(newsDir)
  .filter((f) => f.endsWith('.md') && /^entwurf:\s*true\s*$/m.test(readFileSync(new URL(f, newsDir), 'utf8')))
  .map((f) => `/news/${encodeURI(f.replace(/\.md$/, ''))}/`);

// https://astro.build/config
export default defineConfig({
  site: 'https://solarbonstetten.ch',
  integrations: [sitemap({ filter: (page) => !newsEntwuerfe.some((slug) => page.endsWith(slug)) })],

  fonts: [{
    provider: fontProviders.fontsource(),
    name: 'Inter',
    cssVariable: '--font-inter',
    weights: ['100 900'],
    subsets: ['latin'],
    display: 'swap',
  }],

  prefetch: {
    defaultStrategy: 'hover',
    prefetchAll: true,
  },

  build: {
    inlineStylesheets: 'always',
  },

  vite: {
    plugins: [tailwindcss()]
  }
});