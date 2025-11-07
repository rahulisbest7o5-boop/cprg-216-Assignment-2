
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

def run_add(students: List[Student]) -> None:
    while True:
        print("Enter id of the student, followed by the student's information.")
        print("id:")
        sid = int(input().strip())
        print("name:")
        name = input().strip()
        print("gpa:")
        gpa = float(input().strip())
        print("semester:")
        semester = int(input().strip())

        add(students, sid, name, gpa, semester)
        print("Student added")
        print(_fmt_full_row(students[-1]))
        yn = input("Do you want to add a new student?y(yes)/n(no)\n").strip().lower()
        if yn not in ("y", "yes"):
            break


