# Read 3 names and store them in one tuple. Check if a specific name is in the tuple.
name_1 = 'Layla'
name_2 = 'Omar'
name_3 = 'Yasmin'
tuple = (name_1, name_2, name_3)

name = input("Type an arabic name that you think is in the tuple: ")

capitalized_name = name.capitalize()
if capitalized_name in tuple:
    print(f'You nailed the name! Your name is in the index {tuple.index(capitalized_name)} in the tuple')
else:
    print('Your name is not found in my tuple.')