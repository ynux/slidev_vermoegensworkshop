# Exkurs: Wie Menschen in die Schulden rutschen

<p class="lead">Was Menschen in der Schuldnerberatung als Hauptauslöser nennen</p>

<div class="grid grid-cols-[3fr_2fr] gap-10 mt-6">

<div>

<p class="small">Hauptauslöser der Überschuldung, Anteil der Ratsuchenden 2025</p>

<div v-for="r in [
  { l: 'Krankheit, Sucht, Unfall', v: 18 },
  { l: 'Arbeitslosigkeit', v: 17 },
  { l: 'Unwirtschaftliche Haushaltsführung', v: 12 },
  { l: 'Trennung, Scheidung, Tod des Partners', v: 11 },
  { l: 'Dauerhaft niedriges Einkommen', v: 10 },
  { l: 'Gescheiterte Selbstständigkeit', v: 8 },
]" :key="r.l" class="row">
  <span class="label">{{ r.l }}</span>
  <span class="track"><span class="fill" :style="{ width: (r.v / 18 * 100) + '%' }"></span></span>
  <span class="val">{{ r.v }} %</span>
</div>

</div>

<div class="stats">
  <div class="num">34.650 €</div>
  <div class="cap">durchschnittliche Schulden der Menschen in Schuldnerberatung</div>
  <div class="num mt-5">7,36 Mio.</div>
  <div class="cap">überschuldete Erwachsene in Deutschland, gut jede zehnte Person</div>
</div>

</div>

<p class="source">Quellen: Destatis, Überschuldungsstatistik 2025 (Juli 2026); Creditreform, SchuldnerAtlas (Stichtag 1.10.2026, neue Methode)</p>

<style>
.lead { font-size: 1.15rem; opacity: 0.75; margin-top: 0.25rem; }
.small { font-size: 0.75rem; opacity: 0.7; margin: 0 0 0.5rem 0; }
.row { display: flex; align-items: center; gap: 0.75rem; margin: 0.45rem 0; }
.label { width: 15rem; font-size: 0.85rem; line-height: 1.2; }
.track { flex: 1; height: 1.1rem; }
.fill { display: block; height: 100%; background: #8A8478; border-radius: 3px; }
.val { width: 2.8rem; font-weight: 700; font-size: 0.85rem; text-align: right; }
.stats { border-left: 2px solid #DDD6CA; padding-left: 1.5rem; }
.num { font-size: 2.4rem; font-weight: 700; line-height: 1; }
.cap { font-size: 0.85rem; line-height: 1.3; margin-top: 0.3rem; }
.source { position: absolute; left: 3.5rem; bottom: 1rem; font-size: 0.6rem; opacity: 0.6; }
</style>

<!--
Mögliche Frage an die Teilnehmenden: Welche dieser Auslöser hat man selbst in der Hand, welche nicht?

Hintergrund: Krankheit, Arbeitslosigkeit und Trennung zusammen machen rund 46 Prozent der Fälle aus. Ein Dispokredit kostet im Schnitt rund 11 Prozent Zinsen.

Zur Einordnung: Die Prozentwerte beziehen sich auf Menschen, die eine Schuldnerberatung aufgesucht haben, nicht auf alle Überschuldeten. 15 Prozent nennen sonstige Ursachen. Bei Alleinerziehenden ist Trennung, Scheidung oder Tod des Partners mit rund 23 Prozent der häufigste Auslöser. Mehr als die Hälfte der Ratsuchenden lebt allein.

Die 7,36 Millionen stammen aus dem SchuldnerAtlas mit einer neuen Berechnungsmethode und sind nicht direkt mit älteren Ausgaben vergleichbar (2025 nach alter Methode: 5,67 Millionen).
-->