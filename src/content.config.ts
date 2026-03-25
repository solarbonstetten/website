import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const news = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/news' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    image: z.string().optional(),
  }),
});

const projekte = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/projekte' }),
  schema: z.object({
    title: z.string(),
    image: z.string().optional(),
  }),
});

const solaranlagen = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/solaranlagen' }),
  schema: z.object({
    title: z.string(),
    badge: z.string(),
    reihenfolge: z.number(),
    finanzierung: z.string(),
    typ: z.string(),
    ausrichtung: z.string(),
    leistung: z.string(),
    jahresertrag: z.string(),
    module: z.string(),
    monitoring_url: z.string().optional(),
  }),
});

export const collections = { news, projekte, solaranlagen };
