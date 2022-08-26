import pandas as pd
import matplotlib.pyplot as plt


path = "/Users/tony/PycharmProjects/chess/footwear/average_star_rating_across_brands.csv"

df = pd.read_csv(path)

x_values = df['brand']
y_values = df['avg_star_rating']

plt.bar(x_values, y_values)
plt.xlabel('star rating')
plt.ylabel('Brands')

for i, v in enumerate(y_values):
    plt.text(x_values[i], v, str(v))

plt.title('Average star rating Across all Brands')
plt.show()
