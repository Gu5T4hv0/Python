# Read 3 names and store them in one tuple. Check if a specific name is in the tuple.
tuple = ('Layla', 'Omar', 'Yasmin')

name = input("Type an arabic name that you think is in the tuple: ")

capitalized_name = name.capitalize()
if capitalized_name in tuple:
    print(f'You nailed the name! Your name is in the index {tuple.index(capitalized_name)} in the tuple')
else:
    print('Your name is not found in my tuple.')