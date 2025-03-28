import re
import os 
from functools import reduce
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.ticker as mticker

class Entry:
    def __init__(self,delta, world_switches, read_time, set_timer, misaligned_op, ipi, remote_fence, firmware_exits):
        self.delta = delta
        self.world_switches = world_switches
        self.read_time = read_time
        self.set_timer = set_timer
        self.misaligned_op = misaligned_op
        self.ipi = ipi
        self.remote_fence = remote_fence
        self.firmware_exits = firmware_exits

    def stacked(self):
        v1 = ['no-offload', 'read-time', 'set-timer', 'misaligned-op', 'ipi', 'remote-fence']

        v2 = [self.world_switches_sec()]
        v2 = v2 + [self.read_time_sec()]
        v2 = v2 + [self.set_timer_sec()]
        v2 = v2 + [self.misaligned_op_sec()]
        v2 = v2 + [self.ipi_sec()]
        v2 = v2 + [self.remote_fence_sec()]
    
        return v2
    def __add__(self, other):
        return Entry(
            1, # 1 second
            self.world_switches_sec() + other.world_switches_sec(),
            self.read_time_sec() + other.read_time_sec(),
            self.set_timer_sec() + other.set_timer_sec(),
            self.misaligned_op_sec() + other.misaligned_op_sec(),
            self.ipi_sec() + other.ipi_sec(),
            self.remote_fence_sec() + other.remote_fence_sec() ,
            self.firmware_trap_sec() + other.firmware_trap_sec()
        )
    
    def normalize(self, size):
        self.world_switches = self.world_switches_sec() / size
        self.read_time = self.read_time_sec() / size
        self.set_timer = self.set_timer_sec() / size
        self.misaligned_op = self.misaligned_op_sec() / size
        self.ipi = self.ipi_sec() / size
        self.remote_fence = self.remote_fence_sec() / size
        self.firmware_exits = self.firmware_trap_sec() / size    
    
    def firmware_trap_sec(self):
        return self.firmware_exits / self.delta
    
    def world_switches_sec(self):
        return  self.world_switches / self.delta

    def read_time_sec(self):
        return self.read_time / self.delta

    def set_timer_sec(self): 
        return self.set_timer / self.delta

    def misaligned_op_sec(self):
        return self.misaligned_op / self.delta

    def ipi_sec(self):
        return self.ipi / self.delta

    def remote_fence_sec(self):
        return self.remote_fence / self.delta
    
    def total_exceptions(self):
        return (self.world_switches + self.read_time + self.set_timer + self.misaligned_op + self.ipi + self.remote_fence) / self.delta


def parse_line(line):
    line = line.replace(" ", "")
    line = line.split('[')[1:]

    time = int(line[0].split(':')[1])

    line = line[1:]
    line = list(map(lambda x: x.replace("]", "").replace("&", ""), line))
    line = list(map(lambda x: x.split('|'), line))
    line = ([list(map(int, x)) for x in line])

    output = []
    for i in range(len(line[0])):
        acc = 0
        for j in range(len(line)):
            acc += line[j][i]
        output.append(acc)

    return [time] + output

def compute_deltas(file_path):
    values = []
    """Computes deltas between consecutive lines in the log file."""
    with open(file_path, 'r') as file:
        previous_line = None
        for line in file:
            line = line.strip()
            if not line or line == "":
                continue

            current_line = parse_line(line)
            if not current_line:
                continue

            if previous_line:
                v1 = (current_line[0] - previous_line[0]) / 1000000000
                v2 = current_line[1] - previous_line[1]
                v3 = current_line[2] - previous_line[2]
                v4 = current_line[3] - previous_line[3]
                v5 = current_line[4] - previous_line[4]
                v6 = current_line[5] - previous_line[5]
                v7 = current_line[6] - previous_line[6]
                v8 = current_line[7] - previous_line[7]

                values.append(Entry(v1, v2,v3,v4,v5,v6,v7, v8))

            previous_line = current_line

    return values





