import pandas as pd

path = "/Users/tony/Desktop/datarepo/chess/chess.csv"
df = pd.read_csv(path)


def distribution_of_players_by_country():
    new_df = df['Country'].value_counts().rename_axis('country').reset_index(name='number_of_players')
    new_df.sort_values(by=['number_of_players'], inplace=True, ascending=False)
    new_df.to_csv('distribution_of_players_by_country_2022.csv', index=False)
    return new_df


distribution_of_players_by_country()


def distribution_of_players_by_age():
    new_df = df['Age'].value_counts().rename_axis('age').reset_index(name='number_of_players')
    new_df.sort_values(by=['age'], inplace=True)
    new_df.to_csv('distribution_of_players_by_age_2022.csv', index=False)

    return new_df


distribution_of_players_by_age()


def distribution_of_players_by_age_group():
    df['age_group'] = pd.cut(df['Age'], bins=[0, 18, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
                             labels=['0-18', '18-25', '25-30', '30-35', '35-40', '40-45', '45-50', '50-55', '55-60',
                                     '60-65', '65-70'])

    new_df = df['age_group'].value_counts().rename_axis('age_group').reset_index(name='number_of_players')
    new_df.sort_values(by=['age_group'], inplace=True)
    new_df.to_csv('players_by_age_group_2022.csv', index=False)

    return new_df


distribution_of_players_by_age_group()


def distribution_of_players_by_rating_group():
    df['rating_range'] = pd.cut(df['Rating'], bins=[2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900],
                                labels=['2550-2600', '2600-2650', '2650-2700', '2700-2750', '2750-2800', '2800-2850','2850-2900'])
    new_df = df['rating_range'].value_counts().rename_axis('rating_range').reset_index(name='Number of players')
    new_df.sort_values(by=['rating_range'], inplace=True)
    new_df.to_csv('players_by_rating_range_2022.csv', index=False)

    return new_df


distribution_of_players_by_rating_group()


def distribution_of_players_by_year_born():
    new_df = df['B-Year'].value_counts().rename_axis('year').reset_index(name='number_of_players')

    new_df.sort_values(by=['year'], inplace=True)
    new_df.to_csv('players_by_year_born_2022.csv', index=False)

    return new_df


distribution_of_players_by_year_born()
