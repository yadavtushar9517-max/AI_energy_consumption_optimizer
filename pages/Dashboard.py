import streamlit as st
import plotly.express as px
from utils.database_utils import get_predictions

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard")

history = get_predictions()

if history.empty:
    st.warning("No prediction data available.")
else:

    # ================= KPI Cards =================
    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Predictions",
        len(history)
    )

    c2.metric(
        "Average Energy",
        f"{history['predicted_energy'].mean():.2f} kWh"
    )

    c3.metric(
        "Average Bill",
        f"₹ {history['bill'].mean():.2f}"
    )

    c4.metric(
        "Maximum Energy",
        f"{history['predicted_energy'].max():.2f} kWh"
    )

    st.divider()

    # ================= Charts =================

    left, right = st.columns(2)

    with left:

        fig = px.line(
            history,
            x="id",
            y="predicted_energy",
            markers=True,
            title="Energy Consumption Trend"
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:

        fig2 = px.bar(
            history,
            x="id",
            y="bill",
            title="Electricity Bill"
        )

        st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    st.subheader("Recent Predictions")

    st.dataframe(
        history.tail(10),
        use_container_width=True
    )