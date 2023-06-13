import numpy as np
import netCDF4
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
rainPath = '/Users/charlie/ML/AI101/pr_Amon_GFDL-ESM2G_historical_r1i1p1_186101-186512.nc'
tempPath = '/Users/charlie/ML/AI101/tas_Amon_GFDL-ESM2G_historical_r1i1p1_186101-186512.nc'
rainNC = netCDF4.Dataset(rainPath, 'r')
tempNC = netCDF4.Dataset(tempPath, 'r') 

tas = tempNC.variables['tas'][:]
rain = rainNC.variables['pr'][:]
lat = rainNC.variables['lat'][:]
lon = rainNC.variables['lon'][:]

                                                                   
RainSF = np.array(rain[:,15, 15]).reshape(-1)
tasSF = np.array(tas[:,15,15]).reshape(-1)
RainSF /= np.mean(RainSF)
tasSF /= np.mean(tasSF)
plt.plot(RainSF, label='Rain')
plt.plot(tasSF, label='temp')
plt.legend()


sns.jointplot(x = RainSF, y = tasSF, kind='reg')

#How does San Jose seasonal temperature and rainfall patterns look like? (matplotlib) 
#How does San Jose temperature-rainfall relationship look like? (seaborn)


#37.3387° N, -121.8853° W
#15, 15