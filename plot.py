import numpy as np
import matplotlib.pyplot as plt


def generate_plot(values, names, indices,title):
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
