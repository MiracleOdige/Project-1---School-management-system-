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
    """
    Manages a collection of Student objects.

    Attributes:
        students (dict): Maps student_id to Student objects.
        data_file (str): Path to the JSON file for persistence.
    """

    def __init__(self, data_file="data/students.json"):
        self.students = {}
        self.data_file = data_file
        # TODO: Call self.load_data() to restore saved students.

    def add_student(self, student):
        """
        Add a student to the grade book.

        Raises:
            DuplicateStudentError: If a student with the same ID exists.
        """
        # TODO: Check for duplicate ID, add to self.students, log.
        pass

    def remove_student(self, student_id):
        """
        Remove a student by their ID.

        Raises:
            StudentNotFoundError: If no student with that ID exists.
        """
        # TODO: Implement with error handling.
        pass

    def find_student(self, student_id):
        """
        Look up a student by ID.

        Raises:
            StudentNotFoundError: If the student is not found.
        """
        # TODO: Return the student or raise StudentNotFoundError.
        pass

    def get_all_students(self):
        """Return a list of all students."""
        # TODO: Return list(self.students.values())
        pass

    def save_data(self):
        """Save all student data to JSON."""
        # TODO: Convert each student to dict, write JSON.
        # TODO: Wrap in try/except for I/O errors.
        pass

    def load_data(self):
        """Load student data from JSON."""
        # TODO: Check if file exists, read JSON, create Students.
        # TODO: Handle FileNotFoundError, json.JSONDecodeError.
        pass


class ReportGenerator(GradeBook):
    """Extends GradeBook with reporting capabilities."""

    def class_summary(self):
        """Print a summary of all students with their averages."""
        # TODO: Loop through students, print formatted table.
        # Hint: Use a list comprehension to collect averages.
        pass

    def at_risk_report(self, threshold=40):
        """
        Identify students below the given threshold.

        Returns:
            list: Students whose average falls below the threshold.

        Hint: Use a list comprehension to filter.
        """
        # TODO: Filter students, print report, return list.
        pass

    def module_stats(self, module_name):
        """
        Calculate statistics for a specific module.

        Returns:
            dict: Contains 'average', 'highest', 'lowest', 'num_students'.

        Hint: Use a comprehension to extract scores for the module.
        """
        # TODO: Gather scores, compute stats, print and return.
        pass
