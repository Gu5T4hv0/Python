def count_me(data):
    for id in data:
        if id == "":
            return ""
        elif not id.isnumeric():
            return ""
    dicio = {}
    for i in data:
        if i in dicio:
            dicio[i] += 1
        else:
            dicio[i] = 1
            
    joy = []
    for key, value in dicio.items():
        joy.append(value)
        joy.append(int(key))
        
    result = "".join(map(str, joy))
    return result

        

count_me('1123')
count_me('1')
count_me('11')
count_me('ab')
count_me('a123')
count_me('')
count_me('21')
count_me('1211')