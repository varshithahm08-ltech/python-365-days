tasks = []


def add_task():
    subject = input("Enter subject: ")
    task = input("Enter study task: ")

    task_data = {
        "subject": subject,
        "task": task,
        "completed": False
    }

    tasks.append(task_data)

    print("✅ Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("📚 No tasks available.")
        return

    print("\n📋 YOUR STUDY TASKS")

    for i, task in enumerate(tasks, start=1):
        status = "✅ Completed" if task["completed"] else "⏳ Pending"
        print(f"{i}. {task['subject']} - {task['task']} [{status}]")


def complete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("🎉 Task completed!")
        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")


def study_suggestion():
    for task in tasks:
        if not task["completed"]:
            print("\n🤖 AI STUDY SUGGESTION")
            print(f"Subject: {task['subject']}")
            print(f"Task: {task['task']}")
            print("💡 Study for 45 minutes and take a 10-minute break.")
            return

    print("🎉 You have no pending tasks!")


def progress_report():
    if len(tasks) == 0:
        print("📊 No tasks available.")
        return

    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    total = len(tasks)
    percentage = (completed / total) * 100

    print("\n📊 STUDY PROGRESS")
    print(f"Total tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {total - completed}")
    print(f"Progress: {percentage:.2f}%")


while True:
    print("\n==========================")
    print("🤖 AI STUDY ASSISTANT")
    print("==========================")
    print("1. Add Study Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Get Study Suggestion")
    print("5. Progress Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        study_suggestion()

    elif choice == "5":
        progress_report()

    elif choice == "6":
        print("👋 Goodbye! Keep studying!")
        break

    else:
        print("❌ Invalid choice. Please try again.")