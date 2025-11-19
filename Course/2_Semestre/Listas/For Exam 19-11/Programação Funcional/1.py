def conversion(celsius):
    return celsius * 9/5 + 32

numbers = [1,2,3,4,5]

conversion_map_object = map(conversion, numbers)

converted_list = list(conversion_map_object)

print(converted_list)