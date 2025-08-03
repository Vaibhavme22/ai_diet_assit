import pandas as pd

def calculate_calories(age, gender, weight, height, activity):
    """Calculate daily calorie requirement using Mifflin-St Jeor Equation."""
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_factor = {
        'Sedentary': 1.2,
        'Light': 1.375,
        'Moderate': 1.55,
        'Active': 1.725
    }

    return round(bmr * activity_factor[activity], 2)

def recommend_meals(calories_needed, diet_type, food_file="foods.csv"):
    """Recommend meals based on calorie needs and diet type."""
    df = pd.read_csv(food_file)
    if diet_type.lower() == "veg":
        df = df[df["Type"] == "Veg"]
    
    df_sorted = df.sort_values(by="Calories")
    total = 0
    plan = []

    for _, row in df_sorted.iterrows():
        if total + row["Calories"] <= calories_needed:
            plan.append(row["Food"])
            total += row["Calories"]
    

    return plan
