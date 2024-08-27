# Task 1: Find out if Alice submitted the assignment and attended class using the given lists
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in submitted and "Alice" in attended:
    print("Alice both submitted the assignment and attended class!")
elif "Alice" in submitted and "Alice" not in attended:
    print("Alice submitted the assignment, but she did not attend class.")
elif "Alice" not in submitted and "Alice" in attended:
    print("Alice did not submit the assignment, but she attended class.")
else:
    print("Alice neither submitted the assignment nor attended class.")