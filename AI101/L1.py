import numpy as np
import netCDF4
import pandas as pd
file = '/Users/charlie/ML/AI101/tas_Amon_GFDL-ESM2G_esmHistorical_r1i1p1_199601-200012.nc'
nc = netCDF4.Dataset(file, 'r')

tas = nc.variables['tas'][:]
lon = nc.variables['lon'][:]
lat = nc.variables['lat'][:]

tas_annual = np.mean(tas, axis = 0)

tas_annual.reshape(-1, 1)

lon_all = np.repeat(lon.reshape(1, -1), 90, axis = 0)
lat_all = np.repeat(lat.reshape(-1, 1), 144, axis = 1)

col_1 = lon_all.reshape(-1, 1)
col_2 = lat_all.reshape(-1, 1)
col_3 = tas_annual.reshape(-1, 1)

tmp = pd.DataFrame(np.concatenate((col_1, col_2, col_3), axis=1), columns=['lon', 'lat', 'annual temp'])
                                                                   
                                                                 

