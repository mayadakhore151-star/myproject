
student_name = input("Enter student name: ")

while True:
    try:
        marks = float(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("Invalid marks! Enter marks between 0 and 100.")

    except ValueError:
        print("Invalid input! Please enter a number.")

print("Student Name:", student_name)
print("Marks:", marks)
