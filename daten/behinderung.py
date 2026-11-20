"""Behinderung: vier Einzelgrafiken (Teilhabebefragung BMAS/infas, Abschlussbericht 2022, S. 171–172)."""
import os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "..", "public", "gruppen")
plt.rcParams.update({"svg.fonttype": "none", "font.family": "sans-serif", "font.sans-serif": ["Inter", "DejaVu Sans"],
    "font.size": 11, "axes.edgecolor": "#8A8478", "xtick.color": "#52514e", "ytick.color": "#52514e", "text.color": "#0b0b0b"})
INK2, GRID = "#52514e", "#DDD6CA"
FARBEN = ["#2a78d6", "#f0a070", "#c4471b"]   # ohne · mit Beeinträchtigung · mit Behinderung (zwei Orangetöne)
panels = [
    ("spart", "spart jeden Monat", [82, 75, 62]),
    ("ruecklage", "könnte 1.000 € nicht aus Erspartem zahlen", [8, 13, 26]),
    ("schulden", "hat Kreditschulden", [22, 22, 27]),
    ("vermoegen", "Vermögen ab 25.000 € (ohne Immobilien)", [44, 42, 29]),
]
for key, title, vals in panels:
    fig, ax = plt.subplots(figsize=(3.7, 1.95))
    xs = range(3)
    ax.bar(xs, vals, width=0.72, color=FARBEN, edgecolor="white", linewidth=1, zorder=3)
    for x, v in zip(xs, vals):
        ax.text(x, v + 2.5, f"{v} %", ha="center", va="bottom", fontsize=10, color=INK2)
    ax.set_ylim(0, 100); ax.set_xticks([])
    ax.set_yticks([0, 50, 100]); ax.set_yticklabels(["0 %", "50 %", "100 %"], fontsize=8.5)
    ax.grid(axis="y", color=GRID, lw=0.8, zorder=0)
    for s in ["top", "right", "left"]: ax.spines[s].set_visible(False)
    ax.tick_params(length=0)
    ax.set_title(title, fontsize=10, loc="left", color="#0b0b0b", pad=6)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, f"behinderung-{key}.svg"), transparent=True); plt.close(fig)
print("ok")

# Legende als eigenes Bild (wird über den vier Grafiken eingebunden)
from matplotlib.patches import Patch
fig = plt.figure(figsize=(7.6, 0.35))
fig.legend(handles=[Patch(color=c, label=l) for c, l in zip(FARBEN, ["ohne Beeinträchtigung", "mit Beeinträchtigung",
           "mit selbsteingeschätzter Behinderung"])], loc="center left", ncol=3, frameon=False, fontsize=10,
           handlelength=1.2, columnspacing=1.6)
fig.savefig(os.path.join(OUT, "behinderung-legende.svg"), transparent=True); plt.close(fig)
print("legende ok")
