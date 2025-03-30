import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from plot import *


# DIVIDING FACTOR 
# 2_000_000 for the vf2
# 200_000 for the premier

# Read CSV
csv = pd.read_csv(f"boot/{HARDWARE}.csv")

# Remove 'Firmware exit' column
csv = csv.drop('Firmware exit', axis=1)

if HARDWARE == "premier":
    csv = csv.groupby(csv.index // 4).sum()

# Normalize each row to sum to 1
csv = csv.apply(lambda row: row / row.sum() if row.sum() > 0 else row, axis=1)

# Truncate data
# print(len(csv))
# csv = csv.head(200)
# print(len(csv))

# Prepare data
data = {}
for col in csv.columns:
    data[col] = np.array(csv[col])

unit_of_time = np.arange(0, len(csv), 1)

fig, ax = plt.subplots()
fig.set_figheight(3.2)
fig.set_figwidth(5.4)

# Convert unit_of_time to labels (every 2 minutes)
unit_of_time_labels = list(map(lambda x: f"{2 * x}s", unit_of_time))

# Compute cumulative sums for stacking
stacked_values = np.zeros_like(unit_of_time, dtype=float)
for i, (label, values) in enumerate(data.items()):
    ax.fill_between(unit_of_time, stacked_values, stacked_values + values, 
                    step="post", label=label, alpha=0.8)
    stacked_values += values  # Stack values

# Set x-axis ticks
ax.set_xticks(unit_of_time[::50])
ax.set_xticklabels(unit_of_time_labels[::50])

# Labels and formatting
# ax.set_title(f"Proportion of exceptions per category on the {HARDWARE}")
# ax.set_xlabel('CPU cycles')
ax.set_ylabel('Proportion of traps to firmware')
ax.set_ylim(0, 1)
ax.set_xlim(0, 180) # max is 256

# Vertical reference line
# ax.axvline(x=113, color='black', linestyle='--')

# Minor ticks for y-axis
ax.yaxis.set_minor_locator(mticker.MultipleLocator(.2))

from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset

# Define zoom area (e.g., first 20 CPU cycles)
x1, x2 = 18, 30
y1, y2 = 0, 0.04  # Zoom sur toute la hauteur


if HARDWARE == "premier":
    x1, x2 = 45, 55
    y1, y2 = 0, 0.015   

# Create inset

if HARDWARE == "premier":
    axins = zoomed_inset_axes(ax, zoom=9, loc="right")
else:
    axins = zoomed_inset_axes(ax, zoom=10.5, loc="lower right")  # Facteur de zoom ajustable

# Replot same data in inset
stacked_values_zoom = np.zeros_like(unit_of_time[:x2], dtype=float)
for label, values in data.items():
    axins.fill_between(unit_of_time[:x2], stacked_values_zoom, stacked_values_zoom + values[:x2], step="post", alpha=0.8)
    stacked_values_zoom += values[:x2]

# Format inset
axins.set_xlim(x1, x2-4)
axins.set_ylim(y1, y2)
axins.set_xticks([])  # Enlever les ticks pour plus de lisibilité
axins.set_yticks([])

# Draw rectangle on main plot
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="black", linestyle="-")


# Place legend outside the plot
ax.legend(loc="lower center", bbox_to_anchor=(0.45, -0.28), fancybox=False, ncol=3, labelspacing=-0.06, columnspacing=0.8, frameon=False)
plt.suptitle(TITLE)

ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=2)
plt.tight_layout(rect=[0, 0, 1, 1])  # Ajuste l'espace en bas

# Save as PDF
plt.savefig(f"plots/boot_{HARDWARE}.pdf", format="pdf")
plt.savefig(f"plots/boot_{HARDWARE}", dpi=400)