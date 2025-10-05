name  = 'Dimitri'
split = name.split()
first_name = split[0]
if len(split) == 1:
        print(first_name)
last_name = split[-1]
middle_names = split[1:-1]
initialize = [split[0] + '.' for split in middle_names]
if initialize:
    print(f"{first_name} {' '.join(initialize)} {last_name}")
else:
    print(f"{first_name} {last_name}")