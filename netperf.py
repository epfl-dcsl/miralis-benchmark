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

    print("adapt script to new naming convention")
    exit(1)

    for file_path in folder_path.rglob('*'):  # Recursively search all files
        if is_workload(file_path, "netperf"):
            file_path = str(file_path)
            df = extract_number(file_path)
            name = file_path.split('/')[1]
            names.append(name.split('_')[1])
            values.append(df)
            workload.append(name.split('_')[2].split('.')[0])

    dico = {}


    for i in range(len(values)):
        if names[i] not in dico:
            dico[names[i]] = []

        dico[names[i]].append((values[i], workload[i]))

    
    for key in dico.keys():
        dico[key] = sorted(dico[key])

    title = 'Netperf microbenchmark - throuput in [KB/s] - currently test running both machines on localhost'

    names = []
    values = []
    for key in dico.keys():
        names.append(key)
        list1, list2 = zip(*dico[key])
        values.append(list(list1))
        indices = list(list2)



    generate_plot(values, names, indices, title, "netperf")    
