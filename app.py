import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("decision_tree_model.pkl")

# Configure the page
st.set_page_config(page_title="🎓 Student Pass/Fail Predictor", layout="centered")

# Title and description
st.title("🎓 Student Pass/Fail Predictor")
st.markdown("Predict whether a student is likely to **Pass** or **Fail** based on their habits and background.")

# Input form
with st.form("prediction_form"):
    st.subheader("📋 Enter Student Information:")

    col1, col2 = st.columns(2)

    with col1:
        parent_edu = st.selectbox("👨‍🏫 Parent Education Level", [1, 2, 3, 4, 5], help="1 = No formal education, 5 = Postgraduate")
        academic_stress = st.slider("📊 Academic Stress Level (1 = Low, 10 = High)", 1, 10, 5)
        attendance_rate = st.slider("🏫 Attendance Rate (%)", 0, 100, 80)
        assignment_completion = st.slider("📝 Assignment Completion Rate (%)", 0, 100, 85)

    with col2:
        sleep_hours = st.slider("😴 Hours of Sleep per Night", 0, 12, 6)
        study_hours = st.slider("📖 Hours of Study Outside School", 0, 10, 2)
        social_media_hours = st.slider("📱 Social Media Hours per Day", 0, 10, 3)

    submitted = st.form_submit_button("🔍 Predict")

# Make prediction
if submitted:
    input_data = pd.DataFrame({
        'parent_education_level': [parent_edu],
        'academic_stress': [academic_stress],
        'attendance_rate': [attendance_rate],
        'assignment_completion_rate': [assignment_completion],
        'sleep_hours': [sleep_hours],
        'social_media_hours': [social_media_hours],
        'study_hours': [study_hours]
    })

    prediction = model.predict(input_data)[0]
    result = "✅ Pass" if prediction == 0 else "❌ Fail"

    st.markdown("### 🎯 Prediction Result:")
    st.success(f"**{result}**")
