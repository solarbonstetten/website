// @ts-check
import { defineConfig, fontProviders } from 'astro/config';

import sitemap from '@astrojs/sitemap';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://poc.solarbonstetten.ch',
  integrations: [sitemap()],

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