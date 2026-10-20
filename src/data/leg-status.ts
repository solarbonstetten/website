// Status und Kennzahlen der LEG-Zonen, aus legmanager.
//
// `leg-status.json` ist der Export «Status als JSON» aus legmanager (LEG-Liste) und ist für
// den Status massgebend: legmanager liest ihn direkt aus my.EKZ. Gebraucht von den Zonen-Karten
// (/leg), der Karte (über /leg/data/zonen-status.json) und der Zonen-Auswahl der Anmeldung.
import legsData from '../../public/leg/data/legs.json';
import legStatus from './leg-status.json';

// Die LEGs in legmanager heissen und zählen anders als hier:
// Zonen-Nr. (Reihenfolge in legs.json) → legmanager-ID.
const LEGMANAGER_ID: Record<number, number> = {
  1: 7,   // Dorf - Chüeweid         → Bonstetten - Dorf / Chüeweid
  2: 8,   // Chapf                   → Bonstetten - Chapf
  3: 9,   // Schachenhof             → Bonstetten - Schachenhof
  4: 1,   // Bruggenmatt             → Bonstetten - Bruggenmatt
  5: 3,   // Schachen - Breitenacher → Bonstetten - Schachen / Breitenacher
  6: 4,   // Sunnenberg              → Bonstetten - Sunnenberg
  7: 5,   // Dorf - Im Vorderdorf    → Bonstetten - Dorf / Im Vorderdorf
  9: 2,   // Strumberg               → Bonstetten - Strumberg
  11: 6,  // Heumoos                 → Bonstetten - Heumoos
};

if (legStatus.format !== 1) {
  throw new Error(`leg-status.json hat Format ${legStatus.format}, die Website kennt nur Format 1.`);
}

export type ZonenStatus = 'aktiv' | 'wird_aktiviert' | 'erfassung' | 'geplant';

type Leg = (typeof legStatus.legs)[number];
type Stufe = Leg['active'];

const legOf = (zoneNr: number): Leg | undefined =>
  legStatus.legs.find((l) => l.id === LEGMANAGER_ID[zoneNr]);

// legmanager kennt mehr Stufen, als die Website zeigt: `angemeldet` ist die «Anmeldung zur
// Aktivierung» bei EKZ, die drei Monate bis zur Aktivierung. Jede andere LEG, die legmanager
// kennt, ist «in Erfassung»; eine Zone ohne LEG in legmanager ist «geplant».
// `aufloesung_gemeldet` läuft noch bis zum Monatsende und gilt als aktiv.
export function zonenStatus(zoneNr: number): ZonenStatus {
  const leg = legOf(zoneNr);
  if (!leg) return 'geplant';
  switch (leg.status) {
    case 'aktiv':
    case 'aufloesung_gemeldet':
      return 'aktiv';
    case 'angemeldet':
      return 'wird_aktiviert';
    default:
      return 'erfassung';
  }
}

const leer = (s: Stufe) => s.producers === 0 && s.consumers === 0;
const anzahl = (n: number, eins: string, mehr: string) => `${n} ${n === 1 ? eins : mehr}`;
// «≥», wenn von mindestens einem Produzenten die Leistung noch nicht bekannt ist.
const kwp = (s: Stufe) =>
  `${s.producers_without_power ? '≥ ' : ''}${s.producers_peak_power_kw.toLocaleString('de-CH', {
    maximumFractionDigits: s.producers_peak_power_kw < 10 ? 1 : 0,
  })} kWp`;

// Was eine Zonen-Karte zeigt. Aktiv: die aktiven Anschlüsse, und die bestätigten, die noch
// dazukommen, als «+ …». Wird aktiviert: die bestätigten, die mit der Aktivierung starten.
// In Erfassung und geplant: keine Zahlen.
export function kennzahlen(zoneNr: number) {
  const leg = legOf(zoneNr);
  const status = zonenStatus(zoneNr);
  if (!leg || (status !== 'aktiv' && status !== 'wird_aktiviert')) return null;
  const haupt = status === 'aktiv' ? leg.active : leg.confirmed;
  if (leer(haupt)) return null;
  const zusatz = status === 'aktiv' && !leer(leg.confirmed) ? leg.confirmed : null;
  return {
    produzenten: haupt.producers ? `${anzahl(haupt.producers, 'Produzent', 'Produzenten')} · ${kwp(haupt)}` : null,
    konsumenten: haupt.consumers ? anzahl(haupt.consumers, 'Konsument', 'Konsumenten') : null,
    hinweis: zusatz ? `+ ${zusatz.producers + zusatz.consumers} bestätigt, noch nicht aktiv` : null,
    hinweisTitel: zusatz
      ? 'Von EKZ bestätigt, noch nicht aktiv: ' + [
          zusatz.producers ? `${anzahl(zusatz.producers, 'Produzent', 'Produzenten')} (${kwp(zusatz)})` : '',
          zusatz.consumers ? anzahl(zusatz.consumers, 'Konsument', 'Konsumenten') : '',
        ].filter(Boolean).join(' und ')
      : undefined,
  };
}

// Der Status jeder Zone, in der Reihenfolge von legs.json (Index 0 = Zone 1).
export const alleZonenStatus: ZonenStatus[] = legsData.map((_, i) => zonenStatus(i + 1));

export const stand = new Date(legStatus.as_of).toLocaleDateString('de-CH', {
  day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC',
});
