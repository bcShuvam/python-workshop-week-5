# Part 3
# Q1. Write a Python program that takes in a list of strings and 
# returns a new list with only the strings that contain the letter 'a'.

listStr = []
while True:
    userInput = input('Enter a word or Press Enter to exit : ')
    if userInput == '':
        break
    else:
        if 'a' in userInput:
            listStr.append(userInput)
            
print(f'String only contains letters a : {listStr}')