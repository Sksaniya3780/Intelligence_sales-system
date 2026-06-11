import os
import joblib

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "sales_forecast_model.pkl"
)


def load_model():
    """
    Load trained sales forecasting model
    """
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}"
        )

    model = joblib.load(MODEL_PATH)
    return model