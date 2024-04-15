import pandas as pd
from datetime import datetime
import datetime

df_people = pd.read_excel("People.xlsx")

current_year = datetime.datetime.now().year
df_people = pd.read_excel("People.xlsx")

# Step 2: Calculate age of each player based on finalGame year
df_people["age"] = df_people.apply(
    lambda row: (
        pd.to_datetime(row["finalGame"]).year - row["birthYear"]
        if not pd.isnull(row["finalGame"])
        else current_year - row["birthYear"]
    ),
    axis=1,
)

# Step 3: Associate name with player ID
df_people["fullName"] = df_people["nameLast"] + ", " + df_people["nameFirst"]

# Step 4: Print first 10 entries
print("First 10 entries:")
for i in range(10):
    print(
        f"{df_people.iloc[i]['playerID']} - {df_people.iloc[i]['fullName']} - {df_people.iloc[i]['age']}"
    )
