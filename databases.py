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

def extract_kv_workloads(typ):
    values = []
    for file_path in os.listdir("results"):
        if file_path.startswith(f"workload_{typ}"):
            values.append(file_path.split('_')[2].split('.')[0])



    return list(set(values))

def extract_mysql_workloads(): 
    values = []
    for file_path in os.listdir("results"):
        if file_path.startswith(f"mysql_"):
            values.append(file_path.split('_')[1].split('.')[0])

    return list(set(values))


print("adapt script to new naming convention")
exit(1)

if __name__ == "__main__":
    workloads = ['board', 'miralis', 'protect_payload']

    ### MySQL workload ###

    values  = ['mean', 'p95']

    data = [parse_latency_data_ycsb(f"results/mysqsl_{w}.txt") for w in extract_mysql_workloads()]
    generate_plot(data, workloads, values, "MySQL benchmark with Sysbench", "mysql_workload")


    ### KV workload ###

    values = ['overall throughput', 'read mean', 'read p95', 'read p99', 'write mean', ' write p95', 'write p99']

    data = [parse_latency_data_ycsb(f"results/workload_redis_{w}.txt") for w in extract_kv_workloads("redis")]
    generate_plot(data, workloads, values, "Redis benchmark with YCSB", "redis_kv_workload")

    data = [parse_latency_data_ycsb(f"results/workload_redis_{w}.txt") for w in extract_kv_workloads("memcached")]
    generate_plot(data, workloads, values, "Memcached benchmark with YCSB", "memcached_kv_workload")