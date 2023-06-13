import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

v1 = np.array([10,10,10])
v2 = np.array([-1, 1, 1])

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

x, y = np.meshgrid(x, y)
eq = -1 * x + -1 * y + 0
ax.plot_surface(x, y, eq)

#VECTOR 1
#x, y, z
ax.quiver(0, 10, 0, v1[0], v1[1], v1[2])
#VECTOR 2
# ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='b', arrow_length_ratio=0.1)

plt.title('3D Vector Plot')

plt.show()