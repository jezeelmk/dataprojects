import pandas as pd

df = pd.read_csv('footwear_data_v1.csv')



#drop column named new_column
df.drop(columns=['new_column'], inplace=True)
df.to_csv('footwear_data_v1_new_column_dropped.csv', index=False)