import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/Users/charlie/ML/AI101/segmentation.csv')
angle = df['AngleCh1'].values
plt.hist(angle)

bins = 10
binMin = np.min(angle)
binMax = np.max(angle)
binEdges = np.linspace(binMin, binMax, bins+1)
print(binEdges)

classifiedData = np.full([2019], 0)

for e in range(bins):
    inside_bin = np.where(angle<=binEdges[e+1])[0]
    if len(inside_bin) > 0:
        classifiedData[inside_bin] = e
        angle[inside_bin] = np.nan

print(classifiedData[:10])
C = np.full([bins], 0)
for i in range(2019):
    C[classifiedData[i]] = C[classifiedData[i]] + 1
pX = C / np.sum(C)
plt.plot(pX)
plt.show()
    