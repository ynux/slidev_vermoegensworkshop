---
hideInToc: true
---

# Haushalte und Personen: zwei Arten zu zählen

<Kommentar>Vorsicht, Einheiten! Die besseren Zahlen gibt es für Haushalte, und in vieler Hinsicht ist diese Betrachtung auch sinnvoll. Um beispielsweise Junge und Alte zu vergleichen ist es ungünstig.</Kommentar>

<table class="hp">
<thead>
<tr><th></th><th>Haushalte</th><th>Erwachsene einzeln</th></tr>
</thead>
<tbody>
<tr><td>Wer gezählt wird</td><td>jeder Haushalt mit dem Vermögen aller Mitglieder zusammen</td><td>jede erwachsene Person mit ihrem eigenen Vermögen</td></tr>
<tr><td>Median</td><td class="n">103.200&nbsp;€</td><td class="n">22.800&nbsp;€</td></tr>
<tr><td>unter 100.000&nbsp;€</td><td class="n">ca. 50&nbsp;%</td><td class="n">ca. 70&nbsp;%</td></tr>
<tr><td>über 1&nbsp;Mio.&nbsp;€</td><td class="n">ca. 7&nbsp;%</td><td class="n">ca. 1,5&nbsp;%</td></tr>
<tr><td>Daten</td><td>Bundesbank, 2023¹</td><td>SOEP, 2019²</td></tr>
<tr><td>Folien</td><td>Vier Stufen, Vermögensbildung, Schätzfolie, Bildung, Mieter:innen und Eigentümer:innen, Seitenleisten der Gruppenfolien</td><td>Männer und Frauen, Alter, Ost und West, Migration, Beruf</td></tr>
</tbody>
</table>

<div class="ex">
  <div class="exh">Dasselbe Paar, zweimal gezählt</div>
  <div class="row"><span>Paar mit 150.000&nbsp;€ Nettovermögen</span><span>als Haushalt im <b style="color:#2e7d32">Park</b></span><span>einzeln je 75.000&nbsp;€: <b style="color:#4b4b4b">steiniger Weg</b></span></div>
</div>

<p class="read">Weil Haushalte Vermögen bündeln, liegen sie weiter oben als einzelne Personen. Die Stufen gelten für Haushalte.</p>

<div class="sources">
¹ <a href="https://publikationen.bundesbank.de/caas/v1/media/955436/data/dbdce1fbc3b7f0ac7fc8b3727c17112a">Bundesbank, PHF 2023, Tabellenanhang, Tab. 1</a> · ² <a href="https://doi.org/10.18723/diw_wb:2020-29-1">DIW Wochenbericht 29/2020 (SOEP inkl. Hochvermögenden-Stichprobe)</a>; Anteile interpoliert
</div>

<style>
.hp { width: 100%; border-collapse: collapse; margin-top: 0.6rem; font-size: 0.72rem; line-height: 1.3; }
.hp th { text-align: left; font-size: 0.72rem; border-bottom: 2px solid #8A8478; padding: 0.3rem 0.6rem; }
.hp td { vertical-align: top; border-bottom: 1px solid #DDD6CA; padding: 0.35rem 0.6rem; }
.hp td:first-child { width: 20%; opacity: 0.7; }
.hp td:nth-child(2), .hp td:nth-child(3) { width: 40%; }
.hp td.n { font-size: 0.95rem; font-weight: 700; }
.ex { margin-top: 0.8rem; padding: 0.45rem 0.8rem; border-left: 3px solid #8A8478; background: rgba(138,132,120,0.08); }
.exh { font-size: 0.68rem; font-weight: 700; margin-bottom: 0.2rem; }
.row { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem; font-size: 0.72rem; }
.read { font-size: 0.62rem; line-height: 1.35; opacity: 0.7; margin-top: 0.5rem; }
.sources { position: absolute; left: 3.5rem; right: 3.5rem; bottom: 0.9rem; font-size: 0.5rem; line-height: 1.4; opacity: 0.6; }
.sources a { color: inherit; text-decoration: underline; text-underline-offset: 2px; }
</style>

<!--
Warum die Zahlen so verschieden sind:
- Haushalte bündeln Vermögen. Ein Paar mit gemeinsamer Wohnung ist ein Haushalt mit dem ganzen Wert, aber zwei Personen mit je einem Teil.
- Bei Personen zählen auch Erwachsene ohne eigenes Vermögen mit, die in einem vermögenden Haushalt leben (z. B. erwachsene Kinder bei den Eltern, Partner:innen ohne Eigentumsanteil).
- Es gibt mehr Erwachsene (ca. 70 Mio.) als Haushalte (40,8 Mio.). Dieselben Reichen sind deshalb unter den Personen ein kleinerer Anteil.

Wie die Anteile entstehen:
- Haushalte: Perzentile PHF 2023 (P40 = 49.300 €, Median = 103.200 €, P90 = 779.500 €, P95 = 1.227.900 €); 100.000 € liegt beim 49.–50. Perzentil, 1 Mio. € beim 92.–93.
- Personen: Perzentile aller Erwachsenen 2019 (Median 22.800 €, P75 126.000 €, DIW WB 29/2020 Tab. 1); 100.000 € liegt etwa beim 69.–72. Perzentil. Über 1 Mio. €: die oberste Gruppe des DIW, rund 1,5 % der Erwachsenen.
- Die Spannen kommen von linearer gegenüber logarithmischer Interpolation.

Grenzen: Die beiden Befragungen unterscheiden sich auch in Jahr (2019 / 2023; der Haushaltsmedian lag 2017 bei 70.800 €, 2021 bei 106.600 €, die Jahre allein erklären den Faktor 4,5 also nicht) und Methode (das SOEP enthält eine Zusatzstichprobe sehr Vermögender, die PHF nicht). Die Zusatzstichprobe würde eher mehr Personen über 1 Mio. € ergeben, nicht weniger; der Unterschied geht also auf die Zählweise zurück.

Die Teilhabebefragung (Folie zu Behinderung) zählt Personen, aber mit dem Vermögen der Person und ihres Partners zusammen, ohne Immobilien. Sie passt in keine der beiden Spalten genau.
-->
