"""Jahrgänge im gleichen Alter: PHF 2010/11 vs. PHF 2021 (Bundesbank), Haushalte nach Alter der Referenzperson.
Nominal aus: Monatsbericht Juni 2013, S. 40 (2010/11) und Monatsbericht April 2023, S. 47 (2021).
Preisbereinigung wie bei der Bundesbank: HVPI 2010 = 100, 2021 = 117,8 (Monatsbericht April 2025, S. 33, Fn. 2)."""
import os, json
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "..", "public", "gruppen")
plt.rcParams.update({"svg.fonttype": "none", "font.family": "sans-serif", "font.sans-serif": ["Inter", "DejaVu Sans"],
    "font.size": 11, "axes.edgecolor": "#8A8478", "xtick.color": "#52514e", "ytick.color": "#52514e"})
INK2, GRID = "#52514e", "#DDD6CA"; S = ["#2a78d6", "#eb6834"]
HVPI = {"2010/11": 100.0, "2021": 117.8}
rows = [  # Label, Welle, Median nominal, Mittelwert nominal
    ("16–24 Jahre, 2010/11\ngeboren ca. 1986–1995", "2010/11", 2420, 21640),
    ("16–24 Jahre, 2021\ngeboren ca. 1997–2005", "2021", 11400, 32000),
    (None, None, None, None),
    ("25–34 Jahre, 2010/11\ngeboren ca. 1976–1986", "2010/11", 13590, 45000),
    ("25–34 Jahre, 2021\ngeboren ca. 1987–1996", "2021", 18700, 112900),
]
out = []
fig, ax = plt.subplots(figsize=(7.6, 3.5))
y = 0; ticks, labels = [], []
for lab, wave, med, mean in rows:
    if lab is None:
        y += 0.5; continue
    f = HVPI[wave] / 100
    rm, rmean = med / f, mean / f
    out.append({"gruppe": lab.replace("\n", ", "), "median_real_2010": round(rm), "mittel_real_2010": round(rmean)})
    ax.plot([rm, rmean], [y, y], color=GRID, lw=3, zorder=1, solid_capstyle="round")
    ax.scatter([rm], [y], s=50, color=S[0], zorder=3, label="Median" if y == 0 else None)
    ax.scatter([rmean], [y], s=50, color=S[1], zorder=3, label="Mittelwert" if y == 0 else None)
    t = lambda v: f"{v/1000:.1f}".replace(".", ",") + " Tsd. €" if v < 10000 else f"{v/1000:.0f} Tsd. €"
    ax.text(rm / 1.12, y, t(rm), va="center", ha="right", fontsize=9, color=INK2)
    ax.text(rmean * 1.12, y, t(rmean), va="center", ha="left", fontsize=9, color=INK2)
    ticks.append(y); labels.append(lab); y += 1
ax.set_xscale("log"); ax.set_xlim(700, 500000)
ax.set_xticks([1000, 10000, 100000]); ax.set_xticklabels(["1.000 €", "10.000 €", "100.000 €"], fontsize=9)
ax.set_yticks(ticks); ax.set_yticklabels(labels, fontsize=9.5); ax.invert_yaxis()
ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
for s in ["top", "right", "left"]: ax.spines[s].set_visible(False)
ax.tick_params(length=0)
ax.legend(frameon=False, fontsize=9.5, ncol=2, loc="lower right", bbox_to_anchor=(1, 1.0))
fig.tight_layout(); fig.savefig(os.path.join(OUT, "kohorten.svg"), transparent=True); plt.close(fig)
json.dump(out, open(os.path.join(HERE, "kohorten.json"), "w"), ensure_ascii=False, indent=1)
for o in out: print(o)
