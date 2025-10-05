# Simulate a countdown from 10 to 0.
storage = []
for i in range(11):
    storage.append(i)
    storage.sort(reverse=True)
    
print(storage)