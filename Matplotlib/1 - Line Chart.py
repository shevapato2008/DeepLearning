import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 10)			# arg1 = start, arg2 = end, arg3 = number of points
y = np.sin(x)
plt.plot(x, y)
plt.show()

# Add some labels
plt.xlabel("Time")
plt.ylabel("Some function of time")
plt.title("My cool chart")
plt.show()