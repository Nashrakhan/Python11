# Menu-driven Python program to demonstrate the use of Set in Python

# Initialize empty sets
set1 = set()
set2 = set()

while True:
    print("\n--- SET OPERATIONS MENU ---")
    print("1. Accept two strings from the user")
    print("2. Display common letters in two strings (Intersection)")
    print("3. Display letters in first string but not in second (Difference)")
    print("4. Display set of all letters from both strings (Union)")
    print("5. Display letters in two strings but not common (Symmetric Difference)")
    print("6. Exit")
    
    choice = int(input("Enter your choice (1–6): "))
    
    if choice == 1:
        str1 = input("Enter first string: ")
        str2 = input("Enter second string: ")
        set1 = set(str1)
        set2 = set(str2)
        print("Strings stored successfully!")

    elif choice == 2:
        print("Common letters (Intersection):", set1 & set2)
        
    elif choice == 3:
        print("Letters in first but not in second (Difference):", set1 - set2)
        
    elif choice == 4:
        print("All letters from both strings (Union):", set1 | set2)
        
    elif choice == 5:
        print("Letters not common (Symmetric Difference):", set1 ^ set2)
        
    elif choice == 6:
        print("Exiting program... Thank you!")
        break
    
    else:
        print("Invalid choice! Please enter a number between 1–6.")
