"""
Student model for the Student Grade Management System.
"""

from exceptions import InvalidGradeError


class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.grades = {}

    def add_grade(self, module_name, score):
        if not (0 <= score <= 100):
            raise InvalidGradeError("Score must be between 0 and 100.")

        self.grades[module_name] = score

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "grades": self.grades,
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data["student_id"], data["name"], data["email"])
        student.grades = data.get("grades", {})
        return student

    def __str__(self):
        return (
            f"ID: {self.student_id}, "
            f"Name: {self.name}, "
            f"Email: {self.email}, "
            f"Average: {self.calculate_average():.2f}"
        )
