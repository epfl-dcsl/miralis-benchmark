import matplotlib.pyplot as plt
from plot import *
import os
import matplotlib.pyplot as plt
import pandas as pd
import re
from pathlib import Path
import numpy as np
from plot import *


if __name__ == "__main__":
    values = []
    names = []
    iteration = []
    folder_path = Path("results")

    workloads = []

    for file_path in sorted(folder_path.rglob('*')):
        # Recursively search all files
        if is_workload(file_path, "redis-compilation") and extract_iteration(file_path) == 0:
            value = parse_times(file_path)
            values.append(value)
            workloads.append(extract_workload(file_path))
            iteration.append(extract_iteration(file_path))

    title = 'Redis compilation multicore, in seconds'

    labels = ["real", "user", "sys"]

    generate_plot(values, workloads, labels, title, "redis_compilation")

    values = []
    names = []
    iteration = []
    folder_path = Path("results")

    workloads = []

    for file_path in sorted(folder_path.rglob('*')):
        # Recursively search all files
        if is_workload(file_path, "linux-compilation") and extract_iteration(file_path) == 0:
            value = parse_times(file_path)
            values.append(value)
            workloads.append(extract_workload(file_path))
            iteration.append(extract_iteration(file_path))

    title = 'Linux kernel compilation multicore, in seconds'


    generate_plot(values, workloads, labels, title, "linux_compilation")


