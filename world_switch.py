import numpy as np 
from plot import *

def extract_p_values(line):
    parts = line.split(' ')
    p50 = None
    p95 = None
    p99 = None
    
    for i in range(len(parts)):
        if parts[i] == 'p50:':
            p50 = int(parts[i + 1].rstrip(','))
        elif parts[i] == 'p95:':
            p95 = int(parts[i + 1].rstrip(','))
        elif parts[i] == 'p99:':
            p99 = int(parts[i + 1].rstrip('}'))
    
    return p50, p95, p99

def parse_values(file_path):
    p50_values = []
    p95_values = []
    p99_values = []

    with open(file_path, 'r') as f:
        for line in f:
            result = extract_p_values(line)
            if result:
                p50, p95, p99 = result
                p50_values.append(p50)
                p95_values.append(p95)
                p99_values.append(p99)

    mean_p50 = sum(p50_values) / len(p50_values) 
    mean_p95 = sum(p95_values) / len(p95_values)
    mean_p99 = sum(p99_values) / len(p99_values)

    return [mean_p50, mean_p95, mean_p99]

workloads = ['miralis']
values = ['switch p50','switch p95', 'switch p99']

file_path = 'results/switch_firmware.txt'
generate_plot([parse_values(file_path=file_path)], workloads, values, "Firmware <--> Miralis cost [CPU cycles]", "world_switch_firmware")

file_path = 'results/switch_payload.txt'
generate_plot([parse_values(file_path=file_path)], workloads, values, "Payload <--> Firmware cost [CPU cycles]", "world_switch_payload")