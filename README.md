# Moduel-1-
# To-Do Application
# 1. Add task
# 2. View task
# 3. Delete Task
# 4. Quit application

tasks = []
def add_task():
    task = input("Enter the task description: ")
    task.append(task)
    print("Task added successfully.")

def view_tasks():
    if len(tasks) == 0:
        print("There are no task to view.")
    else:
        print('List of tasks:')
    for i, task in enumerate(tasks):
        print(f'{i+1}. {task}')

def delete_task():
    if len(tasks) == 0:
        print('No task to delete.')
    else:
        print('Tasks: ')
        for i, task in enumerate(tasks):
            print(f' {i+1}. {task}')
        choice = int(input('Enter the task number to delete:'))

        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print('Task deleted successfully.')
        else:
            print('invalid task number.')

def main():
    while True:
        print("1. Add task")
        print('2. view task')
        print('3. Delete task')
        print('4. Quit application')

        choice = user_choice = int(input("Select an option (1-4): "))
        if choice == 1:
           add_task()
        elif choice == 2:
           view_tasks()
        elif choice == 3:
           delete_task()
        elif choice == 4:
           print("Have a great day. Goodbye!")
           break
        else:
           print("Error: Invalid chocie. Please select a valid menu option (1-4).")

if __name__ == "__main__":
        main()