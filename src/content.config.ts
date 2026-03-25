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
    umsetzungspartner: z.string().optional(),
    monitoring_url: z.string().optional(),
  }),
});

const links = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/links' }),
  schema: z.object({
    title: z.string(),
    beschreibung: z.string(),
    url: z.string().url(),
    kategorie: z.string(),
    reihenfolge: z.number(),
  }),
});

const statuten = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/statuten' }),
  schema: z.object({
    title: z.string(),
    stand: z.string(),
  }),
});

const derVerein = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/der-verein' }),
  schema: z.object({
    title: z.string(),
    untertitel: z.string(),
    gruendungsdatum: z.string(),
  }),
});

export const collections = { news, projekte, solaranlagen, links, statuten, derVerein };
