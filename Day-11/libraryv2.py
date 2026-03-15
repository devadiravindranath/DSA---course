#library v2(presistant storage of data)

#new features:
# Data saved in file
#program remembers book after restart

import json

#load library Data
def load_library():
    try:
        with open('library_data.json', 'r') as file:
            library = json.load(file)
    except FileNotFoundError:
        library = {}
    return library

#save library data
def save_library(library):
    with open('library_data.json', 'w') as file:
        json.dump(library, file)

#add book to library
def add_book(library, title, author):
    library[title] = author
    save_library(library)
    print(f'Book "{title}" by {author} added to library.')

#view books in library
def view_books(library):
    if not library:
        print("Library is empty.")
    else:
        print("Books in Library:")
        for title, author in library.items():
            print(f'"{title}" by {author}')

#delete book from library
def delete_book(library, title):
    if title in library:
        del library[title]
        save_library(library)
        print(f'Book "{title}" deleted from library.')
    else:
        print(f'Book "{title}" not found in library.')

def main():
    library = load_library()
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Delete Book")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(library, title, author)
        elif choice == '2':
            view_books(library)
        elif choice == '3':
            title = input("Enter book title to delete: ")
            delete_book(library, title)
        elif choice == '4':
            print("Exiting library. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()