def calculate_gpa(grades):
    grade_points = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0,
    }
    total_points = sum(grade_points[grade] for grade in grades)
    return total_points / len(grades)


def main():
    grades = input("Enter your letter grades separated by commas (A, B, C, D, F): ")
    grades = [grade.strip().upper() for grade in grades.split(",")]

    valid_grades = ("A", "B", "C", "D", "F")
    if not grades or any(grade not in valid_grades for grade in grades):
        print("Please enter only A, B, C, D, or F.")
        return

    gpa = calculate_gpa(grades)
    print(f"Your GPA is {gpa:.2f} out of 4.00.")


main()
