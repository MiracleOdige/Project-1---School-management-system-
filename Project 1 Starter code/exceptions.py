"""
Student Grade Management System with Custom Exceptions
"""

# --- Student Management System ---


class DuplicateStudentError(Exception):
    pass


class StudentNotFoundError(Exception):
    pass


class InvalidGradeError(Exception):
    pass


class StudentManager:
    def __init__(self):
        self.students = {}  # Dictionary: {student_id: {"name": str, "grade": float}}

    def add_student(self, student_id, name):
        if student_id in self.students:
            raise DuplicateStudentError(f"Student ID {student_id} already exists.")

        self.students[student_id] = {"name": name, "grade": None}
        print(f"Student '{name}' added successfully.")

    def assign_grade(self, student_id, grade):
        if student_id not in self.students:
            raise StudentNotFoundError(f"Student ID {student_id} not found.")

        if not (0 <= grade <= 100):
            raise InvalidGradeError("Grade must be between 0 and 100.")

        self.students[student_id]["grade"] = grade
        print(f"Grade {grade} assigned to {self.students[student_id]['name']}.")

    def get_student(self, student_id):
        if student_id not in self.students:
            raise StudentNotFoundError(f"Student ID {student_id} not found.")

        return self.students[student_id]

    def display_all_students(self):
        if not self.students:
            print("No students found.")
            return

        for sid, info in self.students.items():
            print(f"ID: {sid}, Name: {info['name']}, Grade: {info['grade']}")
