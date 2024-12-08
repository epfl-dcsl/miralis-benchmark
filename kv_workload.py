import re

def parse_latency_data(filename):
    # Define the regex patterns for reading latency data
    read_pattern = r"\[READ\], AverageLatency\(us\), (\d+\.\d+).*95thPercentileLatency\(us\), (\d+).*99thPercentileLatency\(us\), (\d+)"
    update_pattern = r"\[UPDATE\], AverageLatency\(us\), (\d+\.\d+).*95thPercentileLatency\(us\), (\d+).*99thPercentileLatency\(us\), (\d+)"

    # Initialize the data to store results
    latencies = {'READ': {}, 'UPDATE': {}}

    # Open the text file for reading
    with open(filename, 'r') as file:
        content = file.read()

        # Search for read data
        read_match = re.search(read_pattern, content, re.DOTALL)
        if read_match:
            latencies['READ']['AverageLatency'] = float(read_match.group(1))
            latencies['READ']['95thPercentileLatency'] = int(read_match.group(2))
            latencies['READ']['99thPercentileLatency'] = int(read_match.group(3))

        # Search for update data
        update_match = re.search(update_pattern, content, re.DOTALL)
        if update_match:
            latencies['UPDATE']['AverageLatency'] = float(update_match.group(1))
            latencies['UPDATE']['95thPercentileLatency'] = int(update_match.group(2))
            latencies['UPDATE']['99thPercentileLatency'] = int(update_match.group(3))

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
