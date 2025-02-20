import re
from plot import *
import matplotlib.pyplot as plt
import pandas as pd
import re
from pathlib import Path
import numpy as np
from plot import *

def parse_latency_data_ycsb(filename):
    # Initialize the data to store results
    latencies = []

    # Open the text file for reading
    with open(filename, 'r') as file:
        content = file.readlines()

        # Iterate through each line in the file
        for line in content:
            if line.startswith("[OVERALL]"):
                if "Throughput(ops/sec)" in line:
                    latencies.append(float(line.split(',')[2].strip()))

            elif line.startswith("[READ]"):
                if "AverageLatency(us)" in line:
                    latencies.append(float(line.split(',')[2].strip()))
                if "95thPercentileLatency(us)" in line:
                    latencies.append(int(line.split(',')[2].strip()))
                if "99thPercentileLatency(us)" in line:
                    latencies.append(int(line.split(',')[2].strip()))

            elif line.startswith("[UPDATE]"):
                if "AverageLatency(us)" in line:
                    latencies.append(float(line.split(',')[2].strip()))
                if "95thPercentileLatency(us)" in line:
                    latencies.append(int(line.split(',')[2].strip()))
                if "99thPercentileLatency(us)" in line:
                    latencies.append(int(line.split(',')[2].strip()))

    return latencies

def parse_latency_data_sysbench(filename):

    # Read the file
    with open(filename, "r") as file:
        content = file.read()

    # Extract latencies from the output
    average_latency = re.search(r"avg:\s+([\d.]+)", content)
    percentile_95_latency = re.search(r"95th percentile:\s+([\d.]+)", content)

    # Convert extracted values to floats
    average_latency = float(average_latency.group(1)) if average_latency else None
    percentile_95_latency = float(percentile_95_latency.group(1)) if percentile_95_latency else None

    # Return the results
    return [average_latency, percentile_95_latency]

def extract_and_plot(key, extractor, values, title, filename):
    data = []
    workloads = []
    iteration = []
    folder_path = Path("results")

    for file_path in sorted(folder_path.rglob('*')):
        # Recursively search all files
        if is_workload(file_path, key) and extract_iteration(file_path) == 0:
            workloads.append(extract_workload(file_path))
            iteration.append(extract_iteration(file_path))
            print(key)
            print(extractor(file_path))
            data.append(extractor(file_path))


    generate_plot(data, workloads, values, title, filename)

if __name__ == "__main__":
    ### MySQL workload ###
    extract_and_plot("mysql", parse_latency_data_sysbench, ['mean', 'p95'], "MySQL benchmark with Sysbench", "mysql_workload")


    ### KV workloads ###
    values = ['overall throughput', 'read mean', 'read p95', 'read p99', 'write mean', ' write p95', 'write p99']
    extract_and_plot("redis-kv", parse_latency_data_ycsb, values, "Redis benchmark with YCSB",
                     "redis_kv_workload")

    extract_and_plot("memcached-kv", parse_latency_data_ycsb, values, "Memcached benchmark with YCSB",
                     "memcached_kv_workload")
