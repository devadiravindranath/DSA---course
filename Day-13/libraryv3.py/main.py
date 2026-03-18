from library import add_book, view_books, remove_book

while True:
    print('\n1. Add Book')
    print('2. View Books')
    print('3. Remove Book')
    print('4. Exit')

    choice = input("Enter your choice: ")

    if choice == '1':
        title = input('Enter book name: ')
        add_book(title)

    elif choice == '2':
        view_books()

    elif choice == '3':
        title = input('Enter book name to remove: ')
        remove_book(title)

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")