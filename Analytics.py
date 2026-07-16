import streamlit as st
import plotly.express as px
from utils.database_utils import get_predictions

st.title("📊 Analytics")

history = get_predictions()

if history.empty:
    st.info("No data available.")
else:

    fig = px.line(
        history,
        x="id",
        y="predicted_energy",
        markers=True,
        title="Energy Prediction Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.bar(
        history,
        x="id",
        y="bill",
        title="Electricity Bill Trend"
    )

    st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.area(
        history,
        x="id",
        y="carbon",
        title="Carbon Emission"
    )

    st.plotly_chart(fig3, use_container_width=True)