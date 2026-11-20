"""Erzeugt die Grafiken für die Gruppen-Folien als SVG (Text bleibt Text, Schrift kommt von Slidev)."""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "public", "gruppen")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "svg.fonttype": "none",
    "font.family": "sans-serif",
    "font.sans-serif": ["Inter", "DejaVu Sans"],
    "font.size": 11,
    "axes.edgecolor": "#8A8478",
    "axes.labelcolor": "#52514e",
    "xtick.color": "#52514e",
    "ytick.color": "#52514e",
    "text.color": "#0b0b0b",
})
INK, INK2, GRID = "#0b0b0b", "#52514e", "#DDD6CA"
S = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]  # Kategorial, feste Reihenfolge

data = json.load(open(os.path.join(HERE, "gruppen_verteilung_soep2019.json")))
BINS = ["untere Hälfte\nunter 22.800 €", "51.–75. Perzentil\n22.800–126.000 €",
        "76.–98,5. Perzentil\n126.000 € – ca. 1 Mio. €", "oberste 1,5 %\nMillionär:innen"]
ALLE = [50, 25, 23.5, 1.5]


def fmt(v):
    return (f"{v:.1f}" if v < 10 else f"{v:.0f}").replace(".", ",") + " %"


def grouped(fname, groups, names, colors, note=None, ymax=None, w=7.6, h=3.6):
    fig, ax = plt.subplots(figsize=(w, h))
    n = len(names)
    bw = 0.8 / n
    vals_all = []
    for i, (name, c) in enumerate(zip(names, colors)):
        d = [x * 100 for x in groups[name]["verteilung"]]
        vals_all += d
        xs = [k - 0.4 + bw * (i + 0.5) for k in range(4)]
        ax.bar(xs, d, width=bw - 0.03, color=c, label=name, zorder=3,
               edgecolor="white", linewidth=1)
        for k, (x, v) in enumerate(zip(xs, d)):
            if n > 2 and k == 3:
                continue  # oberste Gruppe: Werte stehen im Kasten
            ax.text(x, max(v, ALLE[k] if -2 < ALLE[k] - v < 6 else 0) + 1.2, fmt(v), ha="center",
                    va="bottom", fontsize=8.5 if n > 2 else 9.5, color=INK2)
    # Referenz: alle Erwachsenen
    for k, v in enumerate(ALLE):
        ax.plot([k - 0.43, k + 0.43], [v, v], color=INK, lw=1.4, zorder=4,
                label="alle Erwachsenen" if k == 0 else None, dashes=(3, 2))
    ax.set_xticks(range(4))
    ax.set_xticklabels(BINS, fontsize=9.5)
    ax.set_ylim(0, ymax or max(vals_all) * 1.18)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:.0f} %"))
    ax.grid(axis="y", color=GRID, lw=0.8, zorder=0)
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.tick_params(axis="y", length=0, labelsize=9)
    ax.tick_params(axis="x", length=0)
    ax.set_ylabel("Anteil der Gruppe", fontsize=9.5)
    ax.legend(frameon=False, fontsize=9.5, ncol=n + 1, loc="upper right", bbox_to_anchor=(1, 1.12))
    if note:
        ax.annotate(note, xy=(3, 2.5), xytext=(2.55, (ymax or max(vals_all) * 1.18) * 0.55),
                    fontsize=9.5, color=INK, ha="left",
                    arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, fname), transparent=True)
    plt.close(fig)


G = data["gruppen"]
grouped("geschlecht.svg", G["Geschlecht"], ["Frauen", "Männer"], S[:2], ymax=62,
        note="Männer sind hier\n2,3-mal so häufig")
grouped("ost-west.svg", G["Wohnort"], ["Ost (neue Länder)", "West (alte Länder)"], S[:2], ymax=68,
        note="Westdeutsche sind hier\n3,2-mal so häufig")
grouped("migration.svg", G["Migrationshintergrund"], ["mit Migrationshintergrund", "ohne Migrationshintergrund"], S[:2], ymax=75,
        note="ohne Migrationshinter-\ngrund 1,9-mal so häufig")
top = "  ·  ".join(f"{a}: {fmt(G['Alter'][a]['verteilung'][3]*100)}" for a in ["18–24", "25–49", "50–64", "65+"])
grouped("alter.svg", G["Alter"], ["18–24", "25–49", "50–64", "65+"], S[:4], ymax=108, w=7.8,
        note="in den obersten 1,5 %:\n" + top.replace("  ·  ", "\n"))


# Bildung: Median und Mittelwert je Gruppe (PHF 2021, Haushalte nach Referenzperson)
bildung = [
    ("ohne Schulabschluss", 1700, 36100),
    ("Haupt-/Volksschule", 63600, 236000),
    ("Realschule", 115400, 315800),
    ("(Fach-)Hochschulreife", 137300, 401300),
    (None, None, None),
    ("ohne Berufsabschluss", 8200, 95000),
    ("Lehre (dual)", 102100, 270100),
    ("Fachschule", 220500, 431400),
    ("Fachhochschule", 105600, 415600),
    ("Hochschule", 246300, 505500),
]
fig, ax = plt.subplots(figsize=(7.6, 3.9))
y = 0
ticks, labels = [], []
for name, med, mean in bildung:
    if name is None:
        y += 0.6
        continue
    ax.plot([med, mean], [y, y], color=GRID, lw=3, zorder=1, solid_capstyle="round")
    ax.scatter([med], [y], s=46, color=S[0], zorder=3, label="Median" if y == 0 else None)
    ax.scatter([mean], [y], s=46, color=S[1], zorder=3, label="Mittelwert" if y == 0 else None)
    ratio = mean / med
    ax.text(mean * 1.12, y, (f"× {ratio:.1f}" if ratio < 10 else f"× {ratio:.0f}").replace(".", ","), va="center", fontsize=9, color=INK2)
    ticks.append(y); labels.append(name)
    y += 1
ax.set_xscale("log")
ax.set_xlim(1000, 1_000_000)
ax.set_xticks([1000, 10000, 100000, 1000000])
ax.set_xticklabels(["1.000 €", "10.000 €", "100.000 €", "1 Mio. €"], fontsize=9)
ax.set_yticks(ticks); ax.set_yticklabels(labels, fontsize=9.5)
ax.invert_yaxis()
ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.tick_params(length=0)
ax.text(1150, -0.75, "Schulbildung", fontsize=9, color=INK2, va="center")
ax.text(1150, 4.1, "Berufsabschluss", fontsize=9, color=INK2, va="center")
ax.legend(frameon=False, fontsize=9.5, ncol=2, loc="upper right", bbox_to_anchor=(1, 1.1))
fig.tight_layout()
fig.savefig(os.path.join(OUT, "bildung.svg"), transparent=True)
plt.close(fig)
print("ok", os.listdir(OUT))
