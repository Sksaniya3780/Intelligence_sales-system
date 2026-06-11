import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from sklearn.model_selection import train_test_split

from model_loader import load_model


def evaluate_model():

    df = pd.read_csv(
        "dataset/processed_sales.csv"
    )

    features = [
        "quantity",
        "inventory",
        "month",
        "day",
        "day_of_week",
        "quarter"
    ]

    X = df[features]

    y = df["sales_amount"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = load_model()

    predictions = model.predict(
        X_test
    )

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    mse = mean_squared_error(
        y_test,
        predictions
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    print("\nModel Evaluation")

    print(f"MAE : {mae:.2f}")
    print(f"MSE : {mse:.2f}")
    print(f"R2  : {r2:.2f}")


if __name__ == "__main__":
    evaluate_model()