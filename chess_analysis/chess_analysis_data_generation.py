import pandas as pd

path = "/Users/tony/Desktop/datarepo/chess/chess.csv"

df = pd.read_csv(path)


def distribution_of_players_by_country():
    new_df = df['Country'].value_counts().rename_axis('Country').reset_index(name='Number of players')
    new_df.sort_values(by=['Number of players'], inplace=True, ascending=False)
    new_df.to_csv('distribution_of_players_by_country.csv', index=False)
    return new_df

distribution_of_players_by_country()


def distribution_of_players_by_age():
    new_df = df['Age'].value_counts().rename_axis('Age').reset_index(name='Number of players')
    new_df.sort_values(by=['Age'], inplace=True)
    new_df.to_csv('distribution_of_players_by_age.csv', index=False)

    return new_df


distribution_of_players_by_age()


def distribution_of_players_by_age_group():
    df['Age Group'] = pd.cut(df['Age'], bins=[0, 18, 25, 30, 35, 40, 45, 50, 55,60,65,70],
                             labels=['0-18', '18-25', '25-30', '30-35', '35-40', '40-45', '45-50', '50-55', '55-60', '60-65', '65-70'])

    new_df = df['Age Group'].value_counts().rename_axis('Age Group').reset_index(name='Number of players')
    new_df.sort_values(by=['Age Group'], inplace=True)
    new_df.to_csv('players_by_age_group.csv', index=False)

    return new_df


distribution_of_players_by_age_group()


def distribution_of_players_by_rating_group():
    df['Rating_Group'] = pd.cut(df['Rating'], bins=[2650, 2700, 2750, 2800, 2850, 2900],
                                labels=['2650-2700', '2700-2750', '2750-2800', '2800-2850', '2850-2900'])
    new_df = df['Rating_Group'].value_counts().rename_axis('Rating_Group').reset_index(name='Number of players')
    new_df.sort_values(by=['Rating_Group'], inplace=True)
    new_df.to_csv('players_by_rating_group.csv', index=False)

    return new_df


distribution_of_players_by_rating_group()

def distribution_of_players_by_year_born():
    new_df = df['B-Year'].value_counts().rename_axis('Year').reset_index(name='Number of players')

    new_df.sort_values(by=['Year'], inplace=True)
    new_df.to_csv('players_by_year_born.csv', index=False)

    return new_df


distribution_of_players_by_year_born()


def distribution_of_players_by_year_joined():
    new_df = df['J-Year'].value_counts().rename_axis('Year').reset_index(name='Number of players')

    new_df.sort_values(by=['Year'], inplace=True)
    new_df.to_csv('players_by_year_joined.csv', index=False)

    return new_df