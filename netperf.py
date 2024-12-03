import matplotlib.pyplot as plt
import pandas as pd
import re
from pathlib import Path
import numpy as np

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
    folder_path = Path("results/netperf")

    for file_path in folder_path.rglob('*'):  # Recursively search all files
        if file_path.is_file():
            file_path = str(file_path)
            df = extract_number(file_path)
            print("Data parsed successfully.")

            name = file_path.split('/')[2]
            names.append(name.split('_')[0])
            values.append(df)
            workload.append(name.split('_')[1])

    dico1 = {}
    dico2 = {}

    for i in range(len(values)):
        if names[i] not in dico1:
            dico1[names[i]] = []
            dico2[names[i]] = []

        dico1[names[i]].append(values[i])
        dico2[names[i]].append(workload[i])
    

    print(dico1)
    print(dico2)



    size = 2

    width = 0.25 
    multiplier = 0
    indices = np.array(size)

    x = np.arange(2)
    fig, ax = plt.subplots(layout='constrained')

    tmp = ""
    for key in dico1:
        offset = width * multiplier
        rec = ax.bar(x + offset, dico1[key],width,  label = key)
        multiplier += 1
        tmp = dico2[key]

    ax.set_xticks(x + width, tmp)
    ax.set_title('Netperf microbenchmark - throuput in [KB/s] - currently test running both machines on localhost')
    ax.legend(loc='upper left', ncols=2)

    plt.show()
