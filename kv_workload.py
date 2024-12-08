import re

def parse_latency_data(filename):
    # Initialize the data to store results
    latencies = {'READ': {}, 'UPDATE': {}}

    # Open the text file for reading
    with open(filename, 'r') as file:
        content = file.readlines()

        # Iterate through each line in the file
        for line in content:
            # Check if the line starts with "READ" and contains "AverageLatency" for reading latency data
            if line.startswith("[READ]"):
                
                if "AverageLatency(us)" in line:
                    latencies['READ']['AverageLatency'] = float(line.split(',')[2].strip())

                if "95thPercentileLatency(us)" in line:
                    latencies['READ']['95thPercentileLatency'] = int(line.split(',')[2].strip())

                if "99thPercentileLatency(us)" in line:
                    latencies['READ']['99thPercentileLatency'] = int(line.split(',')[2].strip())

            elif line.startswith("[UPDATE]"):
                if "AverageLatency(us)" in line:
                    latencies['UPDATE']['AverageLatency'] = float(line.split(',')[2].strip())
                if "95thPercentileLatency(us)" in line:
                    latencies['UPDATE']['95thPercentileLatency'] = int(line.split(',')[2].strip())
                if "99thPercentileLatency(us)" in line:
                    latencies['UPDATE']['99thPercentileLatency'] = int(line.split(',')[2].strip())

    return latencies


# Example usage
filename = 'workload_redis_board.txt'  # Correct file name
latencies = parse_latency_data(filename)

print(type(latencies))
print(latencies)

# Print the results
for operation in ['READ', 'UPDATE']:
    print(f"{operation} Latencies:")
    print(f"  Average Latency (us): {latencies[operation]['AverageLatency']}")
    print(f"  95th Percentile Latency (us): {latencies[operation]['95thPercentileLatency']}")
    print(f"  99th Percentile Latency (us): {latencies[operation]['99thPercentileLatency']}")
