# Task 1: Extract the temperatures for the second week from the given list
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week = temperatures[7:14]

print(f"The temperatures for the second week are: {second_week}")

# Task 2: Extract all the temperatures above 100
extreme_heat = []

for temperature in temperatures:
    if temperature > 100:
        extreme_heat.append(temperature)
    else:
        continue

print(f"The temperatures for the month above 100 are: {extreme_heat}")