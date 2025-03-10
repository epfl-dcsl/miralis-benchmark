import matplotlib.pyplot as plt
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

    fig, axes = plt.subplots(2, 1, num=1)  # Create subplots in a single figure
    fig.suptitle("Iozone")  # Overall title

    v = [extract_get, extract_set]

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
        axes[idx].plot(percentile_protect, protect_values, label="Protect payload")
        axes[idx].plot(percentile_offload, offload_values, label="Offload")
        axes[idx].plot(percentile_board, board_values, label="Board")
        axes[idx].set_ylabel("Latency [Milliseconds]")  # Label for the y-axis
        axes[idx].set_xlabel("Percentile")  # Label for the y-axis
        axes[idx].legend()  # Show legend
        axes[idx].set_title("Read Performance")  # Subplot title
        axes[idx].set_xticks(percentile_board)  # Set x-ticks
        axes[idx].set_ylim(0,50)

        idx += 1

    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to fit title
    plt.show()


