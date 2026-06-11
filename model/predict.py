import pandas as pd
from model.model_loader import load_model


def predict_sales(input_data):
    """
    Predict sales using trained model

    Parameters:
    ----------
    input_data : pd.DataFrame

    Returns:
    -------
    prediction
    """

    model = load_model()

    if not isinstance(input_data, pd.DataFrame):
        input_data = pd.DataFrame(input_data)

    prediction = model.predict(input_data)

    return prediction