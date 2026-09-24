import os  # Needed to check if the file exists

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(SCRIPT_DIR, "todo_list.txt")

print(f"DEBUG: Your tasks will save exactly here -> {FILENAME}\n")

# --- 1. LOAD TASKS AT START ---
l = []

if os.path.exists(FILENAME):
    with open(FILENAME, "r") as file:
        l = [line.strip() for line in file.readlines() if line.strip()]

# A quick helper function to handle saving easily
def save_to_file():
    with open(FILENAME, "w") as file:
        for task in l:
            file.write(f"{task}\n")


option = 0
removed = ""

while option != -1:

    print("ENTER YOUR OPTION")
    print("1.ADD")
    print("2.VIEW")
    print("3.COMPLETE")
    print("4.DELETE")
    print("5.EXIT")

    try:

        your_option = int(input("ENTER YOUR CHOICE\n"))

        if your_option == 5:
            print("bye")
            break

        if your_option == 1:

            add = input("ADD ANYTHING IN TO DO LIST\n")

            l.append(add)
            save_to_file()

            print("Successfully added your task\n")

        elif your_option == 3:

            completed = input("ENTER YOUR COMPLETED TASK\n")

            if completed in l:

                l.remove(completed)
                save_to_file()

                result = ",".join(l)
                print(result)
                print("you successfully completed a task\n")   # moved inside if

            else:
                print("it not in the list\n")

        elif your_option == 4:

            deleted = input("ENTER YOUR DELETED TASK\n")

            if deleted in l:

                l.remove(deleted)
                save_to_file()

                result = ",".join(l)
                print(result)
                print("you successfully deleted a task\n")   # moved inside if

            else:
                print("it not in the list\n")

        elif your_option == 2:

            print("Here your tasks\n")

            if len(l) == 0:
                print("No tasks available")
            else:
                result = ",".join(l)
                print(result)

        else:
            print("Invalid option")

    except ValueError:
        print("pls enter valid option")