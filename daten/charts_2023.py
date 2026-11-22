"""Grafiken Bildung und Mieter/Eigentümer mit PHF 2023 (Bundesbank-Tabellenanhang, Tab. 2 und 4)."""
import os
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
S = ["#2a78d6", "#eb6834"]

# --- Bildung: Median und Mittelwert (Tab. 2) ---
bildung = [
    ("ohne Schulabschluss", 500, 71400),
    ("Haupt-/Volksschule", 77000, 248700),
    ("Realschule", 91100, 294100),
    ("(Fach-)Hochschulreife", 146500, 418500),
    (None, None, None),
    ("ohne Berufsabschluss", 6000, 69600),
    ("Lehre (dual)", 85800, 263500),
    ("Fachschule", 274500, 500000),
    ("Fachhochschule", 115300, 353200),
    ("Hochschule", 270300, 549800),
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
    r = mean / med
    ax.text(mean * 1.12, y, (f"× {r:.1f}" if r < 10 else f"× {r:.0f}").replace(".", ","), va="center", fontsize=9, color=INK2)
    ticks.append(y); labels.append(name)
    y += 1
ax.set_xscale("log")
ax.set_xlim(100, 1_000_000)
ax.set_xticks([100, 1000, 10000, 100000, 1000000])
ax.set_xticklabels(["100 €", "1.000 €", "10.000 €", "100.000 €", "1 Mio. €"], fontsize=9)
ax.set_yticks(ticks); ax.set_yticklabels(labels, fontsize=9.5)
ax.invert_yaxis()
ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.tick_params(length=0)
ax.text(115, -0.75, "Schulbildung", fontsize=9, color=INK2, va="center")
ax.text(115, 4.1, "Berufsabschluss", fontsize=9, color=INK2, va="center")
ax.legend(frameon=False, fontsize=9.5, ncol=2, loc="upper right", bbox_to_anchor=(1, 1.1))
fig.tight_layout()
fig.savefig(os.path.join(OUT, "bildung.svg"), transparent=True)
plt.close(fig)

# --- Mieter / Eigentümer: Bayes aus Eigentumsquote je Vermögensgruppe (Tab. 4) ---
w = [0.2, 0.2, 0.2, 0.2, 0.1, 0.1]
own = [3, 2, 36, 77, 92, 90]
series = {}
for name, p in [("Mieter:innen", [100 - x for x in own]), ("Eigentümer:innen", own)]:
    j = [a / 100 * b for a, b in zip(p, w)]
    t = sum(j)
    series[name] = [x / t * 100 for x in j]
bins = ["ärmste 20 %\nunter 7.100 €", "20–40 %\nbis 49.300 €", "40–60 %\nbis 196.100 €",
        "60–80 %\nbis 473.500 €", "80–90 %\nbis 779.500 €", "reichste 10 %\nab 779.500 €"]
ref = [20, 20, 20, 20, 10, 10]
fig, ax = plt.subplots(figsize=(7.8, 3.6))
bw = 0.4
for i, (name, c) in enumerate(zip(series, S)):
    d = series[name]
    xs = [k - 0.4 + bw * (i + 0.5) for k in range(6)]
    ax.bar(xs, d, width=bw - 0.03, color=c, label=name, zorder=3, edgecolor="white", linewidth=1)
    for k, (x, v) in enumerate(zip(xs, d)):
        r = ref[k]
        yy = max(v, r) if -2 < r - v < 6 else v
        ax.text(x, yy + 0.6, (f"{v:.1f}" if v < 10 else f"{v:.0f}").replace(".", ",") + " %",
                ha="center", va="bottom", fontsize=9, color=INK2)
for k, v in enumerate(ref):
    ax.plot([k - 0.43, k + 0.43], [v, v], color=INK, lw=1.4, zorder=4,
            label="alle Haushalte" if k == 0 else None, dashes=(3, 2))
ax.set_xticks(range(6)); ax.set_xticklabels(bins, fontsize=8.8)
ax.set_ylim(0, 45)
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:.0f} %"))
ax.grid(axis="y", color=GRID, lw=0.8, zorder=0)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.tick_params(axis="y", length=0, labelsize=9); ax.tick_params(axis="x", length=0)
ax.set_ylabel("Anteil der Haushalte", fontsize=9.5)
ax.legend(frameon=False, fontsize=9.5, ncol=3, loc="lower right", bbox_to_anchor=(1, 1.0))
fig.tight_layout()
fig.savefig(os.path.join(OUT, "wohnen.svg"), transparent=True)
plt.close(fig)
print({k: [round(x, 1) for x in v] for k, v in series.items()})
