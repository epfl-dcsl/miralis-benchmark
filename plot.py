import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path

# source myenv/bin/activate

import numpy as np
import matplotlib.pyplot as plt

colors = {
    'Board': (0.12156862745098039, 0.4666666666666667, 0.7058823529411765), 
    'Offload': (1.0, 0.4980392156862745, 0.054901960784313725), 
    'Protect': (0.17254901960784313, 0.6274509803921569, 0.17254901960784313),
    'Keystone':  (0.8392156862745098, 0.15294117647058825, 0.1568627450980392),
}

def plot_bar(title, x_ticks, data, y_label):
    x = np.arange(len(x_ticks))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for i, (attribute, measurement) in enumerate(data.items()):
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute, color=colors[attribute])
        multiplier += 1

    # Add labels, title, and legend
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.set_xticks(x + width, x_ticks)
    ax.legend(loc='upper right', ncols=3)
    ax.set_ylim(0, 1.3)

    plt.show()


def extract_workload(file_path):
    return str(file_path).split('/')[-1].split('_')[1]

def extract_iteration(file_path):
    return int(str(file_path).split('/')[-1].split('_')[2].split('.')[0])

def is_workload(file_path, name):
    return str(file_path).split('/')[-1].startswith(f"{name}_") and "stats" not in str(file_path)

def extract(key, extractor, path="results"):
    folder_path = Path(path)

    output = []

    for file_path in sorted(folder_path.rglob('*')):
        # Recursively search all files
        if is_workload(file_path, key):
            output.append((extract_workload(file_path),extractor(file_path)))

    return output
