# Write a program that counts how many numbers between 1 and 100 are even.
list = []
for i in range(1, 101):
    if i % 2 == 0:
        list.append(i)
print(len(list))