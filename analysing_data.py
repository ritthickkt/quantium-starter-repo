import pandas as pd
import glob

files = [
  './data/daily_sales_data_0.csv',
  './data/daily_sales_data_1.csv',
  './data/daily_sales_data_2.csv',
]

dfs = []
for file in files:
  df = pd.read_csv(file)
  df = df[df['product'] == 'pink morsel'].copy()
  df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)
  df['Sales'] = df['price'] * df['quantity']
  df = df[['Sales', 'date', 'region']]
  dfs.append(df)


final_df = pd.concat(dfs, ignore_index=True)
final_df.to_csv('pink_morsel_sales.csv', index=False)
