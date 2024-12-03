import matplotlib.pyplot as plt
import pandas as pd
import re
from pathlib import Path
import numpy as np
import io

# Function to parse Iozone output
def parse_iozone_output(file_path):
    # Read the content of the file
    with open(file_path, "r") as file:
        text = file.read()

    # Extract the relevant lines for the first table
    lines = text.splitlines()
    start = lines.index("| Workload Name            | MultiCore (iter/s) | SingleCore (iter/s) | Scaling |")
    end = next(i for i, line in enumerate(lines[start + 1:], start=start + 1) if not line.strip().startswith("|"))

    # Join lines of the first table and convert to a DataFrame
    table_text = "\n".join(lines[start:end])
    df = pd.read_csv(io.StringIO(table_text), sep="|", skipinitialspace=True).drop(columns=["Unnamed: 0", "Unnamed: 5"])
    # Drop the first ------- row
    df = df.iloc[1:].reset_index(drop=True)
    df.columns = df.columns.str.strip()
    return df


if __name__ == "__main__":
    values = []
    names = []
    folder_path = Path("results/coremarkpro")

    for file_path in folder_path.rglob('*'):  # Recursively search all files
        if file_path.is_file():
            file_path = str(file_path)
            df = parse_iozone_output(file_path)
            print(file_path.split('/')[2])
            names.append(file_path.split('/')[2])

            
            values.append(df.set_index("Workload Name")["MultiCore (iter/s)"].astype(float))

    width = 0.25 
    multiplier = 0
    indices = np.array(values[0].index)

    x = np.arange(len(indices))
    fig, ax = plt.subplots(layout='constrained')

    for i in range(len(values)):
        offset = width * multiplier
        rec = ax.bar(x + offset, values[i].values,width,  label = names[i])
        multiplier += 1
    print(x + width)
    ax.set_xticks(x + width / 2, indices)

    ax.set_title('Coremarkpro microbenchmark - [iterations/s] - multicore')
    ax.legend(loc='upper left', ncols=len(indices))

    plt.show()
