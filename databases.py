import re
from plot import *
import os

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

def parse_workloads(name):
    folder_path = "results"
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files = [f for f in files if f.startswith(name)]
    files = [f.split('_')[1] for f in files]
    files = [f for f in files if "txt" not in f]
    files = [f for f in files if "compilation" not in f]
    return list(set(files))



### MySQL workload ###

values  = ['mean', 'p95']
workloads = parse_workloads("mysql")

data = [parse_latency_data_sysbench(f"results/mysql_{e}.txt") for e in workloads]

generate_plot(data, workloads, values, "MySQL benchmark with Sysbench", "mysql_workload")


### KV workload ###

values = ['overall throughput', 'read mean', 'read p95', 'read p99', 'write mean', ' write p95', 'write p99']

workloads = parse_workloads("redis")

print(workloads)
data = [parse_latency_data_ycsb(f"results/workload_redis_{e}.txt") for e in workloads]
generate_plot(data, workloads, values, "Redis benchmark with YCSB", "redis_kv_workload")

workloads = parse_workloads("memcached")
data = [parse_latency_data_ycsb(f"results/workload_memcached_{e}.txt") for e in workloads]
generate_plot(data, workloads, values, "Memcached benchmark with YCSB", "memcached_kv_workload")