students = {
    'John': [6.5, 7.0, 10],
    'Albert': [9.5, 3.0, 7.8],
    'Tyler': [4.5, 2.4, 6.8]
}

for name, grades in students.items():
    average = sum(grades)/len(grades)
    print(f"{name}'s average is {average:.2f}")
# John = students['John']

# average_john = sum(John)/len(John)
# print(f"{average_john:.2f}")


# Albert = students['Albert']

# average_albert = sum(Albert)/len(Albert)
# print(f"{average_albert:.2f}")


# Tyler = students['Tyler']

# average_tyler = sum(Tyler)/len(Tyler)
# print(f"{average_tyler:.2f}")