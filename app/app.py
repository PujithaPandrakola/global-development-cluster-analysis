import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ============================================
# Page Configuration
# ============================================

st.set_page_config(
    page_title="Global Development Cluster Analysis",
    layout="wide"
)

# ============================================
# Load Model and Scaler
# ============================================

model = joblib.load('models/kmeans_model.pkl')
scaler = joblib.load('models/scaler.pkl')

# ============================================
# Title
# ============================================

st.title("🌍 Global Development Cluster Analysis")

st.markdown("""
This application predicts the development cluster of a country 
based on economic and development indicators using Machine Learning Clustering.
""")

st.divider()

# ============================================
# Sidebar
# ============================================

st.sidebar.header("Enter Country Development Details")

# ============================================
# Input Fields
# ============================================

birth_rate = st.sidebar.number_input(
    "Birth Rate",
    min_value=0.0,
    max_value=1.0,
    value=0.02
)

co2 = st.sidebar.number_input(
    "CO2 Emissions",
    min_value=0.0,
    value=50000.0
)

days_business = st.sidebar.number_input(
    "Days to Start Business",
    min_value=0.0,
    value=30.0
)

energy_usage = st.sidebar.number_input(
    "Energy Usage",
    min_value=0.0,
    value=100000.0
)

health_exp = st.sidebar.number_input(
    "Health Expenditure % GDP",
    min_value=0.0,
    max_value=1.0,
    value=0.06
)

infant_mortality = st.sidebar.number_input(
    "Infant Mortality Rate",
    min_value=0.0,
    max_value=1.0,
    value=0.03
)

internet_usage = st.sidebar.number_input(
    "Internet Usage",
    min_value=0.0,
    max_value=1.0,
    value=0.30
)

lending_interest = st.sidebar.number_input(
    "Lending Interest",
    min_value=0.0,
    value=0.10
)

life_exp_female = st.sidebar.number_input(
    "Life Expectancy Female",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

life_exp_male = st.sidebar.number_input(
    "Life Expectancy Male",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

mobile_usage = st.sidebar.number_input(
    "Mobile Phone Usage",
    min_value=0.0,
    value=1.0
)

pop_0_14 = st.sidebar.number_input(
    "Population 0-14",
    min_value=0.0,
    max_value=1.0,
    value=0.30
)

pop_15_64 = st.sidebar.number_input(
    "Population 15-64",
    min_value=0.0,
    max_value=1.0,
    value=0.60
)

pop_65 = st.sidebar.number_input(
    "Population 65+",
    min_value=0.0,
    max_value=1.0,
    value=0.10
)

population_total = st.sidebar.number_input(
    "Population Total",
    min_value=0.0,
    value=10000000.0
)

population_urban = st.sidebar.number_input(
    "Population Urban",
    min_value=0.0,
    max_value=1.0,
    value=0.50
)

# ============================================
# Input DataFrame
# ============================================

input_data = pd.DataFrame([[
    birth_rate,
    co2,
    days_business,
    energy_usage,
    health_exp,
    infant_mortality,
    internet_usage,
    lending_interest,
    life_exp_female,
    life_exp_male,
    mobile_usage,
    pop_0_14,
    pop_15_64,
    pop_65,
    population_total,
    population_urban
]], columns=[
    'Birth Rate',
    'CO2 Emissions',
    'Days to Start Business',
    'Energy Usage',
    'Health Exp % GDP',
    'Infant Mortality Rate',
    'Internet Usage',
    'Lending Interest',
    'Life Expectancy Female',
    'Life Expectancy Male',
    'Mobile Phone Usage',
    'Population 0-14',
    'Population 15-64',
    'Population 65+',
    'Population Total',
    'Population Urban'
])

# ============================================
# Prediction
# ============================================

if st.button("Predict Cluster"):

    # Scale data
    scaled_input = scaler.transform(input_data)

    # Predict cluster
    cluster = model.predict(scaled_input)[0]

    st.success(f"Predicted Cluster: {cluster}")

    # ============================================
    # Cluster Interpretation
    # ============================================

    if cluster == 0:
        st.info("🌱 Emerging Economy Cluster")

    elif cluster == 1:
        st.info("🏆 Developed Country Cluster")

    elif cluster == 2:
        st.info("⚠️ Underdeveloped Country Cluster")

    elif cluster == 3:
        st.info("📈 Developing Country Cluster")

    else:
        st.info("🏭 Industrial High Population Economy Cluster")

    # ============================================
    # Show Input Summary
    # ============================================

    st.subheader("Input Summary")

    st.dataframe(input_data)