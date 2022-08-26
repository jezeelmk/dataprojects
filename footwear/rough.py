import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


path = '/Users/tony/PycharmProjects/chess/footwear/distribution_of_sales_price_Across_all_brands.csv'
df = pd.read_csv(path)

bin = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450',
                          '450-500', '500-550', '550-600']

#set second row as df_ua


def df_to_list(loc_value):
    x = df.iloc[loc_value]
    return x.tolist()[1:]

 #under armour
df_asics = df_to_list(2)  #asics
df_nike = df_to_list(3)  #nike
df_adidas = df_to_list(4)  #adidas
df_puma = df_to_list(5)  #puma

print(df_puma)