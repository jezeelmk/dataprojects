import pandas as pd
import matplotlib.pyplot as plt


path = "/Users/tony/PycharmProjects/chess/footwear/average_number_of_reviews_across_brands.csv"

df = pd.read_csv(path)

x_values = df['brand']
y_values = df['avg_num_reviews']

plt.bar(x_values, y_values)
plt.xlabel('number of reviews')
plt.ylabel('Brands')

for i, v in enumerate(y_values):
    plt.text(x_values[i], v, str(v))

plt.title('Average number of reviews Across all Brands')
plt.show()