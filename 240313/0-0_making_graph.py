# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0, 10, 51)
# y = 2 * x - 3
#
# plt.plot(x, y, 'bx')
# plt.show()
#
# plt.plot(x, y, 'r')
# plt.xlabel('Time (fortnights)')
# plt.ylabel('Distance (furlongs)')
# plt.title('My first graph')
# plt.show()
#
# time = np.linspace(0, 4 * np.pi, 101)
# height = np.exp(- time / 3.0) * np.sin(time * 3)
#
# plt.plot(time, height, 'm-^')
# plt.plot(time, 0.3 * np.sin(time * 3), 'g-')
#
# plt.legend(['damped', 'constant amplitude'])
# plt.xlabel('Time (s)')
# plt.ylabel('height')
# plt.title('Damped oscillation')
#
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(x / 10)
y4 = np.log(x + 1)
y5 = np.tan(x)

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the data with different styles and colors
ax.plot(x, y1, linestyle="-", color="b", label="sin(x)")
ax.plot(x, y2, linestyle="--", color="r", label="cos(x)")
ax.plot(x, y3, linestyle="-.", color="g", label="exp(x/10)")
ax.plot(x, y4, linestyle=":", color="m", label="log(x+1)")
ax.plot(x, y5, linestyle="-", color="y", label="tan(x)")

# Add title and labels
ax.set_title("Crazy Graph")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Add a legend
ax.legend()

# Display the plot
plt.show()
