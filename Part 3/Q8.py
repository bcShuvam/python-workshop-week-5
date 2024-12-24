# Part 3
# Q8. Write a Python program to compute the difference between two lists.

# Sample data:
# ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]

# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']

colorList1 = ["red", "orange", "green", "blue", "white"]
colorList2 = ["black", "yellow", "green", "blue"]

print(f'Color1-Color2: {list(set(colorList1) - set(colorList2))}')
print(f'Color1-Color2: {list(set(colorList2) - set(colorList1))}')