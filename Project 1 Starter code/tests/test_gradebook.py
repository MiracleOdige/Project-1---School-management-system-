"""
Test Suite for Project 1: Student Grade Management System
Run with: python -m unittest tests/test_gradebook.py -v

Your team must write at least 10 meaningful test cases.
The stubs below give you a starting structure.
"""

import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from student import Student
from gradebook import GradeBook, ReportGenerator
from exceptions import DuplicateStudentError, InvalidGradeError, StudentNotFoundError


class TestStudent(unittest.TestCase):

    def test_create_valid_student(self):
        """A student with valid details should be created successfully."""
        pass

    def test_create_student_empty_name_raises(self):
        """Creating a student with an empty name should raise ValueError."""
        pass

    def test_create_student_invalid_email_raises(self):
        """An email without '@' or '.' should raise ValueError."""
        pass

    def test_add_valid_grade(self):
        """Adding a grade between 0-100 should succeed."""
        pass

    def test_add_invalid_grade_raises(self):
        """A grade outside 0-100 should raise InvalidGradeError."""
        pass

    def test_get_average_with_grades(self):
        """Average should be correctly calculated."""
        pass

    def test_get_average_no_grades(self):
        """Average should return 0.0 when no grades exist."""
        pass

    def test_to_dict_and_from_dict(self):
        """Round-trip through dict should preserve all data."""
        pass


class TestGradeBook(unittest.TestCase):

    def test_add_student(self):
        """Adding a student should make them retrievable."""
        pass

    def test_add_duplicate_raises(self):
        """Duplicate ID should raise DuplicateStudentError."""
        pass

    def test_remove_student(self):
        """Removing a student should make them unfindable."""
        pass

    def test_find_nonexistent_raises(self):
        """Searching for a missing student should raise."""
        pass

    def test_save_and_load_data(self):
        """Saving and loading should preserve student data."""
        pass


class TestReportGenerator(unittest.TestCase):

    def test_at_risk_report(self):
        """Students below threshold should appear in the report."""
        pass

    def test_module_stats(self):
        """Module statistics should return correct values."""
        pass


if __name__ == "__main__":
    unittest.main()
