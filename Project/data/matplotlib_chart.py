import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv("data/ipl_ball_by_ball_clean.csv")
print(df.head())
print(df.columns)
over_runs=df.groupby('over')['total_runs'].sum()
plt.figure(figsize=(10,5))
plt.plot(over_runs.index,over_runs,marker='o')
plt.title("Ipl Runs Scored by over")
plt.xlabel("over")
plt.ylabel("Total Runs")
plt.grid(True)
plt.tight_layout()
plt.show()