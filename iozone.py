import matplotlib.pyplot as plt
import pandas as pd
import re
from pathlib import Path
import numpy as np

# Function to parse Iozone output
def parse_iozone_output(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the header line and the data section
    header_line = None
    data_lines = []
    for line in lines:
        if "reclen" in line and header_line is None:
            header_line = line
        elif re.match(r"^\s*\d+", line):
            data_lines.append(line.strip())

    # Parse header and data
    if not header_line or not data_lines:
        raise ValueError("Invalid Iozone output format")

    headers = header_line.split()
    data = []
    for line in data_lines:
        data.append([float(val) for val in line.split()])

    return pd.DataFrame(data, columns=headers)

def process_values(df, name):
        df.columns.values[6] = "random read"
        df.columns.values[7] = "random write"
        df.columns.values[8] = "bkwd read"
        df.columns.values[9] = "record rewrite"
        df.columns.values[10] = "stride read"

        # Useless columns
        df = df.drop(['kB', 'reclen'], axis=1)

        # Calculate the mean for each column
        return df.mean()

if __name__ == "__main__":
    values = []
    names = []
    folder_path = Path("results")

    for file_path in folder_path.rglob('*'):  # Recursively search all files
        if file_path.is_file():
            file_path = str(file_path)
            df = parse_iozone_output(file_path)
            print("Data parsed successfully.")

            name = file_path.split('_')[0]
            name = name.split('/')[1]

            names.append(name)
            values.append(process_values(df, name))

    width = 0.25 
    multiplier = 0
    indices = np.array(values[0].index)

    x = np.arange(len(indices))
    fig, ax = plt.subplots(layout='constrained')

    for i in range(len(values)):
        offset = width * multiplier
        rec = ax.bar(x + offset, values[i].values,width,  label = names[i])
        multiplier += 1

    ax.set_xticks(x + width / 2, indices)

    ax.set_title('IOzone microbenchmark - throuput in [KB/s] (averaged by r/w size from 64kb to 512mb)')
    ax.legend(loc='upper left', ncols=len(indices))

    plt.show()