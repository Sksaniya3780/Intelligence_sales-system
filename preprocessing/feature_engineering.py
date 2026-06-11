import pandas as pd


class FeatureEngineering:

    @staticmethod
    def create_date_features(df):

        if "order_date" not in df.columns:
            return df

        df["order_date"] = pd.to_datetime(
            df["order_date"],
            errors="coerce"
        )

        df["year"] = df["order_date"].dt.year
        df["month"] = df["order_date"].dt.month
        df["day"] = df["order_date"].dt.day
        df["day_of_week"] = df["order_date"].dt.dayofweek
        df["quarter"] = df["order_date"].dt.quarter

        return df

    @staticmethod
    def create_sales_features(df):

        if (
            "sales_amount" not in df.columns
            or "quantity" not in df.columns
        ):
            return df

        df["sales_per_unit"] = (
            df["sales_amount"]
            / (df["quantity"] + 1)
        )

        return df

    @staticmethod
    def create_inventory_features(df):

        if (
            "inventory" not in df.columns
            or "quantity" not in df.columns
        ):
            return df

        df["inventory_ratio"] = (
            df["inventory"]
            / (df["quantity"] + 1)
        )

        return df

    @staticmethod
    def engineer_features(df):

        df = FeatureEngineering.create_date_features(df)
        df = FeatureEngineering.create_sales_features(df)
        df = FeatureEngineering.create_inventory_features(df)

        return df