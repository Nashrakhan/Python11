# Write a menu-driven Python program to perform following operations on an array:

# 1) Sum of all even elements
# 2) Count the number of elements divisible by 3
# 3) Add 2 elements at the end of the list
# 4) Remove all odd elements from the list
# 5) Sort the elements in descending order

# initialize the list (array)

nums = [12, 5, 9, 4, 15, 18, 7]
while True:
    print("\n--- ARRAY OPERATIONS MENU ---")
    print("1. Display the array")
    print("2. Sum of all even elements")
    print("3. Count elements divisible by 3")
    print("4. Add 2 elements at the end of the list")
    print("5. Remove all odd elements from the list")
    print("6. Sort the elements in descending order")
    print("7. Exit")
    
    choice = int(input("Enter your choice (1–7): "))
    
    if choice == 1:
        print("Current array:", nums)
        
    elif choice == 2:
        even_sum = sum(x for x in nums if x % 2 == 0)
        print("Sum of all even elements:", even_sum)
        
    elif choice == 3:
        count_div3 = sum(1 for x in nums if x % 3 == 0)
        print("Number of elements divisible by 3:", count_div3)
        
    elif choice == 4:
        n1 = int(input("Enter first element to add: "))
        n2 = int(input("Enter second element to add: "))
        nums.append(n1)
        nums.append(n2)
        print("Array after adding two elements:", nums)
        
    elif choice == 5:
        nums = [x for x in nums if x % 2 == 0]
        print("Array after removing all odd elements:", nums)
        
    elif choice == 6:
        nums.sort(reverse=True)
        print("Array sorted in descending order:", nums)
        
    elif choice == 7:
        print("Exiting program... Thank you!")
        break
    
    else:
        print("Invalid choice! Please enter a number between 1–7.")
