import re
import os 

class Entry:
    def __init__(self,delta, firmware_exits, world_switches):
        self.delta = delta
        self.firmware_exits = firmware_exits
        self.world_switches = world_switches

    def firmware_trap_second(self):
        return self.firmware_exits / self.delta
    
    def world_switches_second(self):
        return  self.world_switches / self.delta

def parse_line(line):
    while len(line) > 0 and line[0] != 'T':
        line = line[1:]
    """Parses a line and extracts timestamp, firmware exits, and world switches."""
    pattern = r"Timestamp: (\d+) \| Firmware exits: (\d+)  \| World switches: (\d+)"
    match = re.match(pattern, line)
    if match:
        timestamp = int(match.group(1))
        firmware_exits = int(match.group(2))
        world_switches = int(match.group(3))
        return timestamp, firmware_exits, world_switches
    return None

def compute_deltas(file_path):
    values = []
    """Computes deltas between consecutive lines in the log file."""
    with open(file_path, 'r') as file:
        previous_line = None
        for line in file:
            line = line.strip()
            if not line:
                continue

            current_line = parse_line(line)
            if not current_line:
                continue

            if previous_line:
                timestamp_delta = (current_line[0] - previous_line[0]) / 1000000000
                firmware_exits_delta = current_line[1] - previous_line[1]
                world_switches_delta = current_line[2] - previous_line[2]

                values.append(Entry(timestamp_delta, firmware_exits_delta, world_switches_delta))

            previous_line = current_line

    return values

NB_CYCLES = 1_500_000_000
COST_FIRMWARE_TRAP = 300
COST_WORLD_SWITCH = 2000

if __name__ == "__main__":

    print("Adapt this script to the new naming convention")

    exit(1)

    for file_name in os.listdir("results"):
        file_path = os.path.join("results", file_name)
        if os.path.isfile(file_path) and "stats" in file_path:
            if "stats_linux" in file_path:
                continue
            workload_name = file_path.split('.')[0].split('/')[1]
            for value in compute_deltas(file_path):
                percentage = (value.firmware_trap_second() * COST_FIRMWARE_TRAP + value.world_switches_second() * COST_WORLD_SWITCH) / NB_CYCLES * 100
                print(f"Current workload: {workload_name} | Duration in second: {value.delta} | Firmware traps per second: {value.firmware_trap_second():.2f} | World switches per second: {value.world_switches_second():.2f} | Estimated overhead percentage: {percentage:.2f}") 