# Create a dictionary with 5 students and their grades. Then, display the overall class average.
grades = {
    "Alisson": 4.3,
    "George": 7.5,
    "Fernand": 10.0,
    "Sara": 3.0,
    "Veronica": 5.0
}

sum = sum(grades.values())
quantity = len(grades)
average = sum/quantity

print(f"The general average of the class is: {average:.2f}")