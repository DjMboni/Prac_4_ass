name_list = []
score_list = []

# Ask for 5 student names and their scores
"""for i in range(5):
    name = input(f"Enter the name of student {i+1}: ")
    score_str = input(f"Enter the score for {name}: ")
    score = float(score_str)  # Convert the score to a floating-point number
    names.append(name)
    scores.append(score)

# Calculate the average score using a while loop
total_score = 0
count = 0
while count < len(scores):
    total_score += scores[count]
    count += 1
average_score = total_score / len(scores)

print(f"The average score is: {average_score:.2f}")
print("Students who scored above average:")

# Print the names of students who scored above average
for i in range(len(names)):
    if scores[i] > average_score:
        print(names[i])"""



i = 0
while i < 5 :
    name = input(f"Enter name of student {i + 1}: ")
    name_list.append(name)
    score = int(input(f"Enter the score of {name}: "))
    score_list.append(score)
    i += 1

total_score = 0
count = 0
while count < len(score_list):
    total_score += score_list[count]
    count += 1

print("Students who scored above average:")
average_score = total_score / len(score_list)
for i in range(len(name_list)):
    if score_list[i] > average_score:
        print(name_list[i])







