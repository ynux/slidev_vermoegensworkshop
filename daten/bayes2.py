"""Zwei weitere Gruppen-Verteilungen.
1) Stellung im Beruf: DIW WB 29/2020, Tab. 4 (SOEP 2019). Annahme: Die Zeilen 'Stellung im Beruf'
   beziehen sich auf die Personen mit Arbeitsmarktstatus 'aktiv' in derselben Vermögensgruppe.
2) Mieter/Eigentümer: Bundesbank PHF 2021, Monatsbericht April 2023, S. 49 (Prävalenz selbstgenutztes
   Wohneigentum je Nettovermögens-Quantil)."""
import json
w = [0.50, 0.25, 0.235, 0.015]
aktiv = [59, 65, 59, 62]
beruf = {"Selbstständige":[4,8,19,73], "Beamt:innen":[4,7,10,4], "Angestellte":[53,63,59,22], "Arbeiter:innen":[23,20,12,2]}
out = {"beruf": {}, "wohnen": {}}
for k, s in beruf.items():
    j = [si/100*a/100*b for si, a, b in zip(s, aktiv, w)]
    t = sum(j); d = [x/t for x in j]
    out["beruf"][k] = {"anteil_bev": t, "verteilung": d}
    print(f"{k:16s} {t*100:5.1f}% der Erw.  " + "  ".join(f"{x*100:5.1f}%" for x in d))
w2 = [0.2, 0.2, 0.2, 0.2, 0.1, 0.1]
own = [2, 4, 40, 83, 93, 93]
for name, p in [("Eigentümer:innen", own), ("Mieter:innen", [100-x for x in own])]:
    j = [pi/100*b for pi, b in zip(p, w2)]; t = sum(j); d = [x/t for x in j]
    out["wohnen"][name] = {"anteil_haushalte": t, "verteilung": d}
    print(f"{name:16s} {t*100:5.1f}% der HH   " + "  ".join(f"{x*100:5.1f}%" for x in d))
json.dump(out, open("gruppen_verteilung_2.json", "w"), ensure_ascii=False, indent=1)
