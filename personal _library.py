"""
Simple Personal Library
Author: Zhiyuan Jiang
Version: V1
"""
def show_menu():
    """
    Display main menu for users
    """
    print("\nPersonal Library Menu:")
    print("1.Add a book")
    print("2.Remove a book")
    print("3.List all books")
    print("4.Search for a book")
    print("5.Exit")

def add_book(library: list[str]):
    """
    Add a new book to to the library list
    """
    title = input("Enter book title: ").strip()
    library.append(title)
    print(f"Added: {title}")


def remove_book():
    pass
    


def list_book():
    pass


def search_book():
    pass

def main():
    """
    Main program that loops menu options
    """
    library: list[str] = [] #library is initialized to be empty
    while True:
        show_menu()
        choice = input("Choose an option: ").Strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            list_book()
        elif choice == "4":
            search_book()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid number.Please try again")

     