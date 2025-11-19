import numpy as np

# Student Score Data:
# [Midterm_1, Final_1, Midterm_2, Final_2, Midterm_3, Final_3, Midterm_4, Final_4]
score_data = [80, 95, 75, 85, 90, 80, 65, 70]

gradebook = np.array(score_data).reshape(4,2)
print(gradebook)
midterm_scores = gradebook[:,0]
print(midterm_scores)
final_scores = gradebook[:,1]
print(final_scores)
mean = np.mean(final_scores)
print(mean)
total_scores = midterm_scores + final_scores
print(total_scores)