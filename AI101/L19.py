import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import random
# Importing the dataset
dataset = pd.read_csv('/Users/charlie/ML/AI101/ads_CTR_optimisation.csv')
dataset.head()
ad_selected = []
d = 10
N = 10000
# Implementing UCB
number_of_selections = np.full((d), 0)
# define N
number_of_rewards_1 = np.full((d), 0)
number_of_rewards_0 = np.full((d), 0)
total_reward = 0

for n in range(0, N):
    ad = 0
    max_random = 0
    
    for i in range(0, d):
        random_data = random.betavariate(number_of_rewards_1[i] + 1, number_of_rewards_0[i] + 1)
        if random_data > max_random:
            max_random = random_data
            ad = i
    ad_selected.append(ad)
    reward = dataset.iloc[n, ad]
    if reward == 1:
        number_of_rewards_1 += 1
    else:
        number_of_rewards_0 += 1
    total_reward += reward
    
    
plt.plot(ad_selected)
print(total_reward)