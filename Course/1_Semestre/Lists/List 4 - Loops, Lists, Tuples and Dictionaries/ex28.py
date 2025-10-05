# Read a list of 10 names and remove a name typed by the user.
name = input("Tell me a name among \"Ana\", \"Bernard\", \"Cesar\", \"Donald\" to remove from the list: ")

list = ["Ana", "Bernard", "Cesar", "Donald", "Edward", "Frank", "George", "Henry", "Isaac", "Jack"]
if name not in list:
    print("Aw come on, don't give me a name not present in this list that I gave to you!")
else:
    remove_name = list.remove(name)

    print(list)