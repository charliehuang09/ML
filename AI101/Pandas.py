import pandas as pd
df = pd.read_csv('segmentation.csv')
print(df.columns)
print(df['AreaStatusCh1'])