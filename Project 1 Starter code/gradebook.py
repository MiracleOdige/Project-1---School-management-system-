"""
GradeBook and ReportGenerator classes for the Student Grade Management System.
"""

import json
import logging
import os

from student import Student
from exceptions import DuplicateStudentError, StudentNotFoundError

logger = logging.getLogger("GradeManager")


class GradeBook:

    def __init__(self, data_file="data/students.json"):
        self.students = {}
        self.data_file = data_file
        self.load_data()

    def add_student(self, student):

        if student.student_id in self.students:
            raise DuplicateStudentError(
                f"Student with ID {student.student_id} already exists."
            )

        self.students[student.student_id] = student
        logger.info(f"Added student: {student.name} ({student.student_id})")

    def remove_student(self, student_id):

        if student_id not in self.students:
            raise StudentNotFoundError(f"Student with ID {student_id} not found.")

        removed = self.students.pop(student_id)
        logger.info(f"Removed student: {removed.name} ({student_id})")

    def find_student(self, student_id):

        if student_id not in self.students:
            raise StudentNotFoundError(f"Student with ID {student_id} not found.")

        return self.students[student_id]

    def get_all_students(self):

        return list(self.students.values())

    def save_data(self):

        try:
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)

            data = [student.to_dict() for student in self.students.values()]

            with open(self.data_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            logger.info("Student data saved successfully.")

        except OSError as e:
            logger.error(f"Error saving data: {e}")

    def load_data(self):

        try:
            if not os.path.exists(self.data_file):
                logger.warning("Data file not found. Starting fresh.")
                return

            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            for student_data in data:
                student = Student.from_dict(student_data)
                self.students[student.student_id] = student

            logger.info("Student data loaded successfully.")

        except FileNotFoundError:
            logger.warning("Data file not found.")
        except json.JSONDecodeError:
            logger.error("Error decoding JSON data.")


class ReportGenerator(GradeBook):

    def class_summary(self):

        print("\nCLASS SUMMARY")
        print("-" * 50)
        print(f"{'ID':<10}{'Name':<20}{'Average':<10}")
        print("-" * 50)

        averages = [student.calculate_average() for student in self.students.values()]

        for student in self.students.values():
            print(
                f"{student.student_id:<10}"
                f"{student.name:<20}"
                f"{student.calculate_average():<10.2f}"
            )

        if averages:
            print("-" * 50)
            print(f"Class Average: {sum(averages) / len(averages):.2f}")

    def at_risk_report(self, threshold=40):

        at_risk = [
            student
            for student in self.students.values()
            if student.calculate_average() < threshold
        ]

        print(f"\nAT RISK STUDENTS (Below {threshold})")
        print("-" * 50)

        for student in at_risk:
            print(
                f"{student.student_id} - {student.name} "
                f"({student.calculate_average():.2f})"
            )

        return at_risk

    def module_stats(self, module_name):

        scores = [
            student.grades[module_name]
            for student in self.students.values()
            if module_name in student.grades
        ]

        if not scores:
            print(f"No scores found for module: {module_name}")
            return {}

        stats = {
            "average": sum(scores) / len(scores),
            "highest": max(scores),
            "lowest": min(scores),
            "num_students": len(scores),
        }

        print(f"\nMODULE STATS: {module_name}")
        print("-" * 50)
        for key, value in stats.items():
            print(
                f"{key.capitalize()}: {value:.2f}"
                if isinstance(value, float)
                else f"{key.capitalize()}: {value}"
            )

        return stats
