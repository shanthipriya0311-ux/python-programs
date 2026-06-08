import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/ipl_matches_clean.csv")
print(df.head())
print(df.columns)
plt.figure(figsize=(8, 5))
plt.hist(df['total_runs'], bins=30, color='skyblue', edgecolor='black')
plt.title("Run Distribution")
plt.xlabel("Seasons")
plt.ylabel("number of season")
plt.tight_layout()
plt.show()
