# Given a tuple with grades, calculate the average and inform if the student is passed (average >= 6).
grades = (4.5, 2.6, 7.8, 10, 9)

average = sum(grades) / len(grades)

if average >= 6:
    print("Approved")
else:
    print("Disapproved")