import matplotlib.pyplot as plt
from plot import *

# Display redis workloads
values = [parse_times("results/redis_compilation_board.txt"), parse_times("result/redis_compilation_miralis.txt")]
workload = ["Board", "Miralis"]
labels = ["real", "user", "sys"]

generate_plot(values, workload, labels, "Redis compilation", "redis_compilation")
