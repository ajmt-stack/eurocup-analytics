# EuroCup Analytics

Data cleaning pipeline and analytics visualisations for 19 seasons of EuroCup basketball box score data (2007–2025), built with pandas and matplotlib.

<img width="2179" height="1305" alt="3PT Revolution In EuroCup Basketball" src="https://github.com/user-attachments/assets/de7f85ee-4de6-4e86-bda4-f305fe062407" />

## Overview

This project takes a raw EuroCup box score dataset (~97,000 rows spanning 19 seasons) and:

1. Cleans and validates it into an analysis-ready format
2. Derives shooting efficiency metrics not present in the raw data
3. Visualises league-wide trends and player-level performance

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
