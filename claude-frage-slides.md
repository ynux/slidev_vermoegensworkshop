# Schätzt mal: Wer ist häufiger ganz oben?

<p class="sub">Wie viel häufiger gehört Gruppe A zu den Vermögendsten als Gruppe B? Markiert eure Schätzung auf der Skala, dann lösen wir auf.</p>

<div class="cards">

<div class="card">
  <div class="pair"><b>Männer</b> statt Frauen</div>
  <div class="where">unter den reichsten 1,5 %</div>
  <div class="track"><span v-for="t in [1,2,5,10,20,50,100]" :key="t" class="tick" :style="{ left: (Math.log10(t) / 2 * 100) + '%' }">{{ t }}×</span>
    <span v-click class="ans" :style="{ left: (Math.log10(2.3) / 2 * 100) + '%' }">2,3×</span></div>
</div>

<div class="card">
  <div class="pair"><b>West</b> statt Ost</div>
  <div class="where">unter den reichsten 1,5 %</div>
  <div class="track"><span v-for="t in [1,2,5,10,20,50,100]" :key="t" class="tick" :style="{ left: (Math.log10(t) / 2 * 100) + '%' }">{{ t }}×</span>
    <span v-click class="ans" :style="{ left: (Math.log10(3.2) / 2 * 100) + '%' }">ca. 3×</span></div>
</div>

<div class="card">
  <div class="pair"><b>Ohne</b> statt mit Migrationshintergrund</div>
  <div class="where">unter den reichsten 1,5 %</div>
  <div class="track"><span v-for="t in [1,2,5,10,20,50,100]" :key="t" class="tick" :style="{ left: (Math.log10(t) / 2 * 100) + '%' }">{{ t }}×</span>
    <span v-click class="ans" :style="{ left: (Math.log10(1.9) / 2 * 100) + '%' }">ca. 2×</span></div>
</div>

<div class="card">
  <div class="pair"><b>65 und älter</b> statt 25 bis 49</div>
  <div class="where">unter den reichsten 1,5 %</div>
  <div class="track"><span v-for="t in [1,2,5,10,20,50,100]" :key="t" class="tick" :style="{ left: (Math.log10(t) / 2 * 100) + '%' }">{{ t }}×</span>
    <span v-click class="ans" :style="{ left: (Math.log10(2.5) / 2 * 100) + '%' }">2,5×</span></div>
</div>

<div class="card">
  <div class="pair"><b>Eigentümer:innen</b> statt Mieter:innen</div>
  <div class="where">unter den reichsten 10 % der Haushalte</div>
  <div class="track"><span v-for="t in [1,2,5,10,20,50,100]" :key="t" class="tick" :style="{ left: (Math.log10(t) / 2 * 100) + '%' }">{{ t }}×</span>
    <span v-click class="ans" :style="{ left: (Math.log10(16) / 2 * 100) + '%' }">ca. 16×</span></div>
</div>

<div class="card">
  <div class="pair"><b>Selbstständige</b> statt Arbeiter:innen</div>
  <div class="where">unter den reichsten 1,5 %</div>
  <div class="track"><span v-for="t in [1,2,5,10,20,50,100]" :key="t" class="tick" :style="{ left: (Math.log10(t) / 2 * 100) + '%' }">{{ t }}×</span>
    <span v-click class="ans" :style="{ left: (Math.log10(60) / 2 * 100) + '%' }">über 50×</span></div>
</div>

</div>

<p v-click class="next">Und dann: Welche dieser Unterschiede sind <b>Lebenslauf</b>, welche <b>Herkunft</b>, welche <b>Politik</b>?</p>

<style>
.sub { font-size: 0.8rem; opacity: 0.75; margin: 0.2rem 0 0.6rem 0; }
.cards { display: grid; grid-template-columns: 1fr 1fr; gap: 0.7rem 2rem; }
.card { border-top: 2px solid #DDD6CA; padding-top: 0.35rem; }
.pair { font-size: 0.85rem; }
.where { font-size: 0.62rem; opacity: 0.65; margin-bottom: 1.1rem; }
.track { position: relative; height: 1.4rem; border-bottom: 2px solid #8A8478; margin: 0 1rem 0.9rem 0.6rem; }
.tick { position: absolute; bottom: -1.15rem; transform: translateX(-50%); font-size: 0.55rem; opacity: 0.6; }
.tick::before { content: ""; position: absolute; left: 50%; top: -0.35rem; height: 0.3rem; border-left: 1px solid #8A8478; }
.ans { position: absolute; bottom: 0.15rem; transform: translateX(-50%); background: #2e7d32; color: white; font-size: 0.65rem; font-weight: 700; padding: 0.05rem 0.4rem; border-radius: 0.6rem; white-space: nowrap; }
.next { margin-top: 0.9rem; padding: 0.45rem 0.8rem; border-left: 3px solid #2e7d32; background: rgba(46,125,50,0.07); font-size: 0.85rem; }
</style>

<!--
Ablauf: Erst schätzen lassen (Handzeichen, Klebepunkte auf ausgedruckter Skala oder einfach zurufen). Dann Karte für Karte auflösen; jeder Klick zeigt die nächste Antwort, der letzte Klick die Diskussionsfrage.

Die Skala ist logarithmisch: 1× heißt kein Unterschied, 100× ein riesiger.

Lesart der Zahlen: „Männer 2,3×“ heißt: Von allen Männern gehören 2,1 % zu den reichsten 1,5 % der Erwachsenen, von allen Frauen 0,9 %. Erwartbar ist meist, dass das Publikum Geschlecht und Migration überschätzt und Beruf und Wohnen unterschätzt.

Herkunft der Zahlen (Details auf den Gruppenfolien):
- Männer/Frauen, Ost/West, Migration, Alter, Beruf: DIW Wochenbericht 29/2020, Tab. 4 (SOEP 2019, Erwachsene), eigene Umrechnung. Wegen gerundeter Eingaben: Ost/West 2,8–3,7×, Migration 1,8–2,0×, Alter 2,4–2,7×, Selbstständige/Arbeiter:innen nicht genau bestimmbar, sicher über 50×.
- Eigentum/Miete: Bundesbank PHF 2021 (Haushalte): 21 % der Eigentümerhaushalte, aber 1,3 % der Mieterhaushalte gehören zu den reichsten 10 %. Andere Gruppe (reichste 10 % statt 1,5 %), darum eigens vermerkt.
-->
