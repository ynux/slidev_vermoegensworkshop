"""Gruppen-Grafiken mit drei Vermögensgruppen (SOEP 2019, Personen):
untere Hälfte · 51.–75. Perzentil · obere 25 % (die beiden oberen DIW-Gruppen zusammengefasst).
Ersetzt geschlecht/alter/ost-west/migration/beruf aus charts.py und charts2.py."""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "public", "gruppen")
plt.rcParams.update({
    "svg.fonttype": "none", "font.family": "sans-serif", "font.sans-serif": ["Inter", "DejaVu Sans"],
    "font.size": 11, "axes.edgecolor": "#8A8478", "axes.labelcolor": "#52514e",
    "xtick.color": "#52514e", "ytick.color": "#52514e", "text.color": "#0b0b0b",
})
INK, INK2, GRID = "#0b0b0b", "#52514e", "#DDD6CA"
S = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]
BINS = ["untere Hälfte\nunter 22.800 €", "51.–75. Perzentil\n22.800–126.000 €", "obere 25 %\nab 126.000 €"]


def merge(v):
    return [v[0] * 100, v[1] * 100, (v[2] + v[3]) * 100]


def grouped(fname, series, colors, ref, ref_label, ymax, w=7.6, h=3.6):
    fig, ax = plt.subplots(figsize=(w, h))
    names = list(series)
    n = len(names)
    bw = 0.8 / n
    for i, (name, c) in enumerate(zip(names, colors)):
        d = series[name]
        xs = [k - 0.4 + bw * (i + 0.5) for k in range(3)]
        ax.bar(xs, d, width=bw - 0.03, color=c, label=name, zorder=3, edgecolor="white", linewidth=1)
        for k, (x, v) in enumerate(zip(xs, d)):
            r = ref[k]
            y = max(v, r) if -2 < r - v < 6 else v
            ax.text(x, y + ymax * 0.012, f"{v:.0f} %", ha="center", va="bottom",
                    fontsize=8.5 if n > 2 else 9.5, color=INK2)
    for k, v in enumerate(ref):
        ax.plot([k - 0.43, k + 0.43], [v, v], color=INK, lw=1.4, zorder=4,
                label=ref_label if k == 0 else None, dashes=(3, 2))
    ax.set_xticks(range(3)); ax.set_xticklabels(BINS, fontsize=9.5)
    ax.set_ylim(0, ymax)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:.0f} %"))
    ax.grid(axis="y", color=GRID, lw=0.8, zorder=0)
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.tick_params(axis="y", length=0, labelsize=9); ax.tick_params(axis="x", length=0)
    ax.set_ylabel("Anteil der Gruppe", fontsize=9.5)
    ax.legend(frameon=False, fontsize=9.5, ncol=min(n + 1, 3), loc="lower right", bbox_to_anchor=(1, 1.0))
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, fname), transparent=True)
    plt.close(fig)


G = json.load(open(os.path.join(HERE, "gruppen_verteilung_soep2019.json")))["gruppen"]
ALLE = [50, 25, 25]
for fname, key, names, ymax in [
    ("geschlecht.svg", "Geschlecht", ["Frauen", "Männer"], 62),
    ("ost-west.svg", "Wohnort", ["Ost (neue Länder)", "West (alte Länder)"], 68),
    ("migration.svg", "Migrationshintergrund", ["mit Migrationshintergrund", "ohne Migrationshintergrund"], 75),
    ("alter.svg", "Alter", ["18–24", "25–49", "50–64", "65+"], 108),
]:
    grouped(fname, {k: merge(G[key][k]["verteilung"]) for k in names}, S[:len(names)], ALLE,
            "alle Erwachsenen", ymax)

# Stellung im Beruf; Referenz: alle Erwerbsaktiven (Anteil je DIW-Gruppe 59/65/59/62 %)
d = json.load(open(os.path.join(HERE, "gruppen_verteilung_2.json")))
w = [0.50, 0.25, 0.235, 0.015]; aktiv = [59, 65, 59, 62]
j = [a / 100 * b for a, b in zip(aktiv, w)]; ref4 = [x / sum(j) for x in j]
order = ["Selbstständige", "Beamt:innen", "Angestellte", "Arbeiter:innen"]
grouped("beruf.svg", {k: merge(d["beruf"][k]["verteilung"]) for k in order}, S, merge(ref4),
        "alle Erwerbstätigen", 75, w=7.8, h=3.9)
print("ok")
