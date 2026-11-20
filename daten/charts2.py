"""Grafiken für Stellung im Beruf, Mieter/Eigentümer, Behinderung (SVG, Text bleibt Text)."""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "public", "gruppen")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({
    "svg.fonttype": "none", "font.family": "sans-serif", "font.sans-serif": ["Inter", "DejaVu Sans"],
    "font.size": 11, "axes.edgecolor": "#8A8478", "axes.labelcolor": "#52514e",
    "xtick.color": "#52514e", "ytick.color": "#52514e", "text.color": "#0b0b0b",
})
INK, INK2, GRID = "#0b0b0b", "#52514e", "#DDD6CA"
S = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]


def fmt(v):
    return (f"{v:.1f}" if v < 10 else f"{v:.0f}").replace(".", ",") + " %"


def grouped(fname, series, bins, colors, ref=None, ref_label=None, ylabel="Anteil der Gruppe",
            note=None, note_xy=None, skip_labels=(), ymax=100, w=7.6, h=3.6, xfs=9.5, ncol=None, ints=False):
    fig, ax = plt.subplots(figsize=(w, h))
    names = list(series)
    n, nb = len(names), len(bins)
    bw = 0.8 / n
    for i, (name, c) in enumerate(zip(names, colors)):
        d = series[name]
        xs = [k - 0.4 + bw * (i + 0.5) for k in range(nb)]
        ax.bar(xs, d, width=bw - 0.03, color=c, label=name, zorder=3, edgecolor="white", linewidth=1)
        for k, (x, v) in enumerate(zip(xs, d)):
            if k in skip_labels:
                continue
            r = ref[k] if ref else 0
            y = max(v, r) if (ref and -2 < r - v < 6) else v
            ax.text(x, y + ymax * 0.012, (f"{v:.0f} %" if ints else fmt(v)), ha="center", va="bottom",
                    fontsize=8 if n > 3 else (8.5 if n > 2 else 9.5), color=INK2)
    if ref:
        for k, v in enumerate(ref):
            ax.plot([k - 0.43, k + 0.43], [v, v], color=INK, lw=1.4, zorder=4,
                    label=ref_label if k == 0 else None, dashes=(3, 2))
    ax.set_xticks(range(nb)); ax.set_xticklabels(bins, fontsize=xfs)
    ax.set_ylim(0, ymax)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:.0f} %"))
    ax.grid(axis="y", color=GRID, lw=0.8, zorder=0)
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.tick_params(axis="y", length=0, labelsize=9); ax.tick_params(axis="x", length=0)
    ax.set_ylabel(ylabel, fontsize=9.5)
    ax.legend(frameon=False, fontsize=9.5, ncol=ncol or (n + (1 if ref else 0)), loc="lower right", bbox_to_anchor=(1, 1.0))
    if note:
        ax.annotate(note, xy=note_xy[0], xytext=note_xy[1], fontsize=9.5, color=INK, ha="left",
                    arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, fname), transparent=True)
    plt.close(fig)


d = json.load(open(os.path.join(HERE, "gruppen_verteilung_2.json")))

# 1) Stellung im Beruf (SOEP 2019); Referenz: alle Erwerbsaktiven
w = [0.50, 0.25, 0.235, 0.015]; aktiv = [59, 65, 59, 62]
j = [a / 100 * b for a, b in zip(aktiv, w)]; ref = [x / sum(j) * 100 for x in j]
order = ["Selbstständige", "Beamt:innen", "Angestellte", "Arbeiter:innen"]
ser = {k: [x * 100 for x in d["beruf"][k]["verteilung"]] for k in order}
top = "\n".join(f"{k}: {fmt(ser[k][3])}" for k in order)
grouped("beruf.svg", ser,
        ["untere Hälfte\nunter 22.800 €", "51.–75. Perzentil\n22.800–126.000 €",
         "76.–98,5. Perzentil\n126.000 € – ca. 1 Mio. €", "oberste 1,5 %\nMillionär:innen"],
        S, ref=ref, ref_label="alle Erwerbstätigen", skip_labels=(3,), ymax=70, w=7.8, h=3.9, ncol=3,
        note="in den obersten 1,5 %:\n" + top, note_xy=((3.0, 4), (2.55, 40)))

# 2) Mieter / Eigentümer (PHF 2021, Haushalte)
ser = {k: [x * 100 for x in d["wohnen"][k]["verteilung"]] for k in ["Mieter:innen", "Eigentümer:innen"]}
grouped("wohnen.svg", ser,
        ["ärmste 20 %\nunter 6.900 €", "20–40 %\nbis 43.800 €", "40–60 %\nbis 185.400 €",
         "60–80 %\nbis 430.700 €", "80–90 %\nbis 725.900 €", "reichste 10 %\nab 725.900 €"],
        S[:2], ref=[20, 20, 20, 20, 10, 10], ref_label="alle Haushalte", ymax=45, w=7.8, xfs=8.8,
        ylabel="Anteil der Haushalte")

# 3) Behinderung: siehe behinderung.py (vier Einzelgrafiken)
print("ok", sorted(os.listdir(OUT)))
