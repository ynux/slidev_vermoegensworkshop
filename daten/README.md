Der Ordner daten/ enthält die Rechnungen hinter den Grafiken. In Slidev wird er nicht gebraucht; die Folien greifen nur auf public/gruppen/*.svg zu. Er ist dafür da, dass du die Zahlen nachprüfen und die Grafiken neu erzeugen kannst.

Inhalt:

bayes.py nimmt die DIW-Tabelle 4 (Anteil von Frauen, Ostdeutschen, Menschen mit Migrationshintergrund und Altersgruppen in jeder Vermögensgruppe). Daraus rechnet es mit dem Satz von Bayes die Verteilung jeder Gruppe über die vier Vermögensgruppen aus. Es prüft auch, wie stark sich die Rundung der Eingaben auf ganze Prozent auswirkt.
bayes2.py macht dasselbe für Stellung im Beruf (DIW-Tabelle 4) und für Mieter/Eigentümer (Eigentümerquote je Vermögensgruppe, Bundesbank 2021).
gruppen_verteilung_soep2019.json und gruppen_verteilung_2.json sind die Ergebnisse dieser Rechnungen.
charts.py zeichnet die ersten fünf Grafiken: Geschlecht, Alter, Ost/West, Migration, Bildung.
charts2.py zeichnet die drei neuen: Beruf, Wohnen, Behinderung.

Zum Neu-Erzeugen ruft man im Projektordner nacheinander python3 daten/bayes.py, python3 daten/bayes2.py, python3 daten/charts.py und python3 daten/charts2.py auf. Dafür braucht man Python mit matplotlib. Die SVGs landen dann in public/gruppen/.

says Claude
