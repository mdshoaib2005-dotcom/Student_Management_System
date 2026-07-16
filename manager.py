# Brain of the Student Management System

import csv                       # Used to write CSV files
import os                        # Used to create folders and check if files exists
from student import Student

STUDENTS_FILE = "data/students.csv"
MARKS_FILE = "data/marks.csv"

HEADERS_STU = ["student_id", "name", "age", "course", "email", "phone"]
HEADERS_MRK = ["student_id", "subject", "marks", "max_marks"]

class StudentManager:

    def __init__(self):
        os.makedirs("data", exist_ok=True)

        self._init_file(STUDENTS_FILE, HEADERS_STU)
        self._init_file(MARKS_FILE, HEADERS_MRK)

    def _init_file(self, filepath, headers):
        if not os.path.exists(filepath):
            with open(filepath, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(headers)

    def _load_students(self):
                                                                     # Read all students from the CSV file
        students = []

        try:
            with open(STUDENTS_FILE, "r") as file:
                reader = csv.reader(file)

                next(reader)                                         # Skip the header row

                for row in reader:
                    if row:
                        students.append(Student.from_csv_row(row))

        except FileNotFoundError:
            pass

        return students

    def _save_students(self, students):
                                                                     # Write all students back to the CSV file
        with open(STUDENTS_FILE, "w", newline="") as file:
            writer = csv.writer(file)

            # Write the header
            writer.writerow(HEADERS_STU)

            # Write each student
            for student in students:
                writer.writerow(student.to_csv_row())

    def add_student(self, student):
                                                                    # Add a new student. Returns False if the ID already exists
        students = self._load_students()

        for s in students:
            if s.student_id == student.student_id:
                return False

        students.append(student)
        self._save_students(students)

        return True

    def get_all_students(self):
                                                         # Return all students
        return self._load_students()

    def find_student(self, search_term):
                                                         # Search by Student ID or Name.
        students = self._load_students()
        results = []

        for student in students:
            if (
                    student.student_id.lower() == search_term.lower()
                    or search_term.lower() in student.name.lower()
            ):
                results.append(student)

        return results

    def update_student(self, student_id, field, new_value):
                                                                      # Update a student's information
        students = self._load_students()
        updated = False

        for student in students:
            if student.student_id == student_id:
                setattr(student, field, new_value)
                updated = True
                break

        if updated:
            self._save_students(students)

        return updated

    def delete_student(self, student_id):
                                                             # Delete a student by ID
        students = self._load_students()

        new_students = [
            student for student in students
            if student.student_id != student_id
        ]

        if len(new_students) == len(students):
            return False

        self._save_students(new_students)
        return True

    def add_marks(self, student_id, subject, marks, max_marks=100):
                                                                            # Add marks for a student

        with open(MARKS_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([student_id, subject, marks, max_marks])

    def get_marks(self, student_id):
                                                                            # Return all marks for a student

        records = []

        try:
            with open(MARKS_FILE, "r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if row["student_id"] == student_id:
                        records.append(row)

        except FileNotFoundError:
            pass

        return records

