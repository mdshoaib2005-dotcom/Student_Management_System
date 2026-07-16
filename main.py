from manager import StudentManager
from student import Student
from grade_calculator import generate_report_card, get_class_statistics
from utils import print_header, print_table, get_valid_input
import datetime

manager = StudentManager()

# First menu function

def menu_add_student():
    print_header("ADD NEW STUDENT")

    sid = input("Enter Student ID (e.g. S001): ").strip().upper()
    name = input("Enter Full Name: ").strip()
    age = get_valid_input("Enter Age: ", int, 15, 60)
    course = input("Enter Course Name: ").strip()
    email = input("Enter Email Address: ").strip()
    phone = input("Enter Phone (optional): ").strip()

    student = Student(sid, name, age, course, email, phone)

    if manager.add_student(student):
        print(f"\n✅ Student '{name}' added successfully!")
    else:
        print(f"\n❌ Student ID '{sid}' already exists.")


# Second menu function()

def menu_view_all():
    print_header("ALL STUDENTS")

    students = manager.get_all_students()

    if not students:
        print("No students found.")
        return

    rows = []

    for student in students:
        rows.append([
            student.student_id,
            student.name,
            student.age,
            student.course,
            student.email
        ])

    print_table(
        ["ID", "Name", "Age", "Course", "Email"],
        rows
    )

    print(f"\nTotal Students: {len(students)}")


# Third menu function

def menu_search():
    print_header("SEARCH STUDENT")

    term = input("Enter Student ID or Name: ").strip()

    results = manager.find_student(term)

    if not results:
        print("No matching student found.")
    else:
        for student in results:
            print(student)


# Add Marks


def menu_add_marks():
    print_header("ADD MARKS")

    sid = input("Enter Student ID: ").strip().upper()

    result = manager.find_student(sid)

    if not result:
        print("Student not found.")
        return

    student = result[0]

    print(f"Adding marks for: {student.name}")

    n = get_valid_input("How many subjects? ", int, 1, 20)

    for i in range(n):
        subject = input(f"Subject {i+1} name: ").strip()

        marks = get_valid_input("Marks obtained: ", float, 0, 100)

        max_marks = get_valid_input("Maximum marks: ", float, 1, 100)

        manager.add_marks(sid, subject, marks, max_marks)

    print(f"\n✅ Marks added for {student.name}!")


# View Report Card


def menu_report_card():
    print_header("REPORT CARD")

    sid = input("Enter Student ID: ").strip().upper()

    result = manager.find_student(sid)

    if not result:
        print("Student not found.")
        return

    student = result[0]

    marks = manager.get_marks(sid)

    generate_report_card(student, marks)


# Class Statistics


def menu_statistics():
    print_header("CLASS STATISTICS")

    stats = get_class_statistics(manager)

    if not stats:
        print("No data available. Add students and marks first.")
        return

    print(f"Total Students : {stats['total_students']}")
    print(f"With Marks     : {stats['with_marks']}")
    print(f"Class Average  : {stats['average_pct']}%")
    print(
        f"Top Performer  : {stats['top_student']['name']} "
        f"({stats['top_student']['percentage']:.1f}%)"
    )
    print(f"Passed         : {stats['passed']}")
    print(f"Failed         : {stats['failed']}")

    print("\nRANK TABLE:")

    rows = []

    for i, s in enumerate(stats['all_stats']):
        rows.append([
            i + 1,
            s['name'],
            f"{s['percentage']:.1f}%",
            s['grade']
        ])

    print_table(
        ["Rank", "Name", "Percentage", "Grade"],
        rows
    )


# Export Report


def menu_export():
    print_header("EXPORT REPORT")

    filename = f"report_{datetime.date.today()}.txt"

    with open(filename, "w") as file:

        file.write("STUDENT MANAGEMENT SYSTEM - FULL REPORT\n")
        file.write(f"Generated: {datetime.datetime.now()}\n")
        file.write("=" * 60 + "\n")

        for student in manager.get_all_students():

            file.write(str(student) + "\n")

            marks = manager.get_marks(student.student_id)

            for m in marks:
                file.write(
                    f" - {m['subject']}: "
                    f"{m['marks']}/{m['max_marks']}\n"
                )

    print(f"\n✅ Report saved as: {filename}")


# Main ()


def main():
    while True:
        print_header("STUDENT MANAGEMENT SYSTEM")

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Add Marks")
        print("7. View Report Card")
        print("8. Class Statistics")
        print("9. Export Report")
        print("0. Exit")
        print()

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                menu_add_student()

            elif choice == "2":
                menu_view_all()

            elif choice == "3":
                menu_search()

            elif choice == "6":
                menu_add_marks()

            elif choice == "7":
                menu_report_card()

            elif choice == "8":
                menu_statistics()

            elif choice == "9":
                menu_export()

            elif choice == "0":
                print("\nThank you for using Student Management System!")
                break

            else:
                print("\nInvalid choice.")

        except Exception as e:
            print(f"\nError: {e}")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()