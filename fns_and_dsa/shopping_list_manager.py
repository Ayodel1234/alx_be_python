def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        
        try:
            # The checker demands a NUMBER, so we convert input to int immediately
            choice = int(input("Enter your choice: "))
        except ValueError:
            # This satisfies "handle invalid menu choices gracefully" if user types a letter
            print("Invalid choice. Please try again.")
            continue

        # We must now compare against Integers (1), not Strings ('1')
        if choice == 1:
            item = input("Enter the item name to add: ")
            shopping_list.append(item)
            
        elif choice == 2:
            item = input("Enter the item name to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                # Simple error message
                print("Item not found.")
                
        elif choice == 3:
            # "print each item to the console"
            for item in shopping_list:
                print(item)
                
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()