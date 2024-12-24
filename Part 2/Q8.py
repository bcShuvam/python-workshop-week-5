# Part 2
# Q8. Write a Python program to check if a specific key 
# and a value exist in a dictionary.

# students=[
#     {"student_id": 1, "name": "Jean Castro", "class": "V"},
#     {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
#     {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
#     {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
#     {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
# ]
# Your output should as follows:
# Key: 'name' and Value: 'Jean Castro' do exist
# Key: 'address' and Value: 'New York' do not exist

students=[
    {"student_id": 1, "name": "Jean Castro", "class": "V"},
    {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
    {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
    {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
    {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
]

inputKey = input('Enter key : ')
inputValue = input('Enter value : ')
valueMatched = False
keyMatched = False
for i in range(len(students)):
    if inputKey in students[i].keys():
        keyMatched = True
        if students[i][inputKey] == inputValue:
            valueMatched = True
            break
        else:
            valueMatched = False
            continue
    else:
        keyMatched = False
        break

if not keyMatched:
    print(f'Key: "{inputKey}" and Value: "{inputValue}" do not exist')
else:
    if valueMatched:
        print(f'Key: "{inputKey}" and Value: "{inputValue}" do exist')
    else:
        print(f'Key: "{inputKey}" exists but Value: "{inputValue}" do not exist')