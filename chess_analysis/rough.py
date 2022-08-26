import pandas as pd

path = "/Users/tony/PycharmProjects/chess/chess_analysis/chess200-csv.csv"
path_2 = "/Users/tony/PycharmProjects/chess/chess_analysis/chess.csv"

df = pd.read_csv(path)
df_2 = pd.read_csv(path_2)

#player with the lowest rating
print(df['rating'].min())