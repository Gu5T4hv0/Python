# Create a function called "calculate_average" that receives a list of numbers as argument and returns the average arithmetic of the elements.
def calculate_average(numbers: list) -> int:
    avg = sum(numbers)/len(numbers)
    return avg
    
calculate_average([5, 6, 2, 9, 3])