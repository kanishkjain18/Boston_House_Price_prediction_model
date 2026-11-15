
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("Random_Forest.pkl")

# Page configuration
st.set_page_config(
    page_title="Boston House Price Predictor",
    page_icon="🏡",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #101827, #172b46);
    color: white;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #ffffff;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: #b8c7dc;
    font-size: 17px;
    margin-bottom: 30px;
}

.section-title {
    font-size: 22px;
    font-weight: 700;
    color: #7dd3fc;
    margin-top: 15px;
}

.result-card {
    background: linear-gradient(120deg, #075985, #2563eb);
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    color: white;
    margin-top: 25px;
}

.result-label {
    font-size: 18px;
    color: #dbeafe;
}

.result-value {
    font-size: 38px;
    font-weight: 800;
    color: white;
}

div.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #0284c7, #2563eb);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px;
    font-size: 18px;
    font-weight: bold;
}

div.stButton > button:hover {
    background: #0369a1;
    color: white;
    border: none;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    st.title("🏡 House Predictor")
    st.write("Machine Learning Project")
    st.divider()

    st.markdown("### About Project")
    st.write(
        "This application predicts Boston house prices "
        "using a trained Random Forest Regression model."
    )

    st.divider()
    st.markdown("### Model Information")
    st.write("**Algorithm:** Random Forest")
    st.write("**Task:** Regression")
    st.write("**Dataset:** Boston Housing")

    st.divider()
    st.caption("Developed by Kanishk Jain")


# Main heading
st.markdown(
    '<div class="main-title">Boston House Price Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Enter property details to estimate the house price</div>',
    unsafe_allow_html=True
)

st.divider()

# Input sections
st.markdown('<div class="section-title">🏠 Property Details</div>',
            unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    indus = st.number_input("INDUS", min_value=0.0, value=5.0)
    nox = st.number_input("NOX", min_value=0.0, value=0.5)
    rm = st.number_input("RM (Average Rooms)", min_value=0.0, value=6.0)
    age = st.number_input("AGE", min_value=0.0, max_value=100.0, value=60.0)

with col2:
    dis = st.number_input("DIS", min_value=0.0, value=4.0)
    rad = st.number_input("RAD", min_value=0, value=4)
    tax = st.number_input("TAX", min_value=0, value=300)
    ptratio = st.number_input("PTRATIO", min_value=0.0, value=18.0)

with col3:
    lstat = st.number_input("LSTAT", min_value=0.0, value=12.0)
    chas = st.selectbox("CHAS (Charles River)", [0, 1])

st.divider()

# Prediction
if st.button("✨ Predict House Price"):

    input_data = pd.DataFrame([{
        "indus": indus,
        "chas": chas,
        "nox": nox,
        "rm": rm,
        "age": age,
        "dis": dis,
        "rad": rad,
        "tax": tax,
        "ptratio": ptratio,
        "lstat": lstat
    }])

    prediction = model.predict(input_data)[0]

    st.markdown(f"""
    <div class="result-card">
        <div class="result-label">Estimated House Price</div>
        <div class="result-value">${prediction:.2f}K</div>
        <p>Predicted using Random Forest Regression</p>
    </div>
    """, unsafe_allow_html=True)


# Footer
st.divider()
st.markdown(
    "<center style='color:#9ca3af;'>Developed by <b>Kanishk Jain</b> | Boston House Price Prediction</center>",
    unsafe_allow_html=True
)
