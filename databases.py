import re
from plot import *

def parse_latency_data_ycsb(filename):
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
    # print(f"Average Latency: {average_latency} ms")
    # print(f"95th Percentile Latency: {percentile_95_latency} ms")


workloads = ['board', 'miralis', 'protect_payload']

### MySQL workload ###

values  = ['mean', 'p95']

data = [parse_latency_data_sysbench("results/mysql_board.txt"),parse_latency_data_sysbench("results/mysql_miralis.txt"),parse_latency_data_sysbench("results/mysql_protect.txt")]
generate_plot(data, workloads, values, "MySQL benchmark with Sysbench", "mysql_workload")


### KV workload ###

values = ['read mean', 'read p95', 'read p99', 'write mean', ' write p95', 'write p99']

data = [parse_latency_data_ycsb('results/workload_redis_board.txt'), parse_latency_data_ycsb('results/workload_redis_miralis.txt'), parse_latency_data_ycsb('results/workload_redis_protect.txt')]
generate_plot(data, workloads, values, "Redis benchmark with YCSB", "redis_kv_workload")

data = [parse_latency_data_ycsb('results/workload_memcached_board.txt'), parse_latency_data_ycsb('results/workload_memcached_miralis.txt'), parse_latency_data_ycsb('results/workload_redis_protect.txt')]
generate_plot(data, workloads, values, "Memcached benchmark with YCSB", "memcached_kv_workload")