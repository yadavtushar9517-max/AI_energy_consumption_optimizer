import streamlit as st
from database import create_database

create_database()

st.set_page_config(
    page_title="AI Energy Consumption Optimizer",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ AI-Based Energy Consumption Optimization")

st.markdown("""
## Welcome 👋

This application uses **Machine Learning** to predict energy consumption,
estimate electricity bills, calculate carbon emissions, and provide
AI-powered energy-saving recommendations.

---

### 🚀 Features

✅ Energy Consumption Prediction

✅ Electricity Bill Estimation

✅ Carbon Emission Analysis

✅ AI Recommendations

✅ Interactive Dashboard

✅ Analytics

✅ Report Generation

---

### 📌 How to Use

1. Open **Prediction** from the sidebar.
2. Enter energy parameters.
3. Click **Predict**.
4. View recommendations.
5. Check Dashboard and Analytics.
6. Download reports.

---

### 🛠 Technology Stack

- Python
- Streamlit
- Scikit-Learn
- SQLite
- Plotly
- Pandas
- NumPy

---

### 👈 Use the sidebar to navigate between pages.
""")

st.info("Select a page from the left sidebar to begin.")