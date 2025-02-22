import matplotlib.pyplot as plt
import pandas as pd
import re
from pathlib import Path
import numpy as np
import io
from plot import *

def extract_iterations_per_second(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return float(lines[7].split('=')[1])

def extract_iterations_per_second_jpeg(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return float(lines[7+21].split('=')[1])

if __name__ == "__main__":

    title = 'Coremarkpro - [iterations/s] - multicore'

    extract_and_plot("coremarkpro-core", extract_iterations_per_second, ["single entry"], title)
    extract_and_plot("coremarkpro-fft", extract_iterations_per_second, ["single entry"], title)
    extract_and_plot("coremarkpro-gaussian", extract_iterations_per_second, ["single entry"], title)
    extract_and_plot("coremarkpro-jpeg", extract_iterations_per_second_jpeg, ["single entry"], title)
    extract_and_plot("coremarkpro-livermore", extract_iterations_per_second, ["single entry"], title)
    extract_and_plot("coremarkpro-neuralnetwork", extract_iterations_per_second, ["single entry"], title)
    extract_and_plot("coremarkpro-sha", extract_iterations_per_second, ["single entry"], title)
    extract_and_plot("coremarkpro-xml", extract_iterations_per_second, ["single entry"], title)
    extract_and_plot("coremarkpro-zip", extract_iterations_per_second, ["single entry"], title)
