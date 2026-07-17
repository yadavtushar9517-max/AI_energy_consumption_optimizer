import pandas as pd

def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    return df

def clean_data(df):
    df = df.drop_duplicates()
    df = df.fillna(df.mean(numeric_only=True))
    return df

def summary(df):
    return df.describe()