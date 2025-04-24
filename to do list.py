def to_do_list():
    task = []

    while True:
        print("1. Add task")
        print("2. Show task")
        print("3. Delete task")
        print("4. Quit application")
        choice = input("Enter your choice")

        if choice == '1':
            print()
            n_tasks = int(input("How many task do you want to add "))
            print