import matplotlib.pyplot as plt
from plot import *

# Display redis workloads
values = [parse_times("redis_board.txt"), parse_times("redis_miralis.txt")]
workload = ["Board", "Miralis"]
labels = ["real", "user", "sys"]

generate_plot(values, workload, labels, "Redis compilation")
