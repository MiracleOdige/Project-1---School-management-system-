"""
Custom exceptions for the Student Grade Management System.
"""


class DuplicateStudentError(Exception):
    """Raised when attempting to add a student with an ID that already exists."""
    pass


class InvalidGradeError(Exception):
    """Raised when a grade value is outside the valid range (0-100)."""
    pass


class StudentNotFoundError(Exception):
    """Raised when a student lookup fails."""
    pass
