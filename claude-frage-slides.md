---
zoom: 1.2
---

# Schätzt mal: der mittlere Haushalt

<Kommentar>Ich habe nach dem Vortrag zwei der Schätzungen ausgelagert auf die nächste Folie, sie haben einen anderen Charakter. Nehmt euch Zeit für diese Folie.</Kommentar>

<p class="sub">Median des Haushaltsnettovermögens je Gruppe, 2023. Grün hinterlegt: <span style="color:#2e7d32; font-weight:700">der Park</span>, 100.000 bis 750.000 €.</p>

<div class="cards">
<div v-for="c in [
  ['Region', 'Ost', 35900, 'West', 143200],
  ['Staatsangehörigkeit', 'nicht deutsch', 28500, 'deutsch', 134900],
  ['Beruf', 'Arbeiter:innen', 56800, 'Beamt:innen', 323300],
  ['Haushaltstyp', 'Alleinerziehende', 10000, 'Paare mit Kindern', 166300]
]" :key="c[0]" class="card">
  <div class="where">{{ c[0] }}: <span class="pair"><span class="sw lo"></span>{{ c[1] }} &nbsp;<span class="sw hi"></span>{{ c[3] }}</span></div>
  <div class="track">
    <div class="park"></div>
    <span v-for="t in [[1000,'1.000 €'],[10000,'10.000 €'],[100000,'100.000 €'],[1000000,'1 Mio. €']]" :key="t[0]" class="tick" :style="{ left: ((Math.log10(t[0]) - 3) / 3 * 100) + '%' }">{{ t[1] }}</span>
    <div v-click class="ans">
      <span class="dot lo" :style="{ left: ((Math.log10(c[2]) - 3) / 3 * 100) + '%' }"></span>
      <span class="lab lo" :style="{ left: ((Math.log10(c[2]) - 3) / 3 * 100) + '%', transform: ((Math.log10(c[2]) - 3) / 3) > 0.75 ? 'translateX(-100%) translateX(0.5rem)' : (((Math.log10(c[2]) - 3) / 3) < 0.25 ? 'translateX(-0.5rem)' : 'translateX(-50%)') }">{{ c[2].toLocaleString('de-DE') }} €</span>
      <span class="dot hi" :style="{ left: ((Math.log10(c[4]) - 3) / 3 * 100) + '%' }"></span>
      <span class="lab hi" :style="{ left: ((Math.log10(c[4]) - 3) / 3 * 100) + '%', transform: ((Math.log10(c[4]) - 3) / 3) > 0.75 ? 'translateX(-100%) translateX(0.5rem)' : (((Math.log10(c[4]) - 3) / 3) < 0.25 ? 'translateX(-0.5rem)' : 'translateX(-50%)') }">{{ c[4].toLocaleString('de-DE') }} €</span>
    </div>
  </div>
</div>
</div>

<div class="sources">
<a href="https://publikationen.bundesbank.de/caas/v1/media/955436/data/dbdce1fbc3b7f0ac7fc8b3727c17112a">Bundesbank, PHF 2023, Tabellenanhang, Tab. 2</a>
</div>

