# Menu-driven Python program to demonstrate the use of Dictionary in Python
# Initialize an empty dictionary

d = {}
while True:
    print("\n--- DICTIONARY OPERATIONS MENU ---")
    print("1. Create key/value pair dictionary")
    print("2. Update item in existing dictionary")
    print("3. Concatenate another dictionary")
    print("4. Delete item from existing dictionary")
    print("5. Find a key and print its value")
    print("6. Exit")
    
    choice = int(input("Enter your choice (1–6): "))
    
    if choice == 1:
        key = input("Enter key: ")
        value = input("Enter value: ")
        d[key] = value
        print("Dictionary after adding item:", d)
        
    elif choice == 2:
        key = input("Enter key to update: ")
        if key in d:
            new_value = input("Enter new value: ")
            d[key] = new_value
            print("Updated dictionary:", d)
        else:
            print("Key not found!")
        
    elif choice == 3:
        # concatenating another dictionary
        extra = {}
        n = int(input("Enter number of key/value pairs to add: "))
        for i in range(n):
            k = input(f"Enter key {i+1}: ")
            v = input(f"Enter value {i+1}: ")
            extra[k] = v
        d.update(extra)
        print("Dictionary after concatenation:", d)
        
    elif choice == 4:
        key = input("Enter key to delete: ")
        if key in d:
            del d[key]
            print("Key deleted successfully!")
        else:
            print("Key not found!")
            print("Current dictionary:", d)
    
    elif choice == 5:
        key = input("Enter key to search: ")
        if key in d:
            print("Value for", key, "is:", d[key])
        else:
            print("Key not found!")
            
    elif choice == 6:
        print("Exiting program... Thank you!")
        break
    
    else:
        print("Invalid choice! Please enter between 1–6.")
