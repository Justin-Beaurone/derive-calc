# Creates randomly colored logo for derivative calculator.
import numpy as np
from matplotlib import pyplot as plt
import random

# Returns a random RGB tuple.
def RTup():
    return (random.random(), random.random(), random.random())

# Makes the logo.
def MakeLogo():
    x = np.arange(0, (2*np.pi), 0.0001)
    xd = np.cos(x) + np.pi
    yd = np.sin(x)
    fig = plt.figure()
    fig.set_size_inches(5, 1.6)
    ax = plt.Axes(fig, [0.,0.,1.,1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.plot(xd, yd, color=RTup())
    plt.plot(x, np.sin(0.5*x), color=RTup())
    plt.plot(x, -np.sin(0.5*x), color=RTup())
    plt.savefig('logo.png', transparent=True)

# Creates random logo if the file is run without being imported as a module.
if __name__ == "__main__":
    MakeLogo()
