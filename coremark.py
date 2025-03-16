import matplotlib.pyplot as plt
import pandas as pd
import re
from pathlib import Path
import numpy as np
import io
from plot import *
import csv

def extract_iterations_per_second(file_path):
    extensions = ["core", "fft", "gaussian", "jpeg", "livermore", "neuralnetwork", "sha", "xml", "zip"]

    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [float(lines[7].split('=')[1])]

def extract_iterations_per_second_jpeg(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [float(lines[7+21].split('=')[1])]

if __name__ == "__main__":
    title = 'Coremarkpro - [iterations/s] - multicore'

    workloads = ["core", "gaussian","jpeg", "livermore", "neuralnetwork", "sha", "xml", "zip"]
    output = []
    for w in workloads:
        if w == "jpeg":
            output.append(extract(f"coremarkpro-{w}", extract_iterations_per_second_jpeg))
        else:
            output.append(extract(f"coremarkpro-{w}", extract_iterations_per_second))

    values = []
    for i in range(len(workloads)):
        current = list(map(lambda x: x[1][0], output[i]))
        values.append(np.array(current))

    values = np.array(values).T

    normal = np.mean(values[0:5], axis=0)

    native = list(map(lambda x: "{:.1f} it/s".format(x) if x > 10 else "{:.2f} it/s".format(x) , normal))


    board = np.mean(values[0:5], axis=0) / normal
    offload = np.mean(values[5:10], axis=0) / normal
    protect = np.mean(values[10:15], axis=0) / normal

    workloads[4] = 'nn'

    print("Offload: ", np.sort(offload))
    print("Protect: ", np.sort(protect))

    plot_bar(workloads, {
        'Board': board,
        'Offload': offload,
        'Protect': protect,
    }, 'coremark', native, 1.03, 1.1)