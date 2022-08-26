import pandas as pd

path = "/Users/tony/PycharmProjects/chess/chess_analysis/chess200-csv.csv"

df = pd.read_csv(path)

max_Age = df['age'].min()
print(max_Age)