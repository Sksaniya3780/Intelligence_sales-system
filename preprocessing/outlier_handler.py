import numpy as np


class OutlierHandler:

    @staticmethod
    def remove_outliers_iqr(df, column):

        if column not in df.columns:
            return df

        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        return df[
            (df[column] >= lower)
            & (df[column] <= upper)
        ]

    @staticmethod
    def cap_outliers(df, column):

        if column not in df.columns:
            return df

        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        df[column] = np.where(
            df[column] > upper,
            upper,
            np.where(
                df[column] < lower,
                lower,
                df[column]
            )
        )

        return df