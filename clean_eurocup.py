import pandas as pd
import numpy as np

RAW_PATH = r"C:\Users\Gene\OneDrive\Desktop\VS-Code Python\DataPractice\eurocup_box_score.csv"

def minutes_to_decimal(m):
    """Convert 'MM:SS' string to decimal minutes. DNP / missing -> 0.0"""
    if pd.isna(m) or m == "DNP":
        return 0.0
    try:
        mm, ss = m.split(":")
        return round(int(mm) + int(ss) / 60, 2)
    except (ValueError, AttributeError):
        return np.nan

def clean():
    df = pd.read_csv(RAW_PATH)

    # 1. Trim whitespace on all string/object columns
    str_cols = df.select_dtypes(include="object").columns
    for col in str_cols:
        df[col] = df[col].str.strip()

    # 2. Standardise text fields
    df["player"] = df["player"].str.title()          # "BLIDARU, ADRIAN" -> "Blidaru, Adrian"
    df["team_id"] = df["team_id"].str.upper()
    df["phase"] = df["phase"].str.upper()

    # 3. Extract a numeric season year from season_code (e.g. "U2007" -> 2007)
    df["season_year"] = df["season_code"].str.extract(r"(\d{4})").astype(int)

    # 4. Split out team-total rows (dorsal == "TOTAL") from individual player rows.
    #    These are two different grains of data and shouldn't be analysed together.
    is_team_total = df["dorsal"] == "TOTAL"
    team_totals = df[is_team_total].copy()
    players = df[~is_team_total].copy()

    # 5. Convert minutes "MM:SS" -> decimal minutes for both subsets
    players["minutes_played"] = players["minutes"].apply(minutes_to_decimal)
    team_totals["minutes_played"] = team_totals["minutes"].apply(minutes_to_decimal)
    players = players.drop(columns=["minutes"])
    team_totals = team_totals.drop(columns=["minutes"])

    # 6. Convert 0/1 floats to proper booleans
    for col in ["is_starter", "is_playing"]:
        players[col] = players[col].astype(int).astype(bool)
        team_totals[col] = team_totals[col].astype(int).astype(bool)

    # 7. Did-not-play players (is_playing == False) never logged a stat line;
    #    make that explicit rather than leaving ambiguous zeros.
    players["did_not_play"] = ~players["is_playing"]

    # 8. Derived shooting efficiency fields (guard against divide-by-zero)
    players["two_pt_pct"] = np.where(
        players["two_points_attempted"] > 0,
        (players["two_points_made"] / players["two_points_attempted"]).round(3),
        np.nan,
    )
