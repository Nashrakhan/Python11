# Menu-driven program to demonstrate use of in-built string functions in Python

while True:
    print("\n--- STRING OPERATIONS MENU ---")
    print("1. Accept a string from the user")
    print("2. Sort the characters in a string")
    print("3. Remove duplicate characters from a string")
    print("4. List unique characters with their count in a string")
    print("5. Find number of words in a string")
    print("6. Remove all non-alphabetic characters from a string")
    print("7. Exit")
    
    choice = int(input("Enter your choice (1–7): "))

    if choice == 1:
        s = input("Enter a string: ")
        print("String stored successfully!")
    
    elif choice == 2:
        # using sorted() in-built function
        sorted_str = ''.join(sorted(s))
        print("Sorted string:", sorted_str)
    
    elif choice == 3:
        # using for loop and in-built 'not in'
        result = ''
        for ch in s:
            if ch not in result:
                result += ch
        print("String after removing duplicates:", result)
    
    elif choice == 4:
        # using set() and count() in-built functions
        print("Unique characters with their count:")
        for ch in sorted(set(s)):
            print(f"{ch} : {s.count(ch)}")
    
    elif choice == 5:
        # using split() function
        words = s.split()
        print("Number of words in string:", len(words))

    elif choice == 6:
        # using isalpha() to keep only alphabetic characters
        alpha_str = ''.join(ch for ch in s if ch.isalpha() or ch.isspace())
        print("String after removing non-alphabetic characters:", alpha_str)
    
    elif choice == 7:
        print("Exiting program... Thank you!")
        break
    
    else:
        print("Invalid choice! Please enter a number between 1 and 7.")
