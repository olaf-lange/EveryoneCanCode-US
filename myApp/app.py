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

# continue to loop and display menu until the user selects to exit the program
while True:
    print() # add a couple of blank lines
    print()
    print("To-do list: ") # print the title of the list
    for todo in todo_list: # loop through existing to-do items
        print(todo)

    # Print the menu
    print() # add a blank line
    print("Actions:")
    print("A - Add to-do item")
    print("X - Exit")
    choice = input("Enter your choice (A or X): ")
    choice = choice.upper() # converts the choice to uppercase

    # user selected 'a' or 'A' to add an item to the list
    if choice == "A":
        todo = input("Enter the to-do item: ") 
        todo_list.append(todo)
        continue  # tells the program to go back to the start of the loop

    # user selected 'x' or 'X' to exit the program
    if choice == "X":
        break # tells the program to exit the loop

    # user selected something else
    print("Invalid choice")