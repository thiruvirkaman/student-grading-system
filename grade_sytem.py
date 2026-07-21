try:
    mark = int(input("Enter your mark: "))  
    if mark < 0 or mark > 100:
        print("Invalid mark. Please enter a mark between 0 and 100.")
    elif mark >= 90 and mark <= 100:
        print("Grade: A")
    elif mark >= 80 and mark <=89:
        print("Grade: B")
    elif mark >= 70 and mark <=79:
        print("Grade: C")
    elif mark >= 60 and mark <=69:
        print("Grade: D")
    else:
        print("Grade: E")
except ValueError as e:
    print("Invalid input. Please enter a valid integer mark.")
