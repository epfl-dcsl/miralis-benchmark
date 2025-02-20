import matplotlib.pyplot as plt
from plot import *
import os
import matplotlib.pyplot as plt
import pandas as pd
import re
from pathlib import Path
import numpy as np
from plot import *


if __name__ == "__main__":
    title = 'Redis compilation multicore, in seconds'

    values = ["real", "user", "sys"]

    extract_and_plot("redis-compilation", parse_times, values, title)

    title = 'Linux kernel compilation multicore, in seconds'

    extract_and_plot("linux-compilation", parse_times, values, title)



