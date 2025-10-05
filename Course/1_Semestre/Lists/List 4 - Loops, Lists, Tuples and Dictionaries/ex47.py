# Change the age of a person in a dictionary from a user input.
ages = {
    'Arthur': 19,
    'Gabriel': 24,
    'Luis': 26,
    'Tiago': 21
}

print(ages)
name = input("Type the name of the guy that you think the age is wrong: ")
age = int(input("Type the age you think is the correct: "))

cap_name = name.capitalize()
ages[cap_name] = age

print(ages)