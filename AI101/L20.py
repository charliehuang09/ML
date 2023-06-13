# We will focus on providing a basic recommendation system by 
# suggesting items that are most similar to a particular item, 
# in this case, movies. Keep in mind, this is not a true robust 
# recommendation system, to describe it more accurately,it just 
# tells you what movies/items are most similar to your movie choice.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read data
column_names = ['user_id', 'item_id', 'rating', 'timestamp']
# read movie titles:
a = pd.read_csv('/Users/charlie/ML/AI101/u.data', sep='\t', names=column_names)
b = pd.read_csv('/Users/charlie/ML/AI101/Movie_Id_Titles')

df = pd.merge(a, b, on='item_id')


# merge data on column item_id


# Visualization
title = df.groupby('title')
meanRating = title['rating'].mean().sort_values(ascending=False)

rating = df.groupby('rating')

rating.hist(bins=50)
# Construct a recommending system
# First create a matrix that has the user ids on one access and the movie title on another axis. Each cell will then consist of the rating the user gave to that movie. Note there will be a lot of NaN values, because most people have not seen most of the movies.


# Let's choose starwars, a sci-fi movie


# calculation correlation between startwars and other movies


# remove NaN values


# join along index (movie title) 


# remove not frequently reviewed movie (for robustness)

