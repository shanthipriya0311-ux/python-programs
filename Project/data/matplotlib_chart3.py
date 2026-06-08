import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv("data/ipl_matches.csv")
print(df.columns)
team_matches=df['team1'].value_counts()
plt.figure(figsize=(12,6))
plt.bar(team_matches.index,team_matches.values)
plt.title("IPL Matches Played by Teams")
plt.xlabel("Teams")
plt.ylabel("Number of Matches")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()