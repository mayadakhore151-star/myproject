# Function to calculate grade

def calculate_grade(marks):

    if marks >= 90:
        return "A+", "Outstanding! Keep it up."

    elif marks >= 80:
        return "A", "Excellent Work!"

    elif marks >= 70:
        return "B", "Very Good!"

    elif marks >= 60:
        return "C", "Good Effort!"

    elif marks >= 35:
        return "D", "You Passed! Keep Improving."

    else:
        return "F", "Don't Give Up. Try Again!"


# Get student name

name = input("Enter Student Name: ")

# Validate marks

while True:
    try:
        marks = float(input("Enter Marks (0-100): "))

        if 0 <= marks <= 100:
            break

        else:
            print("Invalid Marks! Enter marks between 0 and 100.")

    except ValueError:
        print("Please enter numbers only.")


# Calculate Grade

grade, message = calculate_grade(marks)


# Display Result

print("\n----- Student Result -----")

print("Student Name:", name)
print("Marks:", marks)
print("Grade:", grade)
print("Message:", message)
