# list1 = [2,4,6,8,10,12]
# print(list1)
# list2 = ['a','e','i','o','u']
# print(list2)
# list3 = [1,'Hello world', 2.5, True]
# print(list3)
# name = 'Biratnagar'
# print(name[1:4])

carCollection = ['Hyundai','Hummer','Honda','BYD']

# print(carCollection[0])
# print(carCollection[1])
# print(carCollection[2])
# print(carCollection[-1]) # accessing through negative indexing

print('Original car collection: ', carCollection)
carCollection.append('Mustang')
print('New appended car collection: ', carCollection)
carCollection.insert(2,'Mustang')
carCollection.insert(2,['Ford','Bugatti'])
carCollection.insert(-1,'Tesla')
print('New inserted car collection: ', carCollection)
del carCollection[3]
print(carCollection)
carCollection.insert(1,'Mustang')
print(carCollection)
carCollection.remove('Mustang')
print(carCollection)

carCollection.clear()
print(carCollection)
# del carCollection
# print(carCollection)

# for i in carCollection:
#     print(i)
#
# for i in range(len(carCollection)):
#     print(carCollection[i])

my_tuple = ()
print(my_tuple)

my_tuple = (1,2,3,4)
print(my_tuple)

my_tuple = (1,'Hello',3.4)
print(my_tuple)
# my_tuple.pop()
# my_tuple.insert(1,'ram')
# my_tuple.remove(1)
print(my_tuple[1:3])