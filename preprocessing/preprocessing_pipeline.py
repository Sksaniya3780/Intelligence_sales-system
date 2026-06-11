import os
import pandas as pd

from preprocessing.data_cleaning import DataCleaning
from preprocessing.outlier_handler import OutlierHandler
from preprocessing.feature_engineering import FeatureEngineering


class PreprocessingPipeline:

    @staticmethod
    def process(df):

        df = DataCleaning.clean_data(df)

        if "sales_amount" in df.columns:
            df = OutlierHandler.remove_outliers_iqr(
                df,
                "sales_amount"
            )

        df = FeatureEngineering.engineer_features(df)

        return df


if __name__ == "__main__":

    CURRENT_DIR = os.path.dirname(
        os.path.abspath(__file__)
    )

    ROOT_DIR = os.path.dirname(
        CURRENT_DIR
    )

    input_file = os.path.join(
        ROOT_DIR,
        "dataset",
        "sample_sales_data.csv"
    )

    output_file = os.path.join(
        ROOT_DIR,
        "dataset",
        "processed_sales.csv"
    )

    if not os.path.exists(input_file):
        raise FileNotFoundError(
            f"Dataset not found: {input_file}"
        )

    df = pd.read_csv(input_file)

    processed_df = PreprocessingPipeline.process(df)

    processed_df.to_csv(
        output_file,
        index=False
    )

    print(
        f"Processed file saved: {output_file}"
    )