import pandas as pd


def calculate_age(birth_year, year_played):
    return year_played - birth_year


def main():
    # Read People.xlsx file
    people_df = pd.read_excel("People.xlsx")

    # Read Batting.xlsx file
    batting_df = pd.read_excel("Batting.xlsx")

    # Merge the two dataframes on playerID
    merged_df = pd.merge(people_df, batting_df, on="playerID", how="inner")

    # Counter to track the number of players processed
    player_count = 0

    # Group by playerID and iterate through each group
    for playerID, group in merged_df.groupby("playerID"):
        # Extract player's name
        player_name = f"{group['nameLast'].iloc[0]}, {group['nameFirst'].iloc[0]}"

        # Calculate age for each year played
        age_list = []
        for index, row in group.iterrows():
            age = calculate_age(row["birthYear"], row["yearID"])
            age_list.append(age)

        # Print player's ID, name, and age list
        print(f"{playerID} - {player_name}: {age_list}")

        # Increment player count
        player_count += 1

        # Check if 10 players have been processed
        if player_count == 10:
            break


if __name__ == "__main__":
    main()
