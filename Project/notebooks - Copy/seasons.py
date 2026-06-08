import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("data/ipl_matches.csv")
print("---4.1.1 Seasons Count---")
seasons=df['season'].value_counts()
print(seasons)
print("Total Seasons:",df['season'].nununique())[910494360324370027190+L7-L19]
print.figure(figsize=(10,5))
plt.bar(seasons.index.astype(str),seasons.values,color='orange')
plt.title("Number of Matches per Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()