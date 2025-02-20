import matplotlib.pyplot as plt
import pandas as pd
import re
from pathlib import Path
import numpy as np
from plot import *

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

    headers = header_line.split()[:-4] # Ignore 'fwrite', 'frewrite', 'fread', 'freread' 
    data = []
    for line in data_lines:
        data.append([float(val) for val in line.split()])

    df = pd.DataFrame(data, columns=headers)

    df.columns.values[6] = "random read"
    df.columns.values[7] = "random write"
    df.columns.values[8] = "bkwd read"
    df.columns.values[9] = "record rewrite"
    df.columns.values[10] = "stride read"

    # Useless columns
    df = df.drop(['kB', 'reclen'], axis=1)

    # Calculate the mean for each column
    return df.mean().values


if __name__ == "__main__":
    indices = ['write' ,'rewrite', 'read' ,'reread' ,'random read', 'random write', 'bkwd read', 'record rewrite', 'stride read']

    title = 'IOzone throughput in [KB/s]'

    extract_and_plot("iozone", parse_iozone_output, indices, title)
