# Part 2
# Q6. Write a Python program that prompts the user 
# for a list of integers and stores them in a list. 
# For all values that are greater than 100, 
# the string 'over' should be stored instead. 
# The program should display the resulting list.

numList = []
while True:
    userInput = input('Enter a number or press Enter to exit : ')
    if userInput == '':
        break
    else:
        if userInput.isdigit():
            userInput = int(userInput)
            if userInput > 100:
                numList.append('over')
            else:
                numList.append(userInput)
        else:
            print('Invalid input. Please enter a valid integer.\n')
print(f'Resulting List = {numList}')