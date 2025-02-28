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
            if line.startswith("[READ]"):
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

def parse_latency_data_ycsb_tp(filename):
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

if __name__ == "__main__":
    ### MySQL workload ###
    extract_and_plot("mysql", parse_latency_data_sysbench, ['mean', 'p95'], "MySQL benchmark with Sysbench")

    ### KV workloads ###
    values = ['read mean', 'read p95', 'read p99', 'write mean', ' write p95', 'write p99']
    extract_and_plot("redis-kv", parse_latency_data_ycsb, values, "Redis YCSB - [microseconds]")
    extract_and_plot("memcached-kv", parse_latency_data_ycsb, values, "Memcached YCSB - [microseconds]")

    values = ['overall throughput'] 
    extract_and_plot("redis-kv", parse_latency_data_ycsb_tp, values, "Redis YCSB - [op/s]", "redis-kv-tp")
    extract_and_plot("memcached-kv", parse_latency_data_ycsb_tp, values, "Memcached YCSB - [op/s]", "memcached-kv-tp")
