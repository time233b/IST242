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
    


def remove_book(library: list[str]):
   title = input("Enter the book to remove: ").strip()
   library.remove(title)




def list_book(library: list[str]):
    if not library:
        print("Libary is empty.")
        return
    print("\nYour books: ")
    for i, title in enumerate(library, start = 1):
        print(f"{i}.{title}")
    

def search_book(library:list[str]):
    keyword= input("Enter a title or keyword to search: ").strip()
    if not keyword:
       print("Search term can not be empty.")
       return
    matches=[b for b in library if keyword.lower() in b.lower()]
    if matches:
        print("\nMatches: ")
        for m in matches:
            print(f"- {m}")
    else:
       print("No matches found.")


def main():
    """
    Main program that loops menu options
    """
    library: list[str] = [] #library is initialized to be empty
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            list_book(library)
        elif choice == "4":
            search_book(library)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid number.Please try again")
if __name__ == "__main__":
    main()