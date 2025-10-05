# Make a program that reads the name of 3 products and their prices, storing in the dictionary.
thisdict = {

}
for i in range(3):
    product = input("Type a product: ")
    price = int(input("Type a price: "))
    thisdict.update({product: price})

print(thisdict)
