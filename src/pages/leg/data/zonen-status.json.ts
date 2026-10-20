// Der Status jeder Zone für die Karte (public/leg/legmap.html), die als statische Seite
// die Daten selbst lädt: { "1": "aktiv", "2": "geplant", … }, Schlüssel = Zonen-Nr.
// Wird beim Bauen erzeugt, aus derselben Quelle wie die Zonen-Karten (src/data/leg-status.ts).
import type { APIRoute } from 'astro';
import { alleZonenStatus } from '../../../data/leg-status';

export const GET: APIRoute = () =>
  new Response(JSON.stringify(Object.fromEntries(alleZonenStatus.map((s, i) => [i + 1, s]))), {
    headers: { 'Content-Type': 'application/json' },
  });
