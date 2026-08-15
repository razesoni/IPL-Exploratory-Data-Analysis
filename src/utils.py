"""
utils.py
--------
Helper functions for loading, cleaning, normalizing team names,
and computing metrics for the IPL Matches Analytics Dashboard.
"""

from typing import List, Tuple
import pandas as pd


# Dictionary to unify historical/rebranded team names
TEAM_MAPPING = {
    "Delhi Daredevils": "Delhi Capitals",
    "Kings XI Punjab": "Punjab Kings",
    "Deccan Chargers": "Sunrisers Hyderabad",
    "Rising Pune Supergiants": "Rising Pune Supergiant",
    "Pune Warriors": "Rising Pune Supergiant",
    "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
}


def load_and_preprocess_ipl_data(filepath: str = "data/raw/matches.csv") -> pd.DataFrame:
    """
    Loads raw IPL matches dataset, normalizes team names,
    handles missing values, and calculates outcome metrics.
    """
    df = pd.read_csv(filepath)

    # Drop column with excessive nulls as identified in EDA
    if "method" in df.columns:
        df.drop("method", axis=1, inplace=True)

    # Apply team rebranding unification
    team_cols = ["team1", "team2", "toss_winner", "winner"]
    for col in team_cols:
        if col in df.columns:
            df[col] = df[col].replace(TEAM_MAPPING)

    # Clean date format
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Add boolean flag for toss-winner match conversion
    df["toss_match_winner"] = df["toss_winner"] == df["winner"]

    return df


def filter_ipl_dataset(
    df: pd.DataFrame,
    seasons: List[str],
    match_types: List[str],
    teams: List[str],
    cities: List[str]
) -> pd.DataFrame:
    """
    Filters the dataset based on sidebar options.
    """
    filtered = df.copy()

    if seasons:
        filtered = filtered[filtered["season"].astype(str).isin(seasons)]

    if match_types:
        filtered = filtered[filtered["match_type"].isin(match_types)]

    if teams:
        filtered = filtered[
            filtered["team1"].isin(teams) | filtered["team2"].isin(teams)
        ]

    if cities:
        filtered = filtered[filtered["city"].isin(cities)]

    return filtered


def get_team_win_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes matches played, matches won, and overall win percentage per team.
    """
    matches_played_series = df["team1"].value_counts().add(df["team2"].value_counts(), fill_value=0)
    matches_won_series = df["winner"].value_counts()

    stats_df = pd.DataFrame({
        "Team": matches_played_series.index,
        "Played": matches_played_series.values.astype(int),
        "Won": [int(matches_won_series.get(team, 0)) for team in matches_played_series.index]
    })

    stats_df["Win %"] = ((stats_df["Won"] / stats_df["Played"]) * 100).round(2)
    return stats_df.sort_values(by="Win %", ascending=False)


def get_top_pom_players(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """
    Returns top N Player of the Match award winners.
    """
    if "player_of_match" not in df.columns or df.empty:
        return pd.DataFrame(columns=["Player", "Awards"])

    pom_df = df["player_of_match"].value_counts().head(top_n).reset_index()
    pom_df.columns = ["Player", "Awards"]
    return pom_df


def get_final_winners_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates IPL Final matches and count of championship titles won.
    """
    finals_df = df[df["match_type"] == "Final"]
    if finals_df.empty:
        return pd.DataFrame(columns=["Team", "Titles"])

    titles_df = finals_df["winner"].value_counts().reset_index()
    titles_df.columns = ["Team", "Titles"]
    return titles_df