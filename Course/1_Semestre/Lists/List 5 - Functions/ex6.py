# Create a function called "count_occurrences" that gets a list of elements and a specific element as arguments, and returns the number of times that the element appears in the list.
def count_occurrences(list, element):
    counter = 0
    for i in list:
        if element == i:
            counter += 1
        else:
            counter == 0
    return counter

count_occurrences([2, 5, 1, 5, 8, 9, 5], 5)