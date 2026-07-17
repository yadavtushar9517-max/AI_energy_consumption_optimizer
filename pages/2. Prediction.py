import streamlit as st
import plotly.express as px

from predict import predict_energy
from utils.database_utils import (
    save_prediction,
    get_predictions
)
from utils.recommendations import generate_recommendation

st.set_page_config(
    page_title="Prediction",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ AI Energy Consumption Prediction")

st.sidebar.header("Prediction Guide")
st.sidebar.info("""
1. Select input values.
2. Click Predict.
3. View prediction.
4. Read AI recommendations.
""")

st.subheader("⚙️ Energy Parameters")

col1, col2 = st.columns(2)

with col1:
    hour = st.slider("Hour", 0, 23, 12)
    temperature = st.slider("Temperature (°C)", 10, 50, 25)
    humidity = st.slider("Humidity (%)", 10, 100, 50)

with col2:
    occupancy = st.slider("Occupancy", 1, 10, 2)
    appliance_usage = st.slider(
        "Appliance Usage (kW)",
        0.0,
        10.0,
        2.0,
        0.1
    )

predict = st.button(
    "🚀 Predict Energy Consumption",
    use_container_width=True
)

if predict:

    prediction = predict_energy(
        hour,
        temperature,
        humidity,
        occupancy,
        appliance_usage
    )

    bill = prediction * 8.5
    carbon = prediction * 0.82

    # Save prediction into database
    save_prediction(
        hour,
        temperature,
        humidity,
        occupancy,
        appliance_usage,
        prediction,
        bill,
        carbon
    )

    st.success("Prediction Saved Successfully!")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "⚡ Energy",
        f"{prediction:.2f} kWh"
    )

    c2.metric(
        "💰 Bill",
        f"₹ {bill:.2f}"
    )

    c3.metric(
        "🌱 CO₂",
        f"{carbon:.2f} kg"
    )

    st.subheader("💡 AI Recommendations")

    recommendations = generate_recommendation(
        prediction,
        temperature,
        occupancy
    )

    for rec in recommendations:
        st.write(f"✅ {rec}")

st.divider()

st.subheader("📜 Prediction History")

history = get_predictions()

if history.empty:
    st.info("No predictions available.")
else:

    st.dataframe(history, use_container_width=True)

    st.subheader("📈 Energy Trend")

    fig = px.line(
        history,
        x="id",
        y="predicted_energy",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("💰 Bill Trend")

    fig2 = px.bar(
        history,
        x="id",
        y="bill"
    )

    st.plotly_chart(fig2, use_container_width=True)