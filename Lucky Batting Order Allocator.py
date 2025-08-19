import random

# Step 1: Ask user for number of names
n = int(input("Enter how many names: "))

# Step 2: Get names from user
names = []
for i in range(n):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

# Step 3: Create unique random numbers from 1 to n
numbers = list(range(1, n+1))
random.shuffle(numbers)  # shuffle to make them random

# Step 4: Assign each name one unique number
for i in range(n):
    print(names[i], "→", numbers[i])
