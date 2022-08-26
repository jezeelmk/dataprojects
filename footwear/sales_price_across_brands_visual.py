import pandas as pd
import matplotlib.pyplot as plt


path = "/Users/tony/PycharmProjects/chess/footwear/distribution_of_sales_price.csv"

df = pd.read_csv(path)

x_values = df['Sales Price Range']
y_values = df['count']

plt.bar(x_values, y_values)
plt.xlabel('Brand')
plt.ylabel('Count')

for i, v in enumerate(y_values):
    plt.text(x_values[i], v, str(v))

plt.title('Distribution of Sales Price  Brands')
plt.show()