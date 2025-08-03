import streamlit as st
from diet_logic import calculate_calories, recommend_meals

st.set_page_config(page_title="AI Diet Assistant")

st.title("🥗 AI Diet Assistant")

st.markdown("Get your personalized diet plan based on your health goals.")

# User Inputs
age = st.number_input("Enter your age", min_value=10, max_value=100)
weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0)
height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0)
gender = st.selectbox("Gender", ["Male", "Female"])
activity = st.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "Active"])
goal = st.selectbox("Your Goal", ["Weight Loss", "Maintenance", "Weight Gain"])
diet_type = st.selectbox("Diet Preference", ["Veg", "Non-Veg"])

if st.button("Get My Diet Plan"):
    calories = calculate_calories(age, gender, weight, height, activity)
    
    # Adjust based on goal
    if goal == "Weight Loss":
        calories -= 300
    elif goal == "Weight Gain":
        calories += 300

    st.success(f"Your recommended daily calorie intake is: {calories} kcal")

    meal_plan = recommend_meals(calories, diet_type)
    st.subheader("Recommended Meals:")
    for item in meal_plan:
        st.markdown(f"✅ {item}")