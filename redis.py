import matplotlib.pyplot as plt
from plot import *
import os

def extract_values():
    values = []
    for file_path in os.listdir("results"):
        if file_path.startswith("redis-compilation"):
            values.append(file_path.split('_')[1].split('.')[0])

    return list(set(values))

workloads = extract_values()
values = [parse_times(f"results/redis_compilation_{w}.txt") for w in workloads]
labels = ["real", "user", "sys"]

generate_plot(values, workloads, labels, "Redis compilation time in seconds using -j($ncores)", "redis_compilation")
