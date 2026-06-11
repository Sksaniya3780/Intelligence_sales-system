import os
import pandas as pd

from safety_stock import SafetyStockCalculator
from reorder_calculator import ReorderCalculator


class StockAlerts:

    @staticmethod
    def generate_alerts(df):

        alerts = []

        for _, row in df.iterrows():

            inventory = row["inventory"]
            demand = row["quantity"]

            safety_stock = (
                SafetyStockCalculator.calculate_safety_stock(
                    demand,
                    7
                )
            )

            reorder_point = (
                ReorderCalculator.calculate_reorder_point(
                    demand,
                    7,
                    safety_stock
                )
            )

            if inventory <= reorder_point:
                alerts.append(
                    f"Reorder Required: {row['product']}"
                )
            else:
                alerts.append(
                    f"Stock OK: {row['product']}"
                )

        df["stock_status"] = alerts

        return df


if __name__ == "__main__":

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR = os.path.dirname(BASE_DIR)

    file_path = os.path.join(
        ROOT_DIR,
        "dataset",
        "processed_sales.csv"
    )

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        print("Run preprocessing_pipeline.py first.")
        exit()

    df = pd.read_csv(file_path)

    result = StockAlerts.generate_alerts(df)

    print(
        result[
            ["product", "inventory", "stock_status"]
        ]
    )