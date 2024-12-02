import matplotlib.pyplot as plt
import pandas as pd
import re

# Function to parse Iozone output
def parse_iozone_output(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the header line and the data section
    header_line = None
    data_lines = []
    for line in lines:
        if "reclen" in line and header_line is None:
            header_line = line
        elif re.match(r"^\s*\d+", line):
            data_lines.append(line.strip())

    # Parse header and data
    if not header_line or not data_lines:
        raise ValueError("Invalid Iozone output format")

    headers = header_line.split()
    data = []
    for line in data_lines:
        data.append([float(val) for val in line.split()])

    return pd.DataFrame(data, columns=headers)

# Function to plot metrics
def plot_metrics(df,benchmark_name, title, save_path=None):
    plt.figure(figsize=(10, 6))
    for metric in df.columns: 
            plt.plot(df["kB"], df[metric], label="{}_{}".format(benchmark_name, metric))

    plt.title(title)
    plt.xlabel("File Size (kB)")
    plt.ylabel("Throughput (kBytes/sec)")
    plt.legend()
    plt.grid(True)
    if save_path:
        plt.savefig(save_path)
    plt.show()

if __name__ == "__main__":
    file_path = 'miralis_iozone.txt'

    try:
        df = parse_iozone_output(file_path)
        print("Data parsed successfully.")

        name = file_path.split('_')[0]

        print(df)

        # Tmp filter reclen == 4
        df = df[df["reclen"] == 8]

        df.columns.values[6] = "random read"
        df.columns.values[7] = "random write"
        df.columns.values[8] = "bkwd read"
        df.columns.values[9] = "record rewrite"
        df.columns.values[10] = "stride read"

        # Calculate the mean for each column
        average_values = df.mean()

        # Plot the average values as a bar chart
        plt.figure(figsize=(10, 6))
        average_values.plot(kind='bar', color='skyblue')
        plt.title('Average of Each Column')
        plt.xlabel('Column Names')
        plt.ylabel('Average Throuput')
        plt.xticks(rotation=90)  # Rotate the x-axis labels to make them more readable
        plt.tight_layout()
        plt.show()

        exit(0)


        plot_metrics(df,name, "Performance Metrics")
    except Exception as e:
        print(f"Error: {e}")
