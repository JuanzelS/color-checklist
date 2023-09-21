checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    if 0 <= index < len(checklist):
        return checklist[index]
    else:
        return "Index out of range"

def update(index, item):
    if 0 <= index < len(checklist):
        checklist[index] = item
    else:
        print("Index out of range")

def destroy(index):
    if 0 <= index < len(checklist):
        checklist.pop(index)
    else:
        print("Index out of range")

def mark_completed(index):
    if 0 <= index < len(checklist):
        # You can implement marking an item as completed here (not implemented in this code)
        pass
    else:
        print("Index out of range")

def list_all_items():
    for i, list_item in enumerate(checklist):
        print(f"{i}: {list_item}")

def user_input(prompt):
    user_input = input(prompt).strip().lower()
    return user_input

def select(selection):
    if selection == "c":
        item = user_input("Add an item: ")
        create(item)
    elif selection == "r":
        index = int(user_input("Enter index to read: "))
        print(read(index))
    elif selection == "u":
        index = int(user_input("Enter index to update: "))
        item = user_input("Enter new item: ")
        update(index, item)
    elif selection == "d":
        index = int(user_input("Enter index to delete: "))
        destroy(index)
    elif selection == "p":
        list_all_items()
    elif selection == "q":
        return False
    else:
        print("Invalid input. Please try again.")
    return True

# Test function
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    list_all_items()  # Added to list all items after updating

# Call the test function to see the output
test()

running = True
while running:
    selection = user_input("Press C to add, R to read, U to update, D to delete, P to display, and Q to quit: ")
    running = select(selection)

print(checklist)