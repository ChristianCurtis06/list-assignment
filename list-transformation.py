# Task 1: Sort the given list of grades in descending order and print the sorted list
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()

print(f"The list of grades in descending order is: {grades}")

# Task 2: Calculate the average grade and print it
average_grade = (grades[0] + grades[1] + grades[2] + grades[3] + grades[4] + grades[5] + grades[6] + grades[7] + grades[8] + grades[9]) / len(grades)

print(f"The average grade is: {average_grade}")