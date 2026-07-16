# Calculate_grade()

def calculate_grade(percentage):
   # Return grade and remark based on percentage

    if percentage >= 90:
        return "A+", "Outstanding"

    elif percentage >= 80:
        return "A", "Excellent"

    elif percentage >= 70:
        return "B", "Very Good"

    elif percentage >= 60:
        return "C", "Good"

    elif percentage >= 50:
        return "D", "Pass"

    elif percentage >= 40:
        return "E", "Marginal Pass"

    else:
        return "F", "Fail"


# Test Code
#if __name__ == "__main__":
#    print(calculate_grade(95))
#    print(calculate_grade(82))
#    print(calculate_grade(71))
#    print(calculate_grade(58))
#    print(calculate_grade(39))


# generate_report_card()

def generate_report_card(student, marks_records):
    """Print a formatted report card."""

    print()
    print("*" * 62)
    print("*" + " STUDENT REPORT CARD ".center(60) + "*")
    print("*" * 62)

    print(f"Student ID : {student.student_id}")
    print(f"Name       : {student.name}")
    print(f"Course     : {student.course}")
    print(f"Age        : {student.age}")

    print("-" * 62)

    print(f"{'Subject':<25}{'Marks':>10}{'Max':>10}{'%':>10}")

    print("-" * 62)

    total_marks = 0
    total_max = 0

    for record in marks_records:

        subject = record["subject"]
        marks = float(record["marks"])
        maximum = float(record["max_marks"])

        percentage = (marks / maximum) * 100

        total_marks += marks
        total_max += maximum

        print(f"{subject:<25}{marks:>10.1f}{maximum:>10.0f}{percentage:>9.1f}%")

    print("-" * 62)

    if total_max > 0:

        overall_percentage = (total_marks / total_max) * 100

        grade, remark = calculate_grade(overall_percentage)

        print(f"Total Marks : {total_marks:.1f} / {total_max:.0f}")
        print(f"Percentage  : {overall_percentage:.2f}%")
        print(f"Grade       : {grade}")
        print(f"Remark      : {remark}")

    else:
        print("No marks available.")

    print("*" * 62)

    return total_marks, total_max


# Grade_Calculator_Function()


def get_class_statistics(manager):
    """Calculate class-wide statistics."""

    students = manager.get_all_students()

    if not students:
        return None

    stats = []

    for student in students:

        marks = manager.get_marks(student.student_id)

        if marks:

            total = sum(float(m["marks"]) for m in marks)
            maximum = sum(float(m["max_marks"]) for m in marks)

            percentage = (total / maximum) * 100 if maximum > 0 else 0

            grade, _ = calculate_grade(percentage)

            stats.append({
                "name": student.name,
                "id": student.student_id,
                "percentage": percentage,
                "grade": grade
            })

    if not stats:
        return None

    average = sum(s["percentage"] for s in stats) / len(stats)

    top_student = max(stats, key=lambda x: x["percentage"])

    passed = sum(1 for s in stats if s["percentage"] >= 40)

    failed = len(stats) - passed

    return {
        "total_students": len(students),
        "with_marks": len(stats),
        "average_pct": round(average, 2),
        "top_student": top_student,
        "passed": passed,
        "failed": failed,
        "all_stats": sorted(
            stats,
            key=lambda x: x["percentage"],
            reverse=True
        )
    }


