
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 35:
        return "D"
    else:
        return "Fail"


def main():
    student_name = input("Enter student name: ")

    while True:
        try:
            marks = float(input("Enter marks (0-100): "))

            if 0 <= marks <= 100:
                break

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    grade = calculate_grade(marks)

    print("\n--- Student Result ---")
    print("Name:", student_name)
    print("Marks:", marks)
    print("Grade:", grade)


if __name__ == "__main__":
    main()
