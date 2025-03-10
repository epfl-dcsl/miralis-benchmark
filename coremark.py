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
 
    board = np.mean(values[0:5], axis=0) / normal
    offload = np.mean(values[5:10], axis=0) / normal
    protect = np.mean(values[10:15], axis=0) / normal

    plot_bar("Coremark pro", workloads, {
        'Board': board,
        'Offload': offload,
        'Protect': protect,
    }, 'Relative speedup')