def plot_ratio_traps(all_values):

    all_values = list(map(lambda x: x.stacked(), all_values))


    columns = ['no-offload', 'read-time', 'set-timer', 'misaligned-op', 'ipi', 'remote-fence']

    # Create DataFrame
    csv = pd.DataFrame(all_values, columns=columns)

    csv = csv.sort_values(by='read-time')
    data = {}
    for col in csv.columns:
        data[col] = np.array(csv[col])
        unit_of_time = np.arange(0, len(data[col]), 1)


    fig, ax = plt.subplots()
    ax.stackplot(unit_of_time, data.values(),
                labels=['no-offload', 'read-time', 'set-timer', 'misaligned-op', 'ipi', 'remote-fence'], alpha=0.8)
    ax.legend(loc='upper left', reverse=True)
    ax.set_title('Proportion of exceptions per category', fontsize=16)
    ax.set_ylabel('Total number of Exceptions', fontsize=15)

    # Place legend outside the plot
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

    # Adjust layout to make space for the legend
    plt.tight_layout()

    plt.savefig("plots/distribution_interrupts")

    csv = csv.apply(lambda row: row / row.sum() if row.sum() > 0 else row, axis=1)

    data = {}
    for col in csv.columns:
        data[col] = np.array(csv[col])
        unit_of_time = np.arange(0, len(data[col]), 1)

    fig, ax = plt.subplots()
    ax.stackplot(unit_of_time, data.values(),
                labels=['no-offload', 'read-time', 'set-timer', 'misaligned-op', 'ipi', 'remote-fence'], alpha=0.8)
    ax.legend(loc='upper left', reverse=True)
    ax.set_title('Percentage of exceptions by category', fontsize=16)
    ax.set_ylabel('Cumulative percentage', fontsize=15)

    # Place legend outside the plot
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

    # Adjust layout to make space for the legend
    plt.tight_layout()

    plt.savefig("plots/distribution_interrupts_proportion")


def plot_traps_and_roofline(deltas, names):

    deltas = list(map(lambda x: x.total_exceptions(), deltas))
    # Sort values and categories together
    sorted_data = sorted(zip(deltas, names), reverse=True)  # Sort descending
    deltas, names = zip(*sorted_data)

    pairs = []
    for i in range(len(names)):
        with open("overhead.txt", "r") as file:
            for line in file:
                name, value = line.split(':')
                if name == names[i]:
                    pairs.append((float(value), deltas[i]))

    x,y = zip(*pairs)

    # Create scatter plot
    sns.scatterplot(x=x, y=y, color='blue', marker='o')

    # Labels and title
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Seaborn Scatter Plot")

    model = LinearRegression()

    # Fit the model
    model.fit(np.array(x).reshape(-1,1), y)

    z = np.arange(0.98,4,0.05)
    plt.plot(z,z*model.coef_[0] + model.intercept_)


    # Show plot
    plt.savefig("plots/roofline")

    # Create the plot
    plt.figure(figsize=(12, 6))
    sns.barplot(x=deltas, y=names, palette="viridis")

    plt.tick_params(axis='both', labelsize=15)

    # Labels and title
    plt.title("Number of exceptions per second in Miralis", fontsize=16)

    plt.tight_layout()

    plt.savefig("plots/distribution")



if __name__ == "__main__":

    for file_name in sorted(os.listdir("results/stats")):
        continue
        file_path = os.path.join("results/stats", file_name) 
        if os.path.isfile(file_path) and "stats" in file_path and "board" not in file_path  and "offload" in file_path:
            if "stats_linux" in file_path:
                continue
            workload_name = file_path.split('/')[2].split("_")[0:2]
            for value in compute_deltas(file_path):
                print(f"Current workload: {workload_name} | Duration: {value.delta} | {value.firmware_trap_sec():.2f} World switches: {value.world_switches_sec():.2f},Read time: {value.read_time_sec():.2f}, Set timer: {value.set_timer_sec():.2f}, Misaligned op: {value.misaligned_op_sec():.2f}, IPI: {value.ipi_sec():.2f}, Fences: {value.remote_fence_sec():.2f}")

    deltas = []
    names = []
    for file_path in sorted(Path("results/stats").rglob('*')):
        if "_0" in str(file_path) and "offload" in str(file_path):
            entries = []
            names.append(str(file_path).split('/')[2].split("_")[0])
            for i in range(0,5):
                path = str(file_path).replace("0", str(i))
                entries.append(compute_deltas(path)[0])
            
            deltas.append(reduce(lambda x,y: x + y, entries))

    for d in deltas:
        d.normalize(5)


    all_values = deltas
    plot_traps_and_roofline(deltas, names)
    plot_ratio_traps(all_values)
