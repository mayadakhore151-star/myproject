while True:
    marks = int(input("Enter Marks (0-100): "))

    if marks >= 0 and marks <= 100:
        print("Valid Marks")
        break

    else:
        print("Invalid Marks! Enter again.")
