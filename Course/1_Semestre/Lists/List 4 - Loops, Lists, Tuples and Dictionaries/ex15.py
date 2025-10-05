# Generate the first 20 numbers of the Fibonacci sequence.
a, b = 0, 1
print("Fibonacci Sequence")
for i in range(20):
    print(a, end=' ')
    a, b = b, a + b