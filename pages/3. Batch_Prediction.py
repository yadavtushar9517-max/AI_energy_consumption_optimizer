import streamlit as st
import pandas as pd
from predict import predict_batch

st.set_page_config(
    page_title="Batch Prediction",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Batch Energy Prediction")

st.write("Upload a CSV file to predict energy consumption for multiple records.")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        st.subheader("📄 Uploaded Dataset")
        st.dataframe(df, use_container_width=True)

        if st.button("🚀 Predict All Records"):

            result = predict_batch(df)

            st.success("✅ Prediction Completed Successfully!")

            st.subheader("📊 Prediction Results")
            st.dataframe(result, use_container_width=True)

            csv = result.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="📥 Download Results",
                data=csv,
                file_name="Batch_Predictions.csv",
                mime="text/csv"
            )

    except Exception as e:
        st.error(str(e))