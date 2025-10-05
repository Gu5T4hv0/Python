# Create a function called "find_primes" that takes a positive integer as an argument and returns a list with all prime numbers smaller than or equal to the given number.
def find_primes(n):
    if n < 2:
        return []

    sequence = list(range(2, n + 1))

    for num in sequence:
        for multiple in range(num * 2, n + 1, num):
            if multiple in sequence:
                sequence.remove(multiple)
    
    return sequence

print(find_primes(30))