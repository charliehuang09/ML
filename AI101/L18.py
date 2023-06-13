import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

# Importing the dataset
data = pd.read_csv('/Users/charlie/ML/AI101/ads_CTR_optimisation.csv')
data.head()
ad_selected = []
d = 10
N = 10000
# Implementing UCB
number_of_selections = np.full((d), 0)
# define N
sum_of_rewards = np.full((d), 0)
total_reward = 0
# define R
for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if number_of_selections[i] < 1:
            upper_bound = 1e20
        else:
            average_reward = sum_of_rewards[i] / number_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / number_of_selections[i])
            upper_bound = average_reward + delta_i
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ad_selected.append(ad)
    number_of_selections[ad] = number_of_selections[ad] + 1
    reward = data.iloc[n, ad]
    sum_of_rewards[ad] = sum_of_rewards[ad] + reward
    total_reward = total_reward + reward

            

# Visualising the results
plt.hist(ad_selected)
plt.show()

print(str(total_reward))