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


    headers = header_line.split()[:6] # Ignore 'fwrite', 'frewrite', 'fread', 'freread' 
    data = []
    for line in data_lines:
        data.append([float(val) for val in line.split()])

    df = pd.DataFrame(data, columns=headers)


    df = df[df['reclen'] == 128.0][['kB', 'write', 'read']]

    return df

if __name__ == "__main__":
    indices = ['write' ,'rewrite', 'read' ,'reread' ,'random read', 'random write', 'bkwd read', 'record rewrite', 'stride read']

    title = 'IOzone throughput in [KB/s]'

    values = extract("iozone", parse_iozone_output)
    values = list(map(lambda x: x[1], values))

    values_read = np.array(list(map(lambda x: np.array(x['read']), values)))
    values_write = np.array(list(map(lambda x: np.array(x['write']), values)))
    values_len = np.array(list(map(lambda x: np.array(x['kB']), values))[0])
    values_len = list(map(lambda x: str(x),values_len))

    values_read_board = np.mean(values_read[0:25], axis=0).astype(float)
    values_read_offload =  np.mean(values_read[25:50], axis=0).astype(float)
    values_read_protect =  np.mean(values_read[50:75], axis=0).astype(float)

    values_write_board = np.mean(values_write[0:25], axis=0).astype(float)
    values_write_offload =  np.mean(values_write[25:50], axis=0).astype(float)
    values_write_protect =  np.mean(values_write[50:75], axis=0).astype(float)

    fig, axes = plt.subplots(2, 1, num=1)  # Create subplots in a single figure
    fig.suptitle("Iozone")  # Overall title

    # First subplot (Read performance)
    axes[0].plot(values_len, values_read_board, label="Read Board")
    axes[0].plot(values_len, values_read_offload, label="Read Offload")
    axes[0].plot(values_len, values_read_protect, label="Read Protect")
    axes[0].set_ylabel("Read Speed [KB/s]")  # Label for the y-axis
    axes[0].legend()  # Show legend
    axes[0].set_title("Read Performance")  # Subplot title
    axes[0].set_xticks(values_len)  # Set x-ticks
    axes[0].set_ylim(10000,22000)

    # Second subplot (Write performance)
    axes[1].plot(values_len, values_write_board, label="Write Board")
    axes[1].plot(values_len, values_write_offload, label="Write Offload")
    axes[1].plot(values_len, values_write_protect, label="Write Protect")
    axes[1].set_ylabel("Write Speed [KB/s]")  # Label for the y-axis
    axes[1].set_xlabel("Block Size")  # Label for the x-axis
    axes[1].legend()  # Show legend
    axes[1].set_title("Write Performance")  # Subplot title
    axes[1].set_xticks(values_len)  # Set x-ticks
    axes[1].set_ylim(10000,17000)

    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to fit title
    plt.show()

