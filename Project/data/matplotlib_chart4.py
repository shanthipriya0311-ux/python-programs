import pandas  as pd 
import matplotlib.pyplot as plt
df=pd.read_csv("data/ipl_matches_clean.csv")
print(df.columns)
winner_counts = df["winner"].value_counts()
plt.figure(figsize=(12,6))
plt.bar(winner_counts.index,winner_counts.values)
plt.title("IPL Matches Won by Team")
plt.xlabel("Team")
plt.ylabel("number of wins")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
