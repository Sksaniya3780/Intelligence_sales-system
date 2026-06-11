import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

DATA_PATH = "dataset/processed_sales.csv"
MODEL_PATH = "model/sales_forecast_model.pkl"


def train_model():

    print("Loading dataset...")

    df = pd.read_csv(DATA_PATH)

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

    print("Training model...")

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    print(f"MAE: {mae:.2f}")

    joblib.dump(
        model,
        MODEL_PATH
    )

    print("Model saved successfully")


if __name__ == "__main__":
    train_model()