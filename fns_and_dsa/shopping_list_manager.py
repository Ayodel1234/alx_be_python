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
        
        # 1. Get input as a string first
        choice_input = input("Enter your choice: ")
        
        # 2. Check if it is a number to prevent crashing
        if choice_input.isdigit():
            choice = int(choice_input) # Convert to number for the checker
        else:
            print("Invalid choice. Please try again.")
            continue # Skip the rest and show menu again

        # 3. Use Integers (1, 2, 3) for comparisons now
        if choice == 1:
            item = input("Enter the item name to add: ")
            shopping_list.append(item)
            
        elif choice == 2:
            item = input("Enter the item name to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item not found.")
                
        elif choice == 3:
            for item in shopping_list:
                print(item)
                
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()