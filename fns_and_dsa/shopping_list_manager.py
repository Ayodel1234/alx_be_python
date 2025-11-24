def display_menu():
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item name to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to your list.")
            
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item name to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your list.")
            else:
                print(f"Error: '{item}' was not found in the list.")
                
        elif choice == '3':
            # Display the shopping list
            print("\n--- Current Shopping List ---")
            if len(shopping_list) == 0:
                print("Your list is currently empty.")
            else:
                # Use enumerate to number the items nicely
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            print("-----------------------------")
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()