# Menu-driven Python program using simple tuple operations
# Each student is stored as a tuple:
# (roll_no, name, total_marks, average_marks, admission_date)

students = ()

while True:
    print("\n--- STUDENT TUPLE MENU ---")
    print("1. Add student's marks information (with total & average)")
    print("2. Display student with specified roll number")
    print("3. Display students admitted in the same year")
    print("4. Display students above a given average")
    print("5. Display student with highest and lowest marks")
    print("6. Exit")
    
    choice = int(input("Enter your choice (1-6): "))
    
    if choice == 1:
        roll = input("Enter roll number: ")
        name = input("Enter student name: ")
        m1 = int(input("Enter marks in Subject 1: "))
        m2 = int(input("Enter marks in Subject 2: "))
        m3 = int(input("Enter marks in Subject 3: "))
        
        total = m1 + m2 + m3
        avg = total / 3
        adm_date = input("Enter admission date (dd/mm/yyyy): ")
        student = (roll, name, total, avg, adm_date)
        
        # add the new student as a tuple inside the main tuple
        students = students + (student,)
        print("Student added successfully!")
        
    elif choice == 2:
        roll = input("Enter roll number to search: ")
        found = False
        for st in students:
            if st[0] == roll:
                print("Student found:", st)
        found = True
        if not found:
            print("Student not found.")
            
    elif choice == 3:
        year = input("Enter admission year (yyyy): ")
        found = False
        for st in students:
            # admission date stored as string "dd/mm/yyyy"
            if st[4].endswith(year):
                print(st)
                found = True
            if not found:
                print("No students admitted in year", year)
                
    elif choice == 4:
        limit = float(input("Enter average limit: "))
        found = False
        for st in students:
            if st[3] > limit:
                print(st)
                found = True
        if not found:
            print("No students above this average.")
        
    elif choice == 5:
        if len(students) == 0:
            print("No students added yet.")
        else:
            # use simple max/min based on total marks (index 2)
            max_marks = max(st[2] for st in students)
            min_marks = min(st[2] for st in students)
            for st in students:
                if st[2] == max_marks:
                    print("Highest Marks:", st)
                if st[2] == min_marks:
                    print("Lowest Marks:", st)
    
    elif choice == 6:
        print("Exiting program... Thank you!")
        break
    else:
        print("Invalid choice! Please enter between 1–6.")
