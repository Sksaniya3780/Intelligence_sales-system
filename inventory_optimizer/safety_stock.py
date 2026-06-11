import pandas as pd
import numpy as np


class SafetyStockCalculator:

    @staticmethod
    def calculate_safety_stock(
        avg_daily_demand,
        lead_time_days,
        service_factor=1.65
    ):
        """
        Safety Stock Formula

        Safety Stock =
        Service Factor × √Lead Time × Avg Daily Demand
        """

        safety_stock = (
            service_factor *
            np.sqrt(lead_time_days) *
            avg_daily_demand
        )

        return round(safety_stock, 2)

    @staticmethod
    def add_safety_stock_column(df):

        df["safety_stock"] = df.apply(
            lambda row:
            SafetyStockCalculator.calculate_safety_stock(
                row["quantity"],
                7
            ),
            axis=1
        )

        return df


if __name__ == "__main__":

    result = SafetyStockCalculator.calculate_safety_stock(
        avg_daily_demand=20,
        lead_time_days=7
    )

    print(f"Safety Stock = {result}")