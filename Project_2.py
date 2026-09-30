while True:
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("\nSelect Pattern Type:")
        print("1. Regular Triangle")
        print("2. Inverted Triangle")
        print("3. Number Pyramid")
        pattern_choice = input("Enter pattern choice: ")
        
        rows = int(input("Enter the number of rows for the pattern: "))
        print("\nPattern:")
        
        if pattern_choice == '1':
            for i in range(rows):
                for j in range(i + 1):
                    print("*", end=" ")
                print()
        elif pattern_choice == '2':
            for i in range(rows):
                for j in range(rows - i):
                    print("*", end=" ")
                print()
        elif pattern_choice == '3':
            for i in range(rows):
                for j in range(i + 1):
                    print(i + 1, end=" ")
                print()
        print()
            
    elif choice == '2':
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        
        total_sum = 0 # This line is written using AI
        for num in range(start, end + 1):# This line is written using AI
            total_sum += num # This line is written using AI
            if num % 2 == 0:
                print(f"Number {num} is Even")# This line is written using AI
            else:
                print(f"Number {num} is Odd")# This line is written using AI
                
        print(f"Sum of all numbers from {start} to {end} is: {total_sum}")# This line is written using AI
        print()
        
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please select 1, 2, or 3.\n")
