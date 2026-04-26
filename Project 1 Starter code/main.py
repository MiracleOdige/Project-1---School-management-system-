import logging
import os

from student import Student
from gradebook import ReportGenerator
from exceptions import DuplicateStudentError, StudentNotFoundError, InvalidGradeError

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("GradeManager")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("logs/grade_manager.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


def display_menu():
    print("\n" + "=" * 50)
    print("   Student Grade Management System")
    print("=" * 50)
    print("1. Add a new student")
    print("2. Record a grade")
    print("3. View all students")
    print("4. Search for a student")
    print("5. Remove a student")
    print("6. Class summary report")
    print("7. At-risk students report")
    print("8. Module statistics")
    print("9. Save and exit")
    print("=" * 50)


def main():
    """Main application loop."""
    report = ReportGenerator()

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-9): ").strip()

        if choice == "1":
            try:
                student_id = input("Enter student ID: ").strip()
                name = input("Enter student name: ").strip()
                email = input("Enter student email: ").strip()

                student = Student(student_id, name, email)
                report.add_student(student)

                print(f"\nStudent {name} added successfully.")

            except (ValueError, DuplicateStudentError) as e:
                print(f"Error: {e}")
                logger.error(e)

        elif choice == "2":
            try:
                student_id = input("Enter student ID: ").strip()
                module_name = input("Enter module name: ").strip()
                score = int(input("Enter score: ").strip())

                student = report.find_student(student_id)
                student.add_grade(module_name, score)

                print(f"\nGrade added for {student.name}.")

            except (StudentNotFoundError, InvalidGradeError, ValueError) as e:
                print(f"Error: {e}")
                logger.error(e)

        elif choice == "3":
            students = report.get_all_students()

            if not students:
                print("\nNo students found.")
            else:
                print("\nALL STUDENTS")
                print("-" * 50)
                for student in students:
                    print(student)

        elif choice == "4":
            try:
                student_id = input("Enter student ID: ").strip()
                student = report.find_student(student_id)

                print("\nSTUDENT DETAILS")
                print("-" * 50)
                print(student)
                print("Grades:", student.grades)

            except StudentNotFoundError as e:
                print(f"Error: {e}")
                logger.error(e)

        elif choice == "5":
            try:
                student_id = input("Enter student ID: ").strip()
                report.remove_student(student_id)

                print("\nStudent removed successfully.")

            except StudentNotFoundError as e:
                print(f"Error: {e}")
                logger.error(e)

        elif choice == "6":
            report.class_summary()

        elif choice == "7":
            try:
                threshold_input = input("Enter threshold (default 40): ").strip()

                threshold = float(threshold_input) if threshold_input else 40
                report.at_risk_report(threshold)

            except ValueError:
                print("Invalid threshold. Please enter a number.")

        elif choice == "8":
            module_name = input("Enter module name: ").strip()
            report.module_stats(module_name)

        elif choice == "9":
            report.save_data()
            print("\nData saved. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
