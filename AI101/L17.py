import matplotlib.pyplot as plt
import pandas as pd
import random

# Importing the dataset
dataset = pd.read_csv('/Users/charlie/ML/AI101/ads_CTR_optimisation.csv')
dataset.head()

# Implementing Random Selection
N = 10000
d = 10

ad_selected = []
total_reward = 0

for n in range(0, N):
    # generate a random number between 0 and 9
    ad = random.randrange(d)
    # assume each round select ad randomly
    ad_selected.append(ad)
    # add reward
    reward = dataset.iloc[n, ad]
    # update total reward
    total_reward = total_reward + reward

# Visualising the results
plt.hist(ad_selected)
plt.show()

print(total_reward)