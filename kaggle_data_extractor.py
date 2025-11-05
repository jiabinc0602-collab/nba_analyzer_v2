import os
import glob
import pandas as pd

all_odds_dataframes =[]
path = "kaggle_data/*.csv"
csv_files = glob.glob(path)
print(f"Found CSV files, loading them...")
for file in csv_files:
    try:
        betting_lines = pd.read_csv(file, low_memory=False)
        all_odds_dataframes.append(betting_lines)
    except pd.errors.EmptyDataError:
        print(f"skipping file: {file}(empty)")
print("All files loaded, concatenating.")
odds_df = pd.concat(all_odds_dataframes,ignore_index=True)

odds_df.to_csv('kaggle_odds_combined.csv', index=False)
print("Head of combined data")
print(odds_df.head())
print("Info of combined data")
print(odds_df.info())