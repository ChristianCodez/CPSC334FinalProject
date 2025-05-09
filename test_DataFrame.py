import pandas as pd
import numpy as np
import os
import shutil

# Helper function to load the original CSV (can be reused in multiple tests)
def load_original_df():
    return pd.read_csv("data.csv")

def test_csv_loads_correctly():
    df = load_original_df()
    assert not df.empty
    assert list(df.columns) == ["Teams", "Best Player", "Average PPG"]

def test_row_count_is_9():
    df = load_original_df()
    assert len(df) == 9

def test_dodgers_player_is_shohei():
    df = load_original_df()
    row = df[df["Teams"] == "Dodgers"]
    assert row.iloc[0]["Best Player"] == "Shohei Ohtani"

def test_christian_carrington_exists():
    df = load_original_df()
    assert "Christian Carrington" in df["Best Player"].values

def test_index_ranks_set_correctly():
    df = load_original_df()
    ranks = ['Best Team', 'Second Best', 'Third Best', '4th', '5th', '6th', 'Third Worst', 'Second Worst', 'Worst Team']
    df.index = ranks
    assert list(df.index) == ranks

def test_swap_dodgers_and_worst_team():
    df = load_original_df()
    df.index = ['Best Team', 'Second Best', 'Third Best', '4th', '5th', '6th', 'Third Worst', 'Second Worst', 'Worst Team']

    # Find indexes
    dodgers_index = df[df["Teams"] == "Dodgers"].index[0]
    worst_team_index = "Worst Team"

    # Swap logic
    temp = df.loc[worst_team_index].copy()
    df.loc[worst_team_index] = df.loc[dodgers_index]
    df.loc[dodgers_index] = temp

    assert df.loc["Worst Team"]["Teams"] == "Dodgers"

def test_swap_christian_to_best_team():
    df = load_original_df()
    df.index = ['Best Team', 'Second Best', 'Third Best', '4th', '5th', '6th', 'Third Worst', 'Second Worst', 'Worst Team']

    original_best = df.loc["Best Team"].copy()
    carrington_index = df[df["Best Player"] == "Christian Carrington"].index[0]

    # Swap
    temp = df.loc["Best Team"].copy()
    df.loc["Best Team"] = df.loc[carrington_index]
    df.loc[carrington_index] = temp

    assert df.loc["Best Team"]["Best Player"] == "Christian Carrington"

def test_no_null_values():
    df = load_original_df()
    assert not df.isnull().values.any()

def test_all_average_ppg_are_numeric():
    df = load_original_df()
    assert df["Average PPG"].apply(lambda x: isinstance(x, (int, float, np.integer, np.float64))).all()

def test_expected_teams_present():
    df = load_original_df()
    expected_teams = {"Dodgers", "Yankees", "Guardians", "Mets", "Phillies", "Tigers", "Padres", "Royals", "Astros"}
    assert set(df["Teams"].values) == expected_teams
