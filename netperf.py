import matplotlib.pyplot as plt
import pandas as pd
import re
from pathlib import Path
import numpy as np
from plot import *

# Function to parse Iozone output
def extract_number(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if re.match(r'^\d.*', line):
            tmp = line.strip()
            return float(tmp.split(' ')[-1])

if __name__ == "__main__":
    values = []
    names = []
    workload = []
    folder_path = Path("results")

    for file_path in folder_path.rglob('*'):  # Recursively search all files
        if is_workload(file_path, "netperf"):
            file_path = str(file_path)
            df = extract_number(file_path)
            print("Data parsed successfully.")

            name = file_path.split('/')[1]
            names.append(name.split('_')[1])
            values.append(df)
            workload.append(name.split('_')[2])

    dico1 = {}
    dico2 = {}

    for i in range(len(values)):
        if names[i] not in dico1:
            dico1[names[i]] = []
            dico2[names[i]] = []

        dico1[names[i]].append(values[i])
        dico2[names[i]].append(workload[i])


    # TODO: Wip here, this is not working corretly at the moment
    title = 'Netperf microbenchmark - throuput in [KB/s] - currently test running both machines on localhost'

    names = list(dico1.keys())
    values = list(dico1.values())
    indices = list(dico2.values())

    generate_plot(values, names, indices, title, "netperf")    
