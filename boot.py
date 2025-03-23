import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from plot import *

# Read CSV
csv = pd.read_csv("boot.csv")

# Remove 'Firmware exit' column
csv = csv.drop('Firmware exit', axis=1)

# Normalize each row to sum to 1
csv = csv.apply(lambda row: row / row.sum() if row.sum() > 0 else row, axis=1)

# Prepare data
data = {}
for col in csv.columns:
    data[col] = np.array(csv[col])

unit_of_time = np.arange(0, len(csv), 1)

fig, ax = plt.subplots()

# Convert unit_of_time to labels (every 2 minutes)
unit_of_time_labels = list(map(lambda x: f"{2 * x}m", unit_of_time))

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
ax.set_title(f"Proportion of exceptions per category on the {HARDWARE}")
ax.set_xlabel('CPU cycles')
ax.set_ylabel('Proportion')
ax.set_ylim(0, 1)
ax.set_xlim(0, 250)

# Vertical reference line
ax.axvline(x=113, color='black', linestyle='--')

# Minor ticks for y-axis
ax.yaxis.set_minor_locator(mticker.MultipleLocator(.2))

# Place legend outside the plot
ax.legend(loc="lower center", bbox_to_anchor=(0.5, 0), ncol=2)

# Adjust layout for better spacing
plt.tight_layout()

# Save as PDF
plt.savefig("plots/boot.pdf", format="pdf")