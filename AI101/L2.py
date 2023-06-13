import matplotlib.pyplot as plt
import numpy as np

x = [0,1,2,3,4,5,6,7,8]
y = np.array(x) * np.array(x)
plt.plot(x, y)

#plt.subplot(1, 2, 1)
#plt.plot(x, y, 'r')
#plt.subplot(2, 2, 4)
#plt.plot(y, x, 'b')


fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8 ,0.8])
axes1.plot(x, y, 'g')

fig, axes = plt.subplots(nrows=1, ncols=2)
for ax in axes:
    ax.plot(x, y, 'b')