# Create a function that receives weight (kg) and height (m) and calculate the BMI:
def calculate_BMI(weight, height):
    bmi = weight/height**2
    print(f"{bmi:.2f}")
calculate_BMI(80, 1.80)
