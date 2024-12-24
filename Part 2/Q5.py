# Part 2
# Q5. Write a Python program to create a dictionary of student names 
# and their corresponding ages, and 
# then print the age of a specific student

# students = [
#     {'name': 'John', 'age': 13},
#     {'name': 'Alice', 'age': 15},
#     {'name': 'Mike', 'age': 19}
# ]
students = {
    "Alice": 20,
    "Bob": 22,
    "Charlie": 21,
    "David": 23,
    "Eve": 19
}
print(f'Available students = {list(students.keys())}')
studName = input('Enter the name of the student : ')
if studName in students:
    print(f'{studName}\'s age is {students[studName]}')
else:
    print(f'Student with name "{studName}" is not available')