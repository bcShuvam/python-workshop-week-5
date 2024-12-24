# Part 3
# Q7. Write a Python program that takes in a list of tuples representing
# book titles and their corresponding authors, and returns
# a new list of tuples sorted by author name in alphabetical order.

books = (
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien"},
    {"title": "The Da Vinci Code", "author": "Dan Brown"}
)
sortedBooks = ()
authorLists = []

print('Unsorted book by author\'s name:')
for book in books:
    print(book)

books = list(books)
for i in range(len(books)):
    for j in range(len(books)-i-1):
        if books[j]['author'] > books[j+1]['author']:
            temp = books[j]
            books[j] = books[j+1]
            books[j+1] = temp

print('\nSorted books by author\'s name:')
books = tuple(books)
for book in books:
    print(book)