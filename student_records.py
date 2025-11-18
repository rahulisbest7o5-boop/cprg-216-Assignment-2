
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

def search(students, sid):
    for i, s in enumerate(students):
        if s["id"] == sid:
            return i
    return -1


def add(students, sid, name, gpa, semester):
    student = {
        "id": sid,
        "name": name,
        "gpa": gpa,
        "semester": semester
    }
    students.append(student)

    print("Student added")
    print(f"{sid:<8}{name:<15}{gpa:<8}{semester}")


def remove(students, sid):
    index = search(students, sid)
    if index == -1:
        print("Student not found")
    else:
        students.pop(index)
        print("Student removed")


def edit_name(students, sid, new_name):
    index = search(students, sid)
    if index == -1:
        print("Student not found")
    else:
        students[index]["name"] = new_name
        print("Student name modified for the student with id  " + sid)
        print("Student's new name is  " + new_name)


def show_menu():
    print("What would you like to do today?")
    print("-Find a student? enter 1")
    print("-edit a student's info using student ID? enter 2")
    print("-Add a new student? enter 3")
    print("-Remove a student? enter 4")
    return input()


def run_search(students):
    while True:
        print("Enter the id of the student. Enter -1 to return to the previous menu")
        sid = input()

        if sid == "-1":
            break

        index = search(students, sid)
        if index == -1:
            print("Student not found")
        else:
            st = students[index]
            print("Student found")
            print(f"{st['id']:<8}{st['name']:<15}{st['gpa']}")


def run_edit(students):
    while True:
        print("Enter the id of the student. Enter -1 to return to the previous menu")
        sid = input()

        if sid == "-1":
            break

        print("Enter the new name of the student")
        new_name = input()

        edit_name(students, sid, new_name)


def run_add(students):
    while True:
        print("Enter id of the student, followed by the student's information.")
        print("id:")
        sid = input()
        print("name:")
        name = input()
        print("gpa:")
        gpa = float(input())
        print("semester:")
        semester = int(input())

        add(students, sid, name, gpa, semester)

        print("Do you want to add a new student?y(yes)/n(no)")
        again = input().lower()
        if again not in ["y", "yes"]:
            break


def run_remove(students):
    while True:
        print("Enter id of the student that you want to remove from the students' registry.")
        print("id:")
        sid = input()

        remove(students, sid)

        print("Do you want to remove more students?y(yes)/n(no)")
        again = input().lower()
        if again not in ["y", "yes"]:
            break


def main():
    students = []

    print("Welcome to the students record program")

    while True:
        choice = show_menu()

        if choice == "1":
            run_search(students)
        elif choice == "2":
            run_edit(students)
        elif choice == "3":
            run_add(students)
        elif choice == "4":
            run_remove(students)
        else:
            print("Invalid input")

        print("What you like to continue(y/yes), or exit the program(n/no)?")
        again = input().lower()
        if again not in ["y", "yes"]:
            break


if __name__ == "__main__":
    main()




