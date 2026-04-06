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
        # TODO: Validate that no field is empty.
        # TODO: Validate email format (must contain '@' and '.').
        # TODO: Assign attributes and initialise an empty grades dict.
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
        # TODO: Validate score is a number and in range 0-100.
        # TODO: Add to self.grades dict.
        # TODO: Log the grade addition at DEBUG level.
        pass

    def get_average(self):
        """
        Calculate and return the student's average grade.

        Returns:
            float: The mean of all recorded grades, or 0.0 if none.
        """
        # TODO: Use sum() and len() to compute the average.
        # Hint: Handle the case where the student has no grades.
        pass

    def __str__(self):
        """Return a formatted string representation of the student."""
        # TODO: Use an f-string to return something like:
        #       "[STU001] Jane Smith (jane@email.com) - 3 module(s) - Avg: 82.5%"
        pass

    def to_dict(self):
        """Convert to dictionary for JSON serialisation."""
        # TODO: Return a dict with keys: student_id, name, email, grades
        pass

    @classmethod
    def from_dict(cls, data):
        """Create a Student instance from a dictionary."""
        # TODO: Create a Student, loop through data["grades"]
        #       and call add_grade() for each.
        pass
