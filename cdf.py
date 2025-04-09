import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import re
from pathlib import Path
import numpy as np
import io
from plot import *
import csv

def extract_get(file_path):
    return extract_value(file_path, "GET")

def extract_set(file_path):
    return extract_value(file_path, "SET")

def extract_value(file_path, typ):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines = lines[18:][:-2]

    def remove_duplicate_spaces(s):
        return re.sub(r'\s+', ' ', s).strip()

    lines = list(map(remove_duplicate_spaces, lines))
    lines = list(filter(lambda x: not x.startswith('---'), lines))
    lines = list(filter(lambda x: not x.startswith(typ), lines))
    lines = list(map(lambda x: np.array(x.split(' ')[1:]).astype(float), lines))

    return lines

if __name__ == "__main__":
    title = 'Network latency'
    fontsize=14
    ms=12

    fig, axes = plt.subplots(2, 1, num=1, figsize=(6.5, 3.6))  # Create subplots in a single figure

    v = [extract_get, extract_set]
    v2 = ['Get', 'Set']

    idx = 0
    for e in v:
        output = extract(f"memcached-cdf", e)

        board_values = list(map(lambda x:float(x[0]), output[0][1]))
        percentile_board = list(map(lambda x:float(x[1]), output[0][1]))

        offload_values = list(map(lambda x:float(x[0]), output[1][1]))
        percentile_offload = list(map(lambda x:float(x[1]), output[1][1]))

        protect_values = list(map(lambda x:float(x[0]), output[2][1]))
        percentile_protect = list(map(lambda x:float(x[1]), output[2][1]))

        # First subplot (Read performance)
        axes[idx].plot(percentile_board, board_values, label=names['Board'], color=curve_colors['Board'])
        axes[idx].plot(percentile_offload, offload_values, label=names['Offload'], color=curve_colors['Offload'])
        axes[idx].plot(percentile_protect, protect_values, label=names['Protect'], color=curve_colors['Protect'])
        axes[idx].set_ylabel(f"{v2[idx]} latency", fontsize=fontsize)  # Label for the y-axis
        axes[idx].yaxis.set_major_formatter(ticker.FormatStrFormatter('%d$ms$'))
         # Label for the y-axis
        if idx == 1:
            axes[idx].legend(fontsize=fontsize - 2)  # Show legend
            axes[idx].set_xlabel("Percentile", fontsize=fontsize)
        else:
            axes[idx].set_xticklabels([])
        # axes[idx].set_title(v2[idx])  # Subplot title
        #axes[idx].set_xticks(percentile_board)  # Set x-ticks
        axes[idx].set_ylim(0,50)
        axes[idx].set_xlim(10,100)

        idx += 1

    # fig.suptitle(TITLE)

    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to fit title
    plt.savefig(f"plots/cdf_{HARDWARE}.pdf", format="pdf")


