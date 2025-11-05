
print("Welcome to the Student Records Management System")
def show_menu():
    print("What would you like to do today?")
    print("-Find a student? enter 1")
    print("-edit a student's info using student ID? enter 2")
    print("-Add a new student? enter 3")
    print("-Remove a student? enter 4")
    selection = input().strip()
    return selection
print(show_menu())


