import pandas as pd


df = pd.read_csv('/Users/tony/PycharmProjects/chess/chess_analysis/chess.csv')

df.to_csv('fide_rating_data_2022.csv')