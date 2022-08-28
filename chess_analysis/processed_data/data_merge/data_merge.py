import pandas as pd

path_2000 = '/Users/tony/PycharmProjects/chess/chess_analysis/processed_data/players_by_rating_range_2000.csv'
path_2022 = '/Users/tony/PycharmProjects/chess/chess_analysis/processed_data/players_by_rating_range_2022.csv'


df_2000 = pd.read_csv(path_2000)
df_2022 = pd.read_csv(path_2022)

#merge the two dataframes
df_merged = pd.merge(df_2000, df_2022, on='rating_range')

#name the new column '2000' and '2022'
df_merged.rename(columns={'Number of players_x': '2000_players', 'Number of players_y': '2022_players'}, inplace=True)

print(df_merged)

df_merged.to_csv('/Users/tony/PycharmProjects/chess/chess_analysis/processed_data/players_by_rating_range_merged.csv')

