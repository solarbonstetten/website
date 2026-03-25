// @ts-check
import { defineConfig } from 'astro/config';

import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://enbieri.github.io',
  base: '/solarbonstetten_poc',
  integrations: [sitemap()]
});