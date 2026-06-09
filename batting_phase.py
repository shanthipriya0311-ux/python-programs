import pandas as pd
import numpy as np
bbb = pd.read_csv("ipl_ball_by_ball.csv", low_memory=False)
batting = bbb.groupby('batter').agg(
    runs=('batter_runs', 'sum'),
    balls_faced=('ball_in_over', 'count'),
    innings=('match_id', 'nunique'),
    sixes=('batter_runs', lambda x: (x == 6).sum()),
    fours=('batter_runs', lambda x: (x == 4).sum())
).reset_index()
print(batting.head(10))
import pandas as pd

bbb = pd.read_csv("ipl_ball_by_ball.csv", low_memory=False)

batting = bbb.groupby('batter').agg(
    runs=('batter_runs', 'sum'),
    balls_faced=('ball_in_over', 'count'),
    innings=('match_id', 'nunique'),
    sixes=('batter_runs', lambda x: (x == 6).sum()),
    fours=('batter_runs', lambda x: (x == 4).sum())
).reset_index()
print(batting.head(10))
dismissals = (
    bbb[bbb['wicket_player_out'].notna()]
    .groupby('wicket_player_out')
    .size()
    .reset_index(name='dismissals')
)

batting = batting.merge(
    dismissals, left_on='batter', right_on='wicket_player_out', how='left'
)
batting['dismissals'] = batting['dismissals'].fillna(0).astype(int)
batting['average'] = (batting['runs'] / batting['dismissals'].replace(0, np.nan)).round(2)
batting['strike_rate'] = (batting['runs'] / batting['balls_faced'] * 100).round(2)
batting['boundary_pct'] = ((batting['fours'] + batting['sixes']) / batting['balls_faced'] * 100).round(2)
batting_qual = batting[batting['innings'] >= 20].copy()
print(batting_qual.shape)
print(batting_qual[['average','strike_rate','boundary_pct']].describe())
print(batting.nlargest(20, 'runs')[['batter', 'runs', 'innings', 'average', 'strike_rate', 'boundary_pct']].to_string(index=False))
def minmax(series):
    return (series - series.min()) / (series.max() - series.min()) * 100
batting_qual['sr_norm'] = minmax(batting_qual['strike_rate'])
batting_qual['avg_norm'] = minmax(batting_qual['average'])
batting_qual['bd_norm'] = minmax(batting_qual['boundary_pct'])
W_SR, W_AVG, W_BD = 0.50, 0.35, 0.15
batting_qual['bat_index'] = (
    batting_qual['sr_norm'] * W_SR +
    batting_qual['avg_norm'] * W_AVG +
    batting_qual['bd_norm'] * W_BD
).round(2)
print(
    batting_qual.sort_values('bat_index', ascending=False)[
        ['batter', 'bat_index']
    ].head(20)
)