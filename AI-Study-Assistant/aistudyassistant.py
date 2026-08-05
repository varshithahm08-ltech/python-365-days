print("===================================")
print("      AI STUDY ASSISTANT")
print("===================================")

name = input("Enter your name: ")
subject = input("Which subject are you studying today? ")
hours = int(input("How many hours will you study today? "))

print("\nHello", name)

if hours >= 4:
    print("Excellent! Keep up the great work.")
elif hours >= 2:
    print("Good job! Try to study a little more tomorrow.")
else:
    print("You can do better. Aim for at least 2 hours tomorrow.")

print("Today's subject:", subject)
print("Best of Luck for your studies!")