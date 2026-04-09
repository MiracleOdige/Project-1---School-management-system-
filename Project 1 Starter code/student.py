"""
Student model for the Student Grade Management System.
"""

import logging
from exceptions import InvalidGradeError

logger = logging.getLogger("GradeManager")


class Student:
    """
    Represents a single student with their module grades.

    Attributes:
        student_id (str): Unique identifier for the student.
        name (str): Full name of the student.
        email (str): Email address (must contain '@' and '.').
        grades (dict): Maps module names to scores.
    """

    def __init__(self, student_id, name, email):
        """
        Initialise a new Student.

        Raises:
            ValueError: If any field is empty or email format is invalid.
        """
        if not student_id or not name or not email:
            raise ValueError("invalid entry.")

        if "@" not in email or "." not in email:
            raise ValueError("Invalid email.")

        self.student_id = student_id
        self.name = name
        self.email = email
        self.grades = {}
        pass

    def add_grade(self, module, score):
        """
        Record a grade for a given module.

        Args:
            module (str): Name of the module.
            score (float): Grade between 0 and 100.

        Raises:
            InvalidGradeError: If score is not between 0 and 100.
        """
        if (score != (int, float)) or score < 0 or score > 100:
            raise InvalidGradeError("grade must be between 0 and 100.")

            self.grades[module] = score

            logger.debug(
                f"Added grade {score} for module '{module}' to student {self.student_id}"
            )
        pass

    def get_average(self):
        """
        Calculate and return the student's average grade.

        Returns:
            float: The mean of all recorded grades, or 0.0 if none.
        """
        if len(self.grades) == 0:
            return 0.0

        return sum(self.grades.values()) / len(self.grades)

    pass

    def __str__(self):
        """Return a formatted string representation of the student."""
        avg = self.get_average()
        module_count = len(self.grades)

        return f"[{self.student_id}] {self.name} ({self.email}) - {module_count} module(s) - Avg: {avg:.1f}%"

    pass

    def to_dict(self):
        """Convert to dictionary for JSON serialisation."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "grades": self.grades,
        }

    pass

    @classmethod
    def from_dict(cls, data):
        """Create a Student instance from a dictionary."""
        student = cls(data["student_id"], data["name"], data["email"])

        for module, score in data.get("grades", {}).items():
            student.add_grade(module, score)

        return student

    pass
