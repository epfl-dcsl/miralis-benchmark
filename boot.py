import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


csv = pd.read_csv("boot.csv")

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.ticker as mticker

csv = csv.drop('Firmware exit', axis=1)

csv = csv.apply(lambda row: row / row.sum() if row.sum() > 0 else row, axis=1)



data = {}
for col in csv.columns:
    data[col] = np.array(csv[col])
    unit_of_time = np.arange(0, len(data[col]), 1)

fig, ax = plt.subplots()

unit_of_time = list(map(lambda x:  str(2 * x) + "m", unit_of_time))
ax.stackplot(unit_of_time, data.values(),
             labels=data.keys(), alpha=0.8)

ax.set_xticks(unit_of_time[::50])
ax.legend(loc='upper left', reverse=True)
ax.set_title('Proportion of exceptions per category')
ax.set_xlabel('Cpu cycles')
ax.set_ylabel('Proportion')

ax.set_ylim(0,1)
ax.set_xlim(0,250)
ax.axvline(x=113, color='black', linestyle='--')
# add tick at every 200 million people
ax.yaxis.set_minor_locator(mticker.MultipleLocator(.2))

# Place legend outside the plot
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

# Adjust layout to make space for the legend
plt.tight_layout()

plt.savefig("plots/boot.png", dpi=500)