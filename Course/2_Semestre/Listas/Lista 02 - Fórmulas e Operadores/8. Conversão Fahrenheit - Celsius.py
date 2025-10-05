# Create a function that receives a temperature in Fahrenheit and converts it to Celsius:
def fahrenheit_to_celsius(f):
    c = (f - 32)* 5/9
    print(f"{c:.2f}°C")
    return c
fahrenheit_to_celsius(170)