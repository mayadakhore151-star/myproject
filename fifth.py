def get_answer(question):
    """Ask a question and return the answer, or a default if blank."""
    answer = input(question).strip()
    return answer if answer else "Not provided"


def main():
    print("===== STUDENT WELCOME PROGRAM =====")

    name = get_answer("Enter your name: ")
    city = get_answer("Which city do you live in? ")
    course = get_answer("Which course are you studying? ")
    favorite_subject = get_answer("What is your favorite subject? ")

    print("\n========== YOUR PROFILE ==========")
    print(f"Name             : {name}")
    print(f"City             : {city}")
    print(f"Course           : {course}")
    print(f"Favorite Subject : {favorite_subject}")
    print("=================================")
    print(f"Thank you, {name}! Have a great day.")


if __name__ == "__main__":
    main()
