import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv("data/ipl_ball_by_ball.csv")
print(df.columns)
over_runs = df.groupby("over")["total_runs"].sum()
plt.figure(figsize=(10, 5))
plt.plot(over_runs.index,over_runs.values, marker='o')
plt.title("Ipl Runs Scored by Over")
plt.show()