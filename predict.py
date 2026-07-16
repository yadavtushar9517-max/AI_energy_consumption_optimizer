import joblib
import pandas as pd

model = joblib.load("models/energy_model.pkl")

FEATURES = [
    "hour",
    "temperature",
    "humidity",
    "occupancy",
    "appliance_usage"
]

def predict_energy(hour, temperature, humidity, occupancy, appliance_usage):

    data = pd.DataFrame({
        "hour": [hour],
        "temperature": [temperature],
        "humidity": [humidity],
        "occupancy": [occupancy],
        "appliance_usage": [appliance_usage]
    })

    prediction = model.predict(data)

    return round(prediction[0], 2)


def predict_batch(df):

    predictions = model.predict(df[FEATURES])

    df = df.copy()

    df["Predicted Energy"] = predictions

    df["Estimated Bill"] = df["Predicted Energy"] * 8.5

    df["CO₂ Emission"] = df["Predicted Energy"] * 0.82

    return df