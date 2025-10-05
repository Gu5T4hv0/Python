def count_me(data):
    count = 0
    new = []
    for i in data:
        if i.isalpha():
            print(f"{i}")
        else:
            if i == "2":
                new.append("12")
            elif i == "3":
                new.append("13")
            elif i == "1":
                new.append("11")
    count = 0
    for number in new:
        if number == "11":
            count += 1
            if count == 2:
                new.remove(number)
                new.remove(number)
                new.append("21")
                
    print(new, count)

count_me('1123')
count_me('1')
count_me('11')
count_me('ab')
count_me('a123')
count_me('')
count_me('21')
count_me('1211')