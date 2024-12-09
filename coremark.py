import matplotlib.pyplot as plt
import pandas as pd
import re
from pathlib import Path
import numpy as np
import io
from plot import *

def parse_iozone_output(file_path):
    # Read the content of the file
    with open(file_path, "r") as file:
        text = file.read()

    # Extract the WORKLOAD RESULTS TABLE
    workload_start = text.find("WORKLOAD RESULTS TABLE")
    workload_end = text.find("MARK RESULTS TABLE")
    workload_section = text[workload_start+4:workload_end].strip()


    # Process the workload table
    workload_lines = workload_section.splitlines()[5:]

    output = []
    names = []
    for line in workload_lines:
        # Split the string into parts
        parts = line.split()

        names.append(parts[0])

        # Iterate through parts to find the first number
        for part in parts:
            try:
                output.append(float(part))
                break
            except ValueError:
                continue
    
    return np.array(output), names



if __name__ == "__main__":
    values = []
    names = []
    indices = []
    folder_path = Path("results")

    for file_path in folder_path.rglob('*'): 
        if is_workload(file_path, "coremarkpro"):
            file_path = str(file_path)
            print(file_path.split('/')[1])
            names.append(file_path.split('/')[1].split('.')[0].split('_')[1])

            val, index = parse_iozone_output(file_path)
            values.append(val)
            indices = index


    title = 'Coremarkpro microbenchmark - [iterations/s] - multicore'

    generate_plot(values, names, np.array(indices), title, "coremarkpro")