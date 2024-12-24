# Part 3
# Q3. Write a Python program that takes in a list of dictionaries 
# representing people with their age, and 
# returns a new list of dictionaries with only 
# the people over the age of 18

people = [
    {'name': 'John', 'age': 25},
    {'name': 'Alice', 'age': 17},
    {'name': 'Bob', 'age': 30},
    {'name': 'Emily', 'age': 15},
    {'name': 'Michael', 'age': 35},
    {'name': 'Sophia', 'age': 18},
    {'name': 'David', 'age': 27}
]

peopleOver18 = [person for person in people if person['age'] > 18]
print(f'People with age over 18 are:')
for people in peopleOver18:
    print(people)