print("=" * 40)
print("      AI STUDY ASSISTANT")
print("=" * 40)

name = input("Enter your name: ")

while True:
    print("\nWelcome", name)
    print("\n1. Study Planner")
    print("2. Study Motivation")
    print("3. About Project")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        subject = input("Subject: ")
        hours = int(input("Hours: "))

        print("\nToday's Study Plan")
        print("Subject:", subject)
        print("Study Hours:", hours)
        print("✔ Learn theory")
        print("✔ Practice programs")
        print("✔ Revise notes")

    elif choice == "2":
        hours = int(input("How many hours will you study today? "))

        if hours >= 4:
            print("Excellent! Keep up the great work!")
        elif hours >= 2:
            print("Good Job! Try to study a little more.")
        else:
            print("You can do better. Aim for at least 2 hours.")

    elif choice == "3":
        print("\nAI Study Assistant")
        print("Version 2.0")
        print("Developer: Varshitha HM")
        print("Purpose: Helping students study smarter.")

    elif choice == "4":
        print("Thank you for using AI Study Assistant!")
        break

    else:
        print("Invalid choice! Please try again.")