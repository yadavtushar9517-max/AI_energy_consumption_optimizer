import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("dataset/energy_data.csv")

# Features
X = df[[
    "hour",
    "temperature",
    "humidity",
    "occupancy",
    "appliance_usage"
]]

# Target
y = df["energy_consumption"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model Trained Successfully")
print("MAE :", round(mae,3))
print("R2 Score :", round(r2,3))

# Save model
joblib.dump(model, "models/energy_model.pkl")

print("Model saved to models/energy_model.pkl")