import numpy as np
import matplotlib.pyplot as plt
import os

def is_workload(file_path, name):
    return file_path.is_file() and name in str(file_path)

def generate_plot(values, names, indices, title, filename):
    width = 0.25 
    multiplier = 0

    x = np.arange(len(indices))
    _, ax = plt.subplots(layout='constrained')

    for i in range(len(values)):
        offset = width * multiplier
        rec = ax.bar(x + offset, values[i], width, label=names[i])
        multiplier += 1

    ax.set_xticks(x + width / 2)
    ax.set_xticklabels(indices)

    ax.set_title(title)
    ax.legend(loc='upper left', ncols=len(indices))

    folder = 'plots'
    if not os.path.exists(folder):
        os.makedirs(folder)

    plt.xticks(rotation=45, ha='right')


    plt.savefig(folder + "/" + filename)

    plt.close()
