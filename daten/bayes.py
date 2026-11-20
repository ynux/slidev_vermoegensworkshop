# Aus DIW WB 29/2020, Tab. 4 (Anteil eines Merkmals in jeder Vermögensgruppe, SOEP 2019, Erwachsene)
# wird die Verteilung jeder Gruppe über die vier Vermögensgruppen berechnet (Satz von Bayes).
import json, itertools
w = [0.50, 0.25, 0.235, 0.015]   # Breite der Vermögensgruppen (Anteil aller Erwachsenen)
bins = ["untere Hälfte", "51.–75. Perzentil", "76.–98,5. Perzentil", "oberste 1,5 %"]
tab4 = {
  "Geschlecht": {"Frauen":[53,50,48,31], "Männer":[47,50,52,69]},
  "Migrationshintergrund": {"mit Migrationshintergrund":[31,19,12,14], "ohne Migrationshintergrund":[69,81,88,86]},
  "Wohnort": {"Ost (neue Länder)":[20,20,8,6], "West (alte Länder)":[80,80,92,94]},
  "Alter": {"18–24":[16,1,0,0], "25–49":[46,38,23,23], "50–64":[19,32,39,37], "65+":[19,29,38,40]},
}
def dist(shares, wts=w):
    joint=[s/100*b for s,b in zip(shares,wts)]
    tot=sum(joint)
    return tot,[j/tot for j in joint]
out={}
for g,sub in tab4.items():
    out[g]={}
    for name,s in sub.items():
        tot,d=dist(s)
        out[g][name]={"anteil_bevoelkerung":tot,"verteilung":d,"rel_dichte":[x/b for x,b in zip(d,w)]}
        print(f"{g:22s}{name:20s} Bev.={tot*100:5.1f}%  "+"  ".join(f"{x*100:5.1f}%" for x in d)+"   rel: "+" ".join(f"{r:.2f}" for r in out[g][name]['rel_dichte']))
# Rundungsempfindlichkeit für die oberste Gruppe: Eingaben ±0,5 Pp
print("\nSensitivität oberste 1,5 % (Eingaben ±0,5 Prozentpunkte):")
for g,sub in tab4.items():
    for name,s in sub.items():
        vals=[]
        for d in itertools.product([-0.5,0,0.5],repeat=4):
            ss=[max(0,a+b) for a,b in zip(s,d)]
            vals.append(dist(ss)[1][3])
        print(f"  {g}/{name}: {min(vals)*100:.2f}–{max(vals)*100:.2f} %")
json.dump({"bins":bins,"breite":w,"gruppen":out,"quelle":"DIW Wochenbericht 29/2020, Tabelle 4, S. 520; eigene Umrechnung"},open("gruppen_verteilung_soep2019.json","w"),ensure_ascii=False,indent=1)
