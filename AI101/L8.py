import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv('/Users/charlie/ML/AI101/segmentation.csv')

plt.subplot(2,2,1)r
plt.hist(df['AreaCh1'])
plt.title('Original')
plt.subplot(2,2,2)
plt.hist(np.log(df['AreaCh1']))
plt.title('Log')
plt.subplot(2,2,3)
plt.hist(np.sqrt(df['AreaCh1']))
plt.title('Root')
plt.subplot(2,2,4)
plt.hist(1/df['AreaCh1'])
plt.title('Inverse')
plt.show()

out, _ = stats.boxcox(df['AreaCh1'])
plt.hist(out)
plt.show()

corr = df.iloc[:,6:16].corr()
sns.heatmap(corr, vmax=1.0, vmin=-1.0, annot=True, fmt='.1f')

