import numpy as np
import matplotlib.pyplot as plt

# define normal distribution
mean = 0
std = 2
length = 1000
# generate data based from normal distribution
data = np.random.randn(length) * std + mean
# plot density
plt.hist(data, density=True, bins=20)
plt.show()
# define your bins
bins = 20
binMin = np.min(data)
binMax = np.max(data)
binEdges = np.linspace(binMin, binMax, bins+1)
print("=================== binEdges")
# Define classified data
classifiedData = np.full([length], 0)
# loop over local bins
for e in range(bins):
    inside_bin = np.where(data<=binEdges[e+1])[0]
    if len(inside_bin) > 0:
        classifiedData[inside_bin] = e
        data[inside_bin] = np.nan

print("=================== classifiedData")
print(classifiedData[:10])
# calculate probability density
C = np.full([bins], 0)
for i in range(length):
    C[classifiedData[i]] = C[classifiedData[i]] + 1
pX = C / np.sum(C)
plt.plot(binEdges[1:], pX)
plt.show()

# plot