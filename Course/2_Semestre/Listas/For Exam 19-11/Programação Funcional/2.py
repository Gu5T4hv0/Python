# def five_char(item):
#         return len(item) > 5
    
# words = ['apple', 'banana', 'kiwi', 'grapefruit', 'orange']

# filter_words = filter(five_char, words)
# filtered_list = list(filter_words)

# print(filtered_list)

    
words = ['apple', 'banana', 'kiwi', 'grapefruit', 'orange']

filter_words = filter(lambda item: len(item) > 5, words)
filtered_list = list(filter_words)

print(filtered_list)