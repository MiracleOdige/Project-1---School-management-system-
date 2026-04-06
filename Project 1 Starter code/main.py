"""
Project 1: Student Grade Management System
Entry point. Run with: python main.py
"""

import logging
import os

from student import Student
from gradebook import ReportGenerator
from exceptions import (
    DuplicateStudentError, InvalidGradeError, StudentNotFoundError,
)

# ── Logging setup ──
# TODO: Configure logging to write to BOTH console AND file.
#       Console: INFO level, File: DEBUG level
#       Format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

logger = logging.getLogger("GradeManager")
# Your logging configuration here...


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
            # TODO: Prompt for student_id, name, email
            # TODO: Create Student and add to report (GradeBook)
            # TODO: Wrap in try/except for ValueError, DuplicateStudentError
            pass

        elif choice == "2":
            # TODO: Prompt for student_id, module name, score
            # TODO: Find the student and call add_grade()
            pass

        elif choice == "3":
            # TODO: Loop through get_all_students() and print each
            pass

        elif choice == "4":
            # TODO: Prompt for student_id, display student and grades
            pass

        elif choice == "5":
            # TODO: Prompt for student_id and remove
            pass

        elif choice == "6":
            # TODO: Call class_summary()
            pass

        elif choice == "7":
            # TODO: Optionally prompt for threshold, call at_risk_report()
            pass

        elif choice == "8":
            # TODO: Prompt for module name, call module_stats()
            pass

        elif choice == "9":
            report.save_data()
            print("\nData saved. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
