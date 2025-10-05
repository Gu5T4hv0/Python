# Create a function called "order_list" that takes a list of numbers as an argument and returns a new list containing the same numbers, but ordered in ascending order.
def order_list(list: list) -> list:
    list.sort()
    return list

order_list([37, 5, 92, 14, 100, 46])