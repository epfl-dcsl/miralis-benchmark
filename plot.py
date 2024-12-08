import numpy as np
import matplotlib.pyplot as plt

# source myenv/bin/activate 

def generate_plot(values, names, indices,title):
    print(values)
    print(names)
    print(indices)
    width = 0.25 
    multiplier = 0

    x = np.arange(len(indices))
    _, ax = plt.subplots(layout='constrained')

    for i in range(len(values)):
        offset = width * multiplier
        rec = ax.bar(x + offset, values[i],width,  label = names[i])
        multiplier += 1
    print(x + width)
    ax.set_xticks(x + width / 2, indices)

    ax.set_title(title)
    ax.legend(loc='upper left', ncols=len(indices))

    plt.show()

def time_to_seconds(time_str):
    # Split the string at 'm' to separate minutes and seconds
    minutes, seconds = time_str.split('m')
    
    # Remove the 's' from the seconds part and convert both parts to float
    seconds = float(seconds.replace('s', ''))
    
    # Convert minutes to seconds and return the total
    return float(minutes) * 60 + seconds

# Function to parse time values from the input text file
def parse_times(filename):
    real_times = []
    user_times = []
    sys_times = []

    # Open and read the file
    with open(filename, 'r') as f:
        real_times = []
        user_times = []
        sys_times = []

        lines = f.readlines()  # Read all lines from the file

        i = 0  # Index for line processing
        while i < len(lines):
            # Skip empty lines
            if lines[i].strip() == "":
                i += 1
                continue

            # Process the next 3 non-empty lines
            if i + 2 < len(lines) and lines[i+1].strip() != "" and lines[i+2].strip() != "":
                real_line = lines[i].strip()
                user_line = lines[i+1].strip()
                sys_line = lines[i+2].strip()

                # Extract time values (ignoring 'm' and 's' part)
                real_time = time_to_seconds(real_line.split()[1])  # e.g., 0.002
                user_time = time_to_seconds(user_line.split()[1])  # e.g., 0.000
                sys_time = time_to_seconds(sys_line.split()[1])    # e.g., 0.001

                # Append the times to the respective lists
                real_times.append(real_time)
                user_times.append(user_time)
                sys_times.append(sys_time)

                # Skip the next two lines since we've already processed them
                i += 3
            else:
                # If we can't find a full block (real, user, sys), just move to the next non-empty line
                i += 1

    return np.array([np.mean(real_times), np.mean(user_times), np.mean(sys_times)])