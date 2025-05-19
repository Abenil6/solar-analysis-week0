import pandas as pd

def clean_data(file_path, save_path):
    df = pd.read_csv(file_path)
    df_cleaned = df.fillna(df.median(numeric_only=True))
    df_cleaned.to_csv(save_path, index=False)
