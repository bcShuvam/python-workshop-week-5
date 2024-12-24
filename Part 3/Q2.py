# Part 3
# Q2. Write a Python program that takes in two sets of integers and 
# returns a new set with only the common elements in both sets.

set1 = {1,3,5,7,9}
set2 = {1,2,3,4,5}
commonElement = set1.intersection(set2)
print(f'Set 1 = {set1}')
print(f'Set 2 = {set2}')
print(f'common element = {commonElement}')