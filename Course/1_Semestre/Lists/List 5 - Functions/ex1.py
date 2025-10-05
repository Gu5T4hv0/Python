#Create a function called "greater_number" that receives a list of numbers as argument and returns the largest number of the list.
def greater_number(numbers: list) -> int:
    numbers.sort()
    last_number = numbers[-1]
    return last_number
    
greater_number([5, 8, 35, 93, 6, 3])