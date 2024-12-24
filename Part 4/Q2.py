# Part 4
# Q2. Imagine that you are working on a project to assist a nearby library in
# managing their book inventory.
# They want you to design a program that enables them to add new books,
# remove old books, and perform advanced book searches.
# You make the decision to use a list to store all the library's books.
# Moreover, your book list will be as shown below:

# books = [
# {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
# {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
# {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954},
# {"title": "The Da Vinci Code", "author": "Dan Brown", "year": 2003}
# ]
# Task: Create a Python program that prompts user with a dashboard menu as follows:
# 1. Add a new book
# 2. Remove a book
# 3. Search for a book by title
# 4. Search for a book by author (optional)
# 5. List all the books
# 6. Quit

# List of books
books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954},
    {"title": "The Da Vinci Code", "author": "Dan Brown", "year": 2003}
]

dashboardMenu = [
    'Press 1 to Add a new book',
    'Press 2 to Remove a book',
    'Press 3 to Search for a book by title',
    'Press 4 to Search for a book by author',
    'Press 5 to List all the books',
    'Press 6 to Quit',
]

selectedMenu = 0
while selectedMenu != 6: # 6. Quit
    # for book in books:
    #     print(book)
    print()
    for menu in dashboardMenu:
        print(menu)
    selectedMenu = input('\nSelect any option: ')
    if not selectedMenu.isdigit():
        print('\nInvalid! input.')
        continue
        # selectedMenu = input('Select any option: ')
    else:
        selectedMenu = int(selectedMenu)

        # 1. Add a new book
        if selectedMenu == 1:
            bookTitle = input('Enter book title: ')
            bookAuthor = input('Enter book\'s author: ')
            bookPublished = input('Enter book\'s year of publish: ')
            if bookPublished.isdigit():
                bookPublished = int(bookPublished)
            newBook = {
                "title": bookTitle,
                "author": bookAuthor,
                "year": bookPublished
            }
            books.append(newBook)
            print('****************************************************************************')
            print(f'New book titled "{newBook['title']}" added successfully!')
            print('****************************************************************************')

        # 2. Remove a book
        elif selectedMenu == 2:
            for i in range(len(books)):
                print(f'Press {i+1} to remove book "{books[i]['title']}"')
            while True:
                deleteBookByIndex = input('Enter your choice or Press Enter to exit: ')
                if deleteBookByIndex.isdigit():
                    deleteBookByIndex = int(deleteBookByIndex)
                    if 0 < deleteBookByIndex < len(books)+1:
                        print('****************************************************************************')
                        print(f'"{books[deleteBookByIndex - 1]['title']}" book was removed successfully!')
                        print('****************************************************************************')
                        books.pop(deleteBookByIndex - 1)
                        break
                    else:
                        print('Invalid! input')
                elif deleteBookByIndex == '':
                    break
                else:
                    print('Invalid! input')

        # 3. Search for book by title
        elif selectedMenu == 3:
            print('Search book by book title')
            searchByTitle = input('Enter book title: ')
            bookFound = False
            print('****************************************************************************')
            for book in books:
                if searchByTitle.lower() in book['title'].lower():
                    bookFound = True
                    print(f'Book found by title\nTitle: {book['title']}')
                    print(f'Author: {book['author']}')
                    print(f'Year: {book['year']}')
                    break
            if not bookFound:
                print(f'Book titled "{searchByTitle}" not found!')
            print('****************************************************************************')

        # 4. Search for book by author
        elif selectedMenu == 4:
            searchByAuthor = input('Enter author name: ')
            bookFound = False
            print('****************************************************************************')
            for book in books:
                if searchByAuthor.lower() in book['author'].lower():
                    bookFound = True
                    print(f'Book found by author named\nTitle: {book['title']}')
                    print(f'Author: {book['author']}')
                    print(f'Year: {book['year']}')
                    break
            if not bookFound:
                print(f'Book author named "{searchByAuthor}" not found!')
            print('****************************************************************************')

        # 5. List all the books
        elif selectedMenu == 5:
            print('Displaying all book in books list')
            for book in books:
                print(book)

        elif selectedMenu > 6:
            print('Invalid! input')
print('****************************************************************************')
print('\tProgram Exited Successfully!')
print('****************************************************************************')