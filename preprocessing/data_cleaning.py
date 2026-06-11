import pandas as pd


class DataCleaning:

    @staticmethod
    def remove_duplicates(df):
        return df.drop_duplicates()

    @staticmethod
    def handle_missing_values(df):

        numeric_cols = df.select_dtypes(
            include=["int64", "float64"]
        ).columns

        for col in numeric_cols:
            df[col] = df[col].fillna(
                df[col].median()
            )

        categorical_cols = df.select_dtypes(
            include=["object"]
        ).columns

        for col in categorical_cols:
            df[col] = df[col].fillna(
                "Unknown"
            )

        return df

    @staticmethod
    def standardize_column_names(df):

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        return df

    @staticmethod
    def clean_data(df):

        df = DataCleaning.standardize_column_names(df)
        df = DataCleaning.remove_duplicates(df)
        df = DataCleaning.handle_missing_values(df)

        return df