import pandas as pd 
import numpy as np 
bbb=pd.read_csv("ipl_ball_by_ball_clean.csv")
NON_BOWLER = ['run out','retired hurt','obstructing the field','retired out']
bowler_wkts = (
    bbb[(bbb['is_wicket'] == 1) & (~bbb['wicket_kind'].isin(NON_BOWLER))]
    .groupby('bowler')
    .size()
    .reset_index(name='wickets')
)
bowling = bbb.groupby('bowler').agg(
    runs_conceded=('total_runs', 'sum'),
    balls_bowled=('ball_in_over', 'count'),
    matches=('match_id', 'nunique'),
    dot_balls=('is_dot_ball', 'sum')
).reset_index()
bowling = bowling.merge(bowler_wkts, on='bowler', how='left')
bowling['wickets'] = bowling['wickets'].fillna(0).astype(int)
bowling['economy'] = (bowling['runs_conceded'] / bowling['balls_bowled'] * 6).round(2)
bowling['bowl_average'] = (bowling['runs_conceded'] / bowling['wickets'].replace(0, np.nan)).round(2)
bowling['bowl_sr'] = (bowling['balls_bowled'] / bowling['wickets'].replace(0, np.nan)).round(2)
bowling['dot_pct'] = (bowling['dot_balls'] / bowling['balls_bowled'] * 100).round(2)
bowling_qual = bowling[bowling['wickets'] >= 20].copy()
print(bowling_qual.shape)
print(
    bowling_qual[
        ['economy', 'bowl_average', 'bowl_sr', 'dot_pct']
    ].describe()
)
print(
    bowling.sort_values('wickets', ascending=False)[
        ['bowler', 'wickets']
    ].head(20)
)
def minmax(series):
    return (series - series.min()) / (series.max() - series.min()) * 100
def minmax_inv(series):
    return 100 - minmax(series)
bowling_qual['econ_norm'] = minmax_inv(bowling_qual['economy'])
bowling_qual['bavg_norm'] = minmax_inv(bowling_qual['bowl_average'])
bowling_qual['bsr_norm'] = minmax_inv(bowling_qual['bowl_sr'])
bowling_qual['dot_norm'] = minmax(bowling_qual['dot_pct'])
W_ECON, W_BAVG, W_BSR, W_DOT = 0.40, 0.35, 0.15, 0.10
bowling_qual['bowl_index'] = (
    bowling_qual['econ_norm'] * W_ECON +
    bowling_qual['bavg_norm'] * W_BAVG +
    bowling_qual['bsr_norm'] * W_BSR +
    bowling_qual['dot_norm'] * W_DOT
).round(2)
print(
    bowling_qual.sort_values('bowl_index', ascending=False)[
        ['bowler', 'bowl_index']
    ].head(20)
)