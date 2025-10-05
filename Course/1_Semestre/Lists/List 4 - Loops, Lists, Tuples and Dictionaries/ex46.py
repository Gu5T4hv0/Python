# Create a dictionary with countries and capitals. Let the user type the country and display the capital.
capitals = {"USA": "Washington D.C.",
            "China": "Beijing",
            "Brazil": "Brasília",
            "Índia": "New Delhi"}

country = input("Type a country: ")

if country in capitals:
    print(f"The capital of {country} is {capitals[country]}.")
else:
    print("This country is not found in our dictionary.")