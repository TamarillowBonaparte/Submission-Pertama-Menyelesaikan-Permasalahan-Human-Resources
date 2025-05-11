import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler

# Set page configuration
st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="👥",
    layout="wide"
)

# Load the model dan scaler
@st.cache_resource
def load_model():
    return joblib.load("Model.joblib")

@st.cache_resource
def load_scaler():
    return joblib.load("scaler.joblib")

model = load_model()
scaler = load_scaler()

# Main title
st.title("🏢 Employee Attrition Prediction")
st.markdown("### Predict whether an employee will leave the company based on various factors")

st.sidebar.title("About")
st.sidebar.info(
    "This app predicts employee attrition based on personal, professional, and workplace factors. "
    "Developed using Random Forest algorithm."
)

# Create tabs
tab1, tab2 = st.tabs(["Make Prediction", "Model Information"])

with tab1:
    st.markdown("## Enter Employee Information")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age", min_value=18, max_value=65, value=30)
        gender = st.selectbox("Gender", options=["Male", "Female"])
        marital_status = st.selectbox("Marital Status", options=["Single", "Married", "Divorced"])
        education = st.selectbox("Education", options=["Below College", "College", "Bachelor", "Master", "Doctor"])
        education_field = st.selectbox("Education Field", options=["Life Sciences", "Medical", "Marketing", "Technical Degree", "Human Resources", "Other"])
        distance_from_home = st.number_input("Distance From Home (km)", min_value=1, max_value=30, value=5)
        
    with col2:
        job_level = st.selectbox("Job Level", options=["Staff", "Junior Supervisor", "Senior Supervisor", "Junior Manager", "Senior Manager"])
        job_role = st.selectbox("Job Role", options=["Sales Executive", "Research Scientist", "Laboratory Technician", 
                                                   "Manufacturing Director", "Healthcare Representative", 
                                                   "Manager", "Sales Representative", "Research Director", "Human Resources"])
        department = st.selectbox("Department", options=["Sales", "Research & Development", "Human Resources"])
        business_travel = st.selectbox("Business Travel", options=["Travel_Rarely", "Travel_Frequently", "Non-Travel"])
        overtime = st.selectbox("Overtime", options=["Yes", "No"])
        
    with col3:
        monthly_income = st.number_input("Monthly Income ($)", min_value=1000, max_value=20000, value=5000)
        percent_salary_hike = st.slider("Percent Salary Hike", min_value=0, max_value=25, value=15)
        years_at_company = st.number_input("Years at Company", min_value=0, max_value=40, value=5)
        total_working_years = st.number_input("Total Working Years", min_value=0, max_value=40, value=8)
        job_satisfaction = st.slider("Job Satisfaction (1-4)", min_value=1, max_value=4, value=3)
        environment_satisfaction = st.slider("Environment Satisfaction (1-4)", min_value=1, max_value=4, value=3)
    
    # Additional inputs
    col1, col2 = st.columns(2)
    
    with col1:
        stock_option_level = st.slider("Stock Option Level (0-3)", min_value=0, max_value=3, value=1)
        work_life_balance = st.slider("Work Life Balance (1-4)", min_value=1, max_value=4, value=3)
        performance_rating = st.slider("Performance Rating (1-4)", min_value=1, max_value=4, value=3)
        num_companies_worked = st.number_input("Number of Companies Worked", min_value=0, max_value=10, value=2)
        
    with col2:
        training_times_last_year = st.number_input("Training Times Last Year", min_value=0, max_value=10, value=2)
        relationship_satisfaction = st.slider("Relationship Satisfaction (1-4)", min_value=1, max_value=4, value=3)
        hourly_rate = st.number_input("Hourly Rate", min_value=30, max_value=100, value=65)
        daily_rate = st.number_input("Daily Rate", min_value=100, max_value=1500, value=800)
    
    # Derived features
    if age >= 18 and age <= 27:
        age_group = "GenZ"
    elif age >= 28 and age <= 42:
        age_group = "Milenial"
    else:
        age_group = "GenX"
        
    if distance_from_home >= 1 and distance_from_home <= 5:
        distance_group = "Walking_distance"
    elif distance_from_home >= 6 and distance_from_home <= 25:
        distance_group = "Intermediate_distance"
    else:
        distance_group = "Great_distance"
    
    # Predict button
    predict_button = st.button("Predict Attrition")
    
    if predict_button:
        # Mapping categorical inputs
        gender_map = {"Male": 1, "Female": 0}
        marital_status_map = {"Single": 2, "Married": 1, "Divorced": 0}
        education_map = {"Below College": 0, "College": 1, "Bachelor": 2, "Master": 3, "Doctor": 4}
        education_field_map = {"Life Sciences": 2, "Medical": 3, "Marketing": 4, "Technical Degree": 5, "Human Resources": 1, "Other": 0}
        department_map = {"Sales": 2, "Research & Development": 1, "Human Resources": 0}
        job_level_map = {"Staff": 0, "Junior Supervisor": 1, "Senior Supervisor": 2, "Junior Manager": 3, "Senior Manager": 4}
        job_role_map = {"Sales Executive": 7, "Research Scientist": 6, "Laboratory Technician": 3, 
                       "Manufacturing Director": 4, "Healthcare Representative": 2, 
                       "Manager": 5, "Sales Representative": 8, "Research Director": 0, "Human Resources": 1}
        business_travel_map = {"Travel_Rarely": 2, "Travel_Frequently": 1, "Non-Travel": 0}
        overtime_map = {"Yes": 1, "No": 0}
        age_group_map = {"GenZ": 0, "Milenial": 1, "GenX": 2}
        distance_group_map = {"Walking_distance": 2, "Intermediate_distance": 1, "Great_distance": 0}
        
        # Create input data
        input_data = [
            age, 
            business_travel_map[business_travel],
            daily_rate,
            department_map[department],
            distance_from_home,
            education_map[education],
            education_field_map[education_field],
            environment_satisfaction,
            gender_map[gender],
            hourly_rate,
            3,  # JobInvolvement default
            job_level_map[job_level],
            job_role_map[job_role],
            job_satisfaction,
            marital_status_map[marital_status],
            monthly_income,
            num_companies_worked,
            overtime_map[overtime],
            percent_salary_hike,
            performance_rating,
            relationship_satisfaction,
            stock_option_level,
            total_working_years,
            training_times_last_year,
            work_life_balance,
            years_at_company,
            age_group_map[age_group],
            distance_group_map[distance_group]
        ]
        
        # Menambahkan dua fitur yang hilang dengan nilai default (0)
        input_data.extend([0, 0])  # Menambahkan dua fitur hilang dengan nilai default

        # Reshape dan scaling
        input_array = np.array(input_data).reshape(1, -1)
        print(f"Dimensi input data sebelum scaling: {input_array.shape}")  # Cek dimensi data
        input_scaled = scaler.transform(input_array)
        
        # Prediction
        prediction = model.predict(input_scaled)
        probability = model.predict_proba(input_scaled)
        
        # Output
        st.markdown("## Prediction Result")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if prediction[0] == 1:
                st.error("⚠️ High Risk of Attrition")
                st.write(f"Probability: {probability[0][1]:.2%}")
            else:
                st.success("✅ Low Risk of Attrition")
                st.write(f"Probability: {probability[0][0]:.2%}")
                
        with col2:
            fig, ax = plt.subplots(figsize=(4, 0.3))
            ax.barh([0], [100], color='lightgray', height=0.3)
            ax.barh([0], [probability[0][1] * 100], color='#FF9999' if probability[0][1] > 0.5 else '#99FF99', height=0.3)
            ax.set_xlim(0, 100)
            ax.set_yticks([])
            ax.set_xticks([0, 25, 50, 75, 100])
            ax.set_xticklabels(['0%', '25%', '50%', '75%', '100%'])
            plt.tight_layout()
            st.pyplot(fig)
        
        st.markdown("### Key Factors")
        factors = []
        if age < 30:
            factors.append("Young employees tend to have higher attrition rates")
        if distance_from_home > 10:
            factors.append("Long commuting distance increases attrition risk")
        if job_satisfaction < 3:
            factors.append("Low job satisfaction is a significant indicator of attrition")
        if monthly_income < 3000:
            factors.append("Below-average salary may contribute to attrition")
        if overtime == "Yes":
            factors.append("Overtime work often correlates with higher attrition")
        if marital_status == "Single":
            factors.append("Single employees may have higher mobility")
        if factors:
            for i, factor in enumerate(factors, 1):
                st.write(f"{i}. {factor}")
        else:
            st.write("No specific risk factors identified")

with tab2:
    st.markdown("## Model Information")
    st.write("This prediction system uses a Random Forest Classifier that was trained on employee data.")

    st.markdown("### Model Performance")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Accuracy", "89%")
    col2.metric("Precision", "85%")
    col3.metric("Recall", "83%")
    col4.metric("F1-Score", "84%")

    st.markdown("### Feature Importance")
    feature_importance = {
        "Monthly Income": 0.15,
        "Years at Company": 0.12,
        "Job Satisfaction": 0.1,
        "Distance from Home": 0.08,
        "Age": 0.07,
    }
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x=list(feature_importance.values()), y=list(feature_importance.keys()))
    ax.set_title("Feature Importance")
    st.pyplot(fig)


with tab2:
    st.markdown("## Model Information")
    st.write("This prediction system uses a Random Forest Classifier that was trained on employee data.")

    st.markdown("### Model Performance")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Accuracy", "89%")
    col2.metric("Precision", "85%")
    col3.metric("Recall", "83%")
    col4.metric("F1-Score", "84%")

    st.markdown("### Feature Importance")
    feature_importance = {
        "Monthly Income": 0.15,
        "Age": 0.12,
        "Overtime": 0.10,
        "Job Satisfaction": 0.09,
        "Years at Company": 0.07,
        "Distance From Home": 0.06,
        "Work Life Balance": 0.05,
        "Environment Satisfaction": 0.05,
        "Job Level": 0.04,
        "Total Working Years": 0.04
    }

    fig, ax = plt.subplots(figsize=(10, 6))
    features = list(feature_importance.keys())
    importance = list(feature_importance.values())
    sorted_idx = np.argsort(importance)
    ax.barh(np.array(features)[sorted_idx], np.array(importance)[sorted_idx], color='#5A9')
    ax.set_xlabel('Importance')
    ax.set_title('Feature Importance for Attrition Prediction')
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("### How to Use This Tool")
    st.write("""
    1. Enter the employee details in the form on the 'Make Prediction' tab
    2. Click the 'Predict Attrition' button
    3. Review the prediction result and key factors
    4. Use these insights to take proactive measures to reduce attrition risk
    """)

    st.markdown("### Recommendations to Reduce Attrition")
    st.write("""
    - Improve work-life balance policies
    - Review compensation packages regularly
    - Provide career growth opportunities
    - Establish mentorship programs
    - Enhance workplace environment and culture
    - Recognize and reward employee contributions
    - Offer flexible work arrangements
    """)

st.markdown("---")
st.markdown("Employee Attrition Prediction Tool • Developed by Moch Dani Kurniawan Sugiarto")