<style>
.sub { font-size: 0.75rem; opacity: 0.8; margin: 0.2rem 0 0.4rem 0; }
.cards { display: grid; grid-template-columns: 1fr 1fr; gap: 1.6rem 2.5rem; margin-top: 1rem; }
.card { padding-top: 0.2rem; }
.where { font-size: 0.6rem; text-transform: uppercase; letter-spacing: 0.06em; color: rgba(0,0,0,0.6); }
.track { position: relative; height: 3.9rem; margin: 0 1.6rem 0 1.6rem; }
.track::after { content: ""; position: absolute; left: 0; right: 0; top: 1.8rem; border-top: 2px solid #8A8478; }
.park { position: absolute; top: 1.35rem; height: 0.9rem; left: 66.67%; width: 29.17%; background: rgba(46,125,50,0.18); border-radius: 2px; }
.tick { position: absolute; top: 2.05rem; transform: translateX(-50%); font-size: 0.5rem; opacity: 0.55; white-space: nowrap; }
.tick::before { content: ""; position: absolute; left: 50%; top: -0.35rem; height: 0.3rem; border-left: 1px solid #8A8478; }
.ans { position: absolute; inset: 0; }
.dot { position: absolute; top: 1.8rem; width: 0.7rem; height: 0.7rem; border-radius: 50%; transform: translate(-50%, -50%); border: 2px solid white; z-index: 2; }
.dot.lo { background: #8A8478; }
.dot.hi { background: #2a78d6; }
.lab { position: absolute; transform: translateX(-50%); font-size: 0.6rem; font-weight: 700; white-space: nowrap; }
.lab.hi { top: 0.15rem; }
.lab.lo { top: 2.75rem; font-weight: 600; opacity: 0.85; }
.sources { position: absolute; left: 3.5rem; right: 3.5rem; bottom: 0.9rem; font-size: 0.5rem; line-height: 1.4; opacity: 0.6; }
.sources a { color: inherit; text-decoration: underline; text-underline-offset: 2px; }
.pair { text-transform: none; letter-spacing: 0; opacity: 1; font-size: 0.68rem; color: inherit; }
.sw { display: inline-block; width: 0.5rem; height: 0.5rem; border-radius: 50%; margin: 0 0.25rem 0 0.3rem; vertical-align: 0.05rem; }
.sw.lo { background: #8A8478; } .sw.hi { background: #2a78d6; }
</style>

<!--
Ablauf: Gruppe nennen, schätzen lassen, wo der mittlere Haushalt liegt (zurufen oder Klebepunkte auf ausgedruckter Skala). Jeder Klick löst eine Karte auf. Wohnsituation und Alter stehen auf der nächsten Folie: Dort hängt der Unterschied eng mit dem Vermögen selbst zusammen (wer Vermögen hat, kauft eher; wer älter ist, hatte mehr Zeit zum Sparen). Hier geht es um Unterschiede, die mehr mit Herkunft und Lebenslage zu tun haben.

Lesart: Der Median ist der mittlere Haushalt der Gruppe; die Hälfte der Gruppe hat weniger, die Hälfte mehr. Liegt der Median im grünen Bereich, ist mindestens die Hälfte der Gruppe im Park oder darüber. Die Skala ist logarithmisch: Jeder Strich ist das Zehnfache des vorigen.

Zum Vergleich: Median aller Haushalte 103.200 €, also genau an der Grenze zum Park.

Weitere Werte aus derselben Tabelle (Median 2023):
- Eigentum mit Kredit 379.900 €
- Angestellte 101.500 €, Selbstständige 475.500 €, Arbeitslose 3.400 €
- Alleinlebende 37.700 €, Paare ohne Kinder 236.300 €
- 16–24 Jahre 13.000 €, 35–44 Jahre 75.100 €, 65–74 Jahre 211.900 €

Grenzen: Haushalte, eingeordnet nach der Person mit dem höchsten Einkommen (Alter, Beruf, Staatsangehörigkeit). Der Median sagt nichts über die Streuung innerhalb der Gruppe; die steht auf den Gruppenfolien.
-->

---
hideInToc: true
zoom: 1.2
---

# Schätzt mal: Wohnsituation und Alter

<Kommentar>Die Unterschiede sind groß, aber haben andere Gründe und Implikationen als die auf der vorigen Folie.</Kommentar>

<p class="sub">Median des Haushaltsnettovermögens je Gruppe, 2023. Grün hinterlegt: <span style="color:#2e7d32; font-weight:700">der Park</span>, 100.000 bis 750.000 €.</p>

<div class="cards">
<div v-for="c in [
  ['Wohnsituation', 'zur Miete', 18300, 'Eigentum ohne Kredit', 450200],
  ['Alter', '25–34 Jahre', 19100, '55–64 Jahre', 255900]
]" :key="c[0]" class="card">
  <div class="where">{{ c[0] }}: <span class="pair"><span class="sw lo"></span>{{ c[1] }} &nbsp;<span class="sw hi"></span>{{ c[3] }}</span></div>
  <div class="track">
    <div class="park"></div>
    <span v-for="t in [[1000,'1.000 €'],[10000,'10.000 €'],[100000,'100.000 €'],[1000000,'1 Mio. €']]" :key="t[0]" class="tick" :style="{ left: ((Math.log10(t[0]) - 3) / 3 * 100) + '%' }">{{ t[1] }}</span>
    <div v-click class="ans">
      <span class="dot lo" :style="{ left: ((Math.log10(c[2]) - 3) / 3 * 100) + '%' }"></span>
      <span class="lab lo" :style="{ left: ((Math.log10(c[2]) - 3) / 3 * 100) + '%', transform: ((Math.log10(c[2]) - 3) / 3) > 0.75 ? 'translateX(-100%) translateX(0.5rem)' : (((Math.log10(c[2]) - 3) / 3) < 0.25 ? 'translateX(-0.5rem)' : 'translateX(-50%)') }">{{ c[2].toLocaleString('de-DE') }} €</span>
      <span class="dot hi" :style="{ left: ((Math.log10(c[4]) - 3) / 3 * 100) + '%' }"></span>
      <span class="lab hi" :style="{ left: ((Math.log10(c[4]) - 3) / 3 * 100) + '%', transform: ((Math.log10(c[4]) - 3) / 3) > 0.75 ? 'translateX(-100%) translateX(0.5rem)' : (((Math.log10(c[4]) - 3) / 3) < 0.25 ? 'translateX(-0.5rem)' : 'translateX(-50%)') }">{{ c[4].toLocaleString('de-DE') }} €</span>
    </div>
  </div>
</div>
</div>

<div class="sources">
<a href="https://publikationen.bundesbank.de/caas/v1/media/955436/data/dbdce1fbc3b7f0ac7fc8b3727c17112a">Bundesbank, PHF 2023, Tabellenanhang, Tab. 2</a>
</div>

<style>
.sub { font-size: 0.75rem; opacity: 0.8; margin: 0.2rem 0 0.4rem 0; }
.cards { display: grid; grid-template-columns: 1fr 1fr; gap: 1.6rem 2.5rem; margin-top: 1rem; }
.card { padding-top: 0.2rem; }
.where { font-size: 0.6rem; text-transform: uppercase; letter-spacing: 0.06em; color: rgba(0,0,0,0.6); }
.track { position: relative; height: 3.9rem; margin: 0 1.6rem 0 1.6rem; }
.track::after { content: ""; position: absolute; left: 0; right: 0; top: 1.8rem; border-top: 2px solid #8A8478; }
.park { position: absolute; top: 1.35rem; height: 0.9rem; left: 66.67%; width: 29.17%; background: rgba(46,125,50,0.18); border-radius: 2px; }
.tick { position: absolute; top: 2.05rem; transform: translateX(-50%); font-size: 0.5rem; opacity: 0.55; white-space: nowrap; }
.tick::before { content: ""; position: absolute; left: 50%; top: -0.35rem; height: 0.3rem; border-left: 1px solid #8A8478; }
.ans { position: absolute; inset: 0; }
.dot { position: absolute; top: 1.8rem; width: 0.7rem; height: 0.7rem; border-radius: 50%; transform: translate(-50%, -50%); border: 2px solid white; z-index: 2; }
.dot.lo { background: #8A8478; }
.dot.hi { background: #2a78d6; }
.lab { position: absolute; transform: translateX(-50%); font-size: 0.6rem; font-weight: 700; white-space: nowrap; }
.lab.hi { top: 0.15rem; }
.lab.lo { top: 2.75rem; font-weight: 600; opacity: 0.85; }
.sources { position: absolute; left: 3.5rem; right: 3.5rem; bottom: 0.9rem; font-size: 0.5rem; line-height: 1.4; opacity: 0.6; }
.sources a { color: inherit; text-decoration: underline; text-underline-offset: 2px; }
.pair { text-transform: none; letter-spacing: 0; opacity: 1; font-size: 0.68rem; color: inherit; }
.sw { display: inline-block; width: 0.5rem; height: 0.5rem; border-radius: 50%; margin: 0 0.25rem 0 0.3rem; vertical-align: 0.05rem; }
.sw.lo { background: #8A8478; } .sw.hi { background: #2a78d6; }
</style>

<!--
Anders als auf der Folie davor: Wohneigentum ist zum großen Teil selbst das Vermögen, und Vermögen wächst mit dem Alter. Die Unterschiede sind deshalb groß, aber eher Zusammenhang als Ungleichbehandlung.

Lesart wie auf der Folie davor: Median des Haushaltsnettovermögens, logarithmische Skala, grün = Park.

Weitere Werte (PHF 2023, Tab. 2, Median): Eigentum mit Kredit 379.900 €; 16–24 Jahre 13.000 €, 35–44 Jahre 75.100 €, 45–54 Jahre 156.200 €, 65–74 Jahre 211.900 €, 75 und älter 149.400 €.
-->
