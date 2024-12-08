import re
from plot import *

def parse_latency_data(filename):
    # Initialize the data to store results
    latencies = []

    # Open the text file for reading
    with open(filename, 'r') as file:
        content = file.readlines()

        # Iterate through each line in the file
        for line in content:
            # Check if the line starts with "READ" and contains "AverageLatency" for reading latency data
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



data = [parse_latency_data('results/workload_redis_board.txt'), parse_latency_data('results/workload_redis_miralis.txt')]
workloads = ['board', 'miralis']
values = ['read mean', 'read p95', 'read p99', 'write mean', ' write p95', 'write p99']


generate_plot(data, workloads, values, "Redis benchmark YCSB")