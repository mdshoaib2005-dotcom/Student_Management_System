class Student:
    """Represents a single student."""

    def __init__(self, student_id, name, age, course, email, phone=''):
        self.student_id = student_id
        self.name = name
        self.age = int(age)
        self.course = course
        self.email = email
        self.phone = phone

    def to_csv_row(self):
        return [
            self.student_id,
            self.name,
            self.age,
            self.course,
            self.email,
            self.phone
        ]

    @classmethod
    def from_csv_row(cls, row):
        return cls(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5] if len(row) > 5 else ''
        )

    def __str__(self):
        return (
            f"ID: {self.student_id} | "
            f"Name: {self.name} | "
            f"Age: {self.age} | "
            f"Course: {self.course}"
        )


if __name__ == "__main__":
    s = Student(
        "S001",
        "Rahul Sharma",
        20,
        "B.Tech CS",
        "rahul@email.com"
    )

    print(s)

    print("CSV Row:", s.to_csv_row())

    s2 = Student.from_csv_row([
        "S002",
        "Priya Singh",
        "19",
        "BCA",
        "priya@email.com"
    ])

    print(s2)