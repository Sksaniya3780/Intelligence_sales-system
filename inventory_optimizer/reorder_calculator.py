import pandas as pd


class ReorderCalculator:

    @staticmethod
    def calculate_reorder_point(
        avg_daily_demand,
        lead_time_days,
        safety_stock
    ):
        """
        Reorder Point Formula

        ROP =
        (Average Daily Demand × Lead Time)
        + Safety Stock
        """

        reorder_point = (
            avg_daily_demand *
            lead_time_days
        ) + safety_stock

        return round(reorder_point, 2)

    @staticmethod
    def add_reorder_column(df):

        reorder_points = []

        for _, row in df.iterrows():

            demand = row["quantity"]

            safety_stock = row.get(
                "safety_stock",
                20
            )

            rop = (
                ReorderCalculator
                .calculate_reorder_point(
                    demand,
                    7,
                    safety_stock
                )
            )

            reorder_points.append(rop)

        df["reorder_point"] = reorder_points

        return df


if __name__ == "__main__":

    result = ReorderCalculator.calculate_reorder_point(
        avg_daily_demand=20,
        lead_time_days=7,
        safety_stock=87
    )

    print(f"Reorder Point = {result}")