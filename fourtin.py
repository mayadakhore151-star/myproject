marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Grade: A+")
    print("Outstanding! Keep it up.")

elif marks >= 80:
    print("Grade: A")
    print("Excellent work!")

elif marks >= 70:
    print("Grade: B")
    print("Very Good!")

elif marks >= 60:
    print("Grade: C")
    print("Good effort!")

elif marks >= 35:
    print("Grade: D")
    print("You Passed!")

else:
    print("Grade: F")
    print("Don't give up. Try again!")
