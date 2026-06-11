import pandas as pd


def load_csv(path):

    return pd.read_csv(path)


def save_csv(df, path):

    df.to_csv(
        path,
        index=False
    )


def calculate_total_sales(df):

    return df["sales_amount"].sum()