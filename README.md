# EuroCup Analytics

Data cleaning pipeline and analytics visualisations for 19 seasons of EuroCup basketball box score data (2007–2025), built with pandas and matplotlib.

 ## Key Findings

- **Three-point attempt rate climbed from ~35% to ~40.5% of all shots between 2007–08 and 2024–25** (peaking near 41% in 2021–22), with a clear trough around 2010–11 (~32.5%) before the sustained rise began.
- **Scoring pace (points per team per game) rose from ~78 to ~86 over the same period**, but the two trends decouple after 2016: three-point rate kept climbing steadily through 2016–2021 while scoring pace plateaued around 81 points/game, then pace jumped sharply from 2022 onward (81 → 86) even as three-point rate flattened. This suggests the recent scoring surge is being driven by something beyond shot selection alone (pace of play, free-throw rate, or turnover reduction are worth investigating next).
- **In the 2024–25 volume-vs-efficiency scatter (n=194 qualified players), there's only a weak positive relationship between shot volume and True Shooting %;**  most high-volume scorers cluster in a mid-efficiency band (55–65% TS), meaning taking a lot of shots doesn't reliably predict scoring efficiently.
- **The standout performer by efficiency at high volume is Creek**, posting the highest True Shooting % (~73%) among the top scorers while still averaging ~17.5 points/game; a rare combination of volume and efficiency.
- **Russell is the clearest volume-over-efficiency outlier**: highest scoring volume in the dataset (~20 ppg) but a comparatively modest ~55% True Shooting %, well below the efficiency of similarly high-volume peers.

<img width="2179" height="1305" alt="3PT Revolution In EuroCup Basketball" src="https://github.com/user-attachments/assets/de7f85ee-4de6-4e86-bda4-f305fe062407" />

## Overview

This project takes a raw EuroCup box score dataset (~97,000 rows spanning 19 seasons) and:

1. Cleans and validates it into an analysis-ready format
2. Derives shooting efficiency metrics not present in the raw data
3. Visualises league-wide trends and player-level performance

## Why this project

EuroCup box scores are publicly available but rarely analysed in depth compared to NBA data. This project cleans and structures 19 seasons of raw box scores to answer two questions: how has shot selection reshaped scoring at the league level, and which players combine scoring volume with efficiency in a single season.

## Dataset

- **Source:** EuroCup player-game box scores, 2007–08 through 2024–25 seasons
- **Raw size:** ~97,000 rows (mixes individual player rows with team-total rows)
- **Cleaned output:** 89,303 player-game rows + 7,812 team-total rows

## What the cleaning script does

`clean_eurocup.py` handles:

- Splitting player-level rows from team-total rows (different data grains)
- Converting `"MM:SS"` minute strings and `"DNP"` entries into numeric minutes
- Converting 0/1 float flags into proper booleans
- Standardising text fields (names, team codes)
- Deriving shooting efficiency stats: 2PT%, 3PT%, FT%, True Shooting %
- Running validation checks (makes ≤ attempts, no duplicate player-games, etc.)

```bash
python3 clean_eurocup.py
```

## Visualisations

### 1. The Three-Point Revolution in EuroCup Basketball

Tracks how three-point shot selection and team scoring pace evolved across 19 seasons league-wide.

<img width="2179" height="1305" alt="3PT Revolution In EuroCup Basketball" src="https://github.com/user-attachments/assets/99629d5a-714a-46f8-8071-7d05ae5a3c62" />

```bash
python3 plot_three_point_trend.py
```

### 2. Scoring Volume vs. Efficiency (2024–25 season)

A player-level scatter plot comparing scoring volume (points per game) against scoring efficiency (True Shooting %), with bubble size representing minutes played. Filtered to players with 10+ games and 10+ minutes/game.

<img width="2050" height="1493" alt="Scoring volume Vs Efficiency" src="https://github.com/user-attachments/assets/f71e783e-745b-4ae6-b293-767179bb62c2" />

```bash
python3 plot_efficiency_scatter.py
```

## Requirements

```bash
pip install pandas numpy matplotlib
```

## Project structure

```
eurocup-analytics/
├── clean_eurocup.py               # data cleaning pipeline
├── plot_three_point_trend.py      # season-trend line chart
├── plot_efficiency_scatter.py     # player efficiency scatter plot
├── eurocup_box_score.csv          # raw input data
├── eurocup_box_score_clean.csv    # cleaned player-game rows
├── eurocup_team_totals_clean.csv  # cleaned team-total rows
├── eurocup_three_point_trend.png
├── eurocup_efficiency_scatter.png
└── README.md
```
