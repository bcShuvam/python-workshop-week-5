# Part 3
# Q4. Write a program to input your friend’s names and 
# their Phone Numbers and store them in the dictionary as the key-value pair. 
# Perform the following operations on the dictionary:

friendList = [] # declaring and initializing an empty list

# Input friends name and phone number
while True: # infinite while loop
    print('\nPress Enter to exit the program.')
    name = input('Enter your friend\'s name: ')
    if name == '': # if name is empty then exit while loop
        print() # for new line
        break
    phoneNum = input('Enter your friend\'s phone number: ')
    if phoneNum == '': # if phoneNum is empty then exit while loop
        print() # for new line
        break

    # Create a object model for friend
    friendDetail = {
        'name': name,
        'phoneNum': phoneNum,
    }
    friendList.append(friendDetail) # adding friendDetail to friendList
    print(f'"{friendDetail['name']}" added successfully to friend list')

# a) Display the name and phone number of all your friends.
print('**********************************************************************************')
print('Friends List:')
for friend in friendList:
    print(f'Original: {friend}')
print('**********************************************************************************\n')

# b) Add a new key in this dictionary and display the modified dictionary
print('**********************************************************************************')
while True:
    newKey = input('Enter name of new Key: ')
    if newKey == '':
        print('Key name cannot be empty')
    elif newKey in friendList[0]:
        print(f'Key "{newKey}" already exists')
    else:
        break
defaultValue = input(f'Enter default value for {newKey}: ')
print('Friends List with new key:')
for friend in friendList:
    # newKeyValue = [friend['name'], friend['phoneNum']]
    friend[newKey] = defaultValue
    print(f'Modified: {friend}')
print('**********************************************************************************\n')

# c) Delete the particular friend from the dictionary
print('**********************************************************************************')
while True:
    print('Enter a friend name form friend list to delete')
    print('Or Press Enter to skip')
    deleteFriendByName = input('Friend name: ')
    friendDeleted = False
    if deleteFriendByName == '':
        print('Delete friend step skipped successfully\n')
        break
    for friend in friendList:
        if deleteFriendByName == friend['name']:
            friendList.remove(friend)
            friendDeleted = True
            break
    if friendDeleted:
        print(f'"{deleteFriendByName}" deleted from friend list\n')
    else:
        print(f'{deleteFriendByName} not found in friend list\n')
print('**********************************************************************************\n')

# d) Modify the phone number of an existing friend
while True:
    print('Select the given number as shown to modify a friend')
    for i in range(len(friendList)):
        print(f'Press {i} for {friendList[i]}')
    selectedFriend = input('Select a friend or Press Enter to skip: ')
    if selectedFriend == '':
        break
    if not selectedFriend.isdigit():
        print('Invalid input.')
        continue
    selectedFriend = int(selectedFriend)
    if selectedFriend < len(friendList):
        while True:
            print('Press Enter to skip')
            newPhoneNum = input(f'Enter new phone number for {friendList[selectedFriend]['name']}: ')
            if newPhoneNum == '':
                print("Phone number update skipped.\n")
                break
            else:
                friendList[selectedFriend]['phoneNum'] = newPhoneNum
                print(f"Phone number for {friendList[selectedFriend]['name']} updated successfully.\n")
                break
print()
for friend in friendList:
    print(f'Deleted Friend List: {friend}')
print()

# e) Check if a friend is present in the dictionary or not and 
#    display it in sorted form.
while True:
    print('Enter a friend name to check if it exists in friend list or not')
    print('Or Press Enter to skip')
    checkFriendByName = input('Friend name: ')
    if checkFriendByName == '':
        break
    for friend in friendList:
        if checkFriendByName == friend['name']:
            print(f'"{checkFriendByName}" found in friend list\n')
            break
    else:
        print(f'"{checkFriendByName}" not found in friend list\n')
print('Program exited successfully!')


# dean4@DESKTOP-UEPI2CG MINGW64 /d/BIC/Python/Week 5/Part 3 (main)
# $ python Q4.py 

# Press Enter to exit the program.
# Enter your friend's name: ram
# Enter your friend's phone number: 9874105263
# "ram" added successfully to friend list

# Press Enter to exit the program.
# Enter your friend's name: hari
# Enter your friend's phone number: 9812345670 
# "hari" added successfully to friend list

# Press Enter to exit the program.
# Enter your friend's name: suresh
# Enter your friend's phone number: 9876543210
# "suresh" added successfully to friend list

# Press Enter to exit the program.
# Enter your friend's name:

# ********************************************************************************
# Friends List:
# Original: {'name': 'ram', 'phoneNum': '9874105263'}
# Original: {'name': 'hari', 'phoneNum': '9812345670'}
# Original: {'name': 'suresh', 'phoneNum': '9876543210'}
# ********************************************************************************

# ********************************************************************************
# Enter name of new Key: k
# Enter default value for k: v
# Friends List with new key:
# Modified: {'name': 'ram', 'phoneNum': '9874105263', 'k': 'v'}
# Modified: {'name': 'hari', 'phoneNum': '9812345670', 'k': 'v'}
# Modified: {'name': 'suresh', 'phoneNum': '9876543210', 'k': 'v'}
# ********************************************************************************

# ********************************************************************************
# Enter a friend name form friend list to delete
# Or Press Enter to skip
# Friend name: hari
# "hari" deleted from friend list

# Enter a friend name form friend list to delete
# Or Press Enter to skip
# Friend name:
# Delete friend step skipped successfully

# ********************************************************************************

# Select the given number as shown to modify a friend
# Press 0 for {'name': 'ram', 'phoneNum': '9874105263', 'k': 'v'}
# Press 1 for {'name': 'suresh', 'phoneNum': '9876543210', 'k': 'v'}
# Select a friend or Press Enter to skip: 1
# Press Enter to skip
# Enter new phone number for suresh: 9812345670
# Phone number for suresh updated successfully.

# Select the given number as shown to modify a friend
# Press 0 for {'name': 'ram', 'phoneNum': '9874105263', 'k': 'v'}
# Press 1 for {'name': 'suresh', 'phoneNum': '9812345670', 'k': 'v'}
# Select a friend or Press Enter to skip:

# Deleted Friend List: {'name': 'ram', 'phoneNum': '9874105263', 'k': 'v'}
# Deleted Friend List: {'name': 'suresh', 'phoneNum': '9812345670', 'k': 'v'}

# Enter a friend name to check if it exists in friend list or not
# Or Press Enter to skip
# Friend name: hari
# "hari" not found in friend list

# Enter a friend name to check if it exists in friend list or not
# Or Press Enter to skip
# Friend name: ram
# "ram" found in friend list

# Enter a friend name to check if it exists in friend list or not
# Or Press Enter to skip
# Friend name:
# Program exited successfully!