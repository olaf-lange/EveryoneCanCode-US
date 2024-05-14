
todo_list = []
# todo_list.append("Buy milk")
# todo_list.append("Learn more about Azure")
# todo_list.append("Complete first Python project")
# todo_list.append("Learn more about Python")
# todo_list.append("Learn more about Flask")
# todo_list.append("Learn more about Django")
# todo_list.append("Learn more about FastAPI")
# todo_list.append("Learn more about Azure Functions")

# for todo in todo_list:
#     print(todo)

try:
    with open("Todo.txt", "r") as file:
        for line in file:
            todo_list.append(line.strip())
except FileNotFoundError:
    print("No saved items found")
# continue to loop and display menu until the user selects to exit the program
while True:
    print()  # add a couple of blank lines
    print()
    print("To-do list: ")  # print the title of the list
    for todo in todo_list:  # loop through existing to-do items
        print(todo)

    # Print the menu
    print()  # add a couple of blank lines
    print("Actions:")
    print("A - Add to-do item")
    print("R - Remove to-do item")  # <--- ***HERE***
    print("X - Exit")
    # <--- ***ALSO UPDATE MENU OPTIONS with the 'R' ***
    choice = input("Enter your choice (A, R, or X): ")
    choice = choice.upper()  # converts the choice to uppercase
    # user selected 'a' or 'A' to add an item to the list
    if choice == "A":
        todo = input("Enter the to-do item: ")
        todo_list.append(todo)
        continue  # tells the program to go back to the start of the loop
    # user selected 'r' or 'R' to remove an item from the list
    if choice == "R":
        item_number = int(input("Enter the number of the item to remove: "))
        if item_number > 0 and item_number <= len(todo_list):
            todo_list.pop(item_number - 1)
        else:
            print("Invalid item number")
        continue
    # user selected 'x' or 'X' to exit the program
    if choice == "X":
        # write out todo_list to file Todo on exit
        with open("Todo.txt", "w") as file:
            for todo in todo_list:
                file.write(todo + "\n")
        break  # tells the program to exit the loop

    # user selected something else
    print("Invalid choice")
