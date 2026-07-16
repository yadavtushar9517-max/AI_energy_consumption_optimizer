import streamlit as st
from utils.database_utils import get_predictions
from report import generate_pdf

st.title("📄 Reports")

history = get_predictions()

if history.empty:
    st.info("No data available.")
else:

    csv = history.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download CSV",
        csv,
        "prediction_history.csv",
        "text/csv"
    )

    if st.button("Generate PDF"):

        pdf = generate_pdf(history)

        with open(pdf, "rb") as file:

            st.download_button(
                "📄 Download PDF",
                file,
                "Energy_Report.pdf",
                "application/pdf"
            )