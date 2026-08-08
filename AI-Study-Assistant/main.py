print("=" * 40)
print("       AI STUDY ASSISTANT")
print("=" * 40)

print("\nWelcome to AI Study Assistant!")

name = input("Enter your name: ")

print(f"\nHello, {name}!")

print("\nWhat would you like to do?")

print("1. Student Profile")
print("2. Study Calculator")
print("3. AI Study Assistant")
print("4. Exit")

choice = input("\nEnter your choice: ")

if choice == "1":
    print("Student Profile selected")

elif choice == "2":
    print("Study Calculator selected")

elif choice == "3":
    print("AI Study Assistant selected")

elif choice == "4":
    print(f"Goodbye, {name}! Keep studying!")

else:
    print("Invalid choice. Please try again.")