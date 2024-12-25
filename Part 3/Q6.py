# Part 3
# Q6. You are a teacher and you have a list of dictionaries containing 
# information about your students. Each dictionary represents a single 
# student and contains the following keys: "name", "age", "gender", 
# and "grades". The "grades" key points to a list of grades the student 
# has received in different subjects. Your task is to write a 
# Python program that calculates the average grade for each student 
# and prints out their name and average grade.
# Here's an example of list of dictionaries to get you started:

# students = [
    # {"name": "Alice", "age": 17, "gender": "female", "grades": [90, 85, 95]},
    # {"name": "Bob", "age": 16, "gender": "male", "grades": [80, 75, 70]},
    # {"name": "Charlie", "age": 16, "gender": "male", "grades": [100, 90, 95]},
    # {"name": "Diana", "age": 17, "gender": "female", "grades": [85, 80, 90]},
    # {"name": "Emily", "age": 16, "gender": "female", "grades": [95, 90, 100]}
# ]

# Your program should produce the following output:
# Alice: 90.0
# Bob: 75.0
# Charlie: 95.0
# Diana: 85.0
# Emily: 95.0
# Hint: You'll need to use nested loops to iterate over the 
# list of dictionaries and the list of grades for each student. 
# You can use the len() function to get the number of grades 
# for each student.

students = [
    {"name": "Alice", "age": 17, "gender": "female", "grades": [90, 85, 95]},
    {"name": "Bob", "age": 16, "gender": "male", "grades": [80, 75, 70]},
    {"name": "Charlie", "age": 16, "gender": "male", "grades": [100, 90, 95]},
    {"name": "Diana", "age": 17, "gender": "female", "grades": [85, 80, 90]},
    {"name": "Emily", "age": 16, "gender": "female", "grades": [95, 90, 100]}
]

for student in students:
    total_grade = 0
    for grade in student["grades"]:
        total_grade += grade
    average_grade = total_grade / len(student["grades"])
    print(f"{student['name']}: {average_grade:.1f}")