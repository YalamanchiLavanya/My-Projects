# University Management System Using OOPs
from abc import ABC, abstractmethod
# Administrator Class
class Administrator(ABC):
    @abstractmethod
    def details(self):
        pass
# Course Class
class Course:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
    # Course Details
    def display_course(self):
        print("\n--- Course Details ---")
        print(f"Course ID   : {self.course_id}")
        print(f"Course Name : {self.course_name}")
        print(f"Credits     : {self.credits}")
# Student Class
class Student(Administrator):
    """This class stores Student data"""
    def __init__(self, name,department, student_id, university, year_of_joining, dob):
        self.name = name
        self.department = department
        self.student_id = student_id
        self.university = university
        self.year_of_joining = year_of_joining
        self.dob = dob
        self.__courses = []
        self.__grades = {}
    # Student Details
    def details(self):
        print("\n--- Student Details ---")
        print(f"Name            : {self.name}")
        print(f"Department      : {self.department}")
        print(f"Student ID      : {self.student_id}")
        print(f"University      : {self.university}")
        print(f"Year of Joining : {self.year_of_joining}")
        print(f"Date of Birth   : {self.dob}")
    # Enroll Course
    def enroll(self, course):
        if course not in self.__courses:
            self.__courses.append(course)
            print(f"\n{self.name} enrolled in {course.course_name}")
        else:
            print("\nStudent is already enrolled in this course")
    # View Schedule
    def view_schedule(self):
        print(f"\n Schedule of {self.name}")
        if len(self.__courses) == 0:
            print("No courses enrolled")
        else:
            for course in self.__courses:
                print(f"{course.course_id}-{course.course_name}")
    # Add Grade
    def add_grade(self, course, grade):
        self.__grades[course.course_id] = grade
    # Check Grades
    def check_grades(self):
        print(f"\n Grades of {self.name}")
        if len(self.__grades) == 0:
            print("No grades available")
        else:
            for course_id, grade in self.__grades.items():
                print(f"Course ID:{course_id}|Grade:{grade}")
# Undergraduate Student Class
class UndergraduateStudent(Student):
    """This class represents Undergraduate students"""
    # Enroll Course
    def enroll(self, course):
        print("\nUndergraduate Student Enrollment")
        super().enroll(course)
    # View Schedule
    def view_schedule(self):
        print("\nUndergraduate Student Schedule")
        super().view_schedule()
# Graduate Student Class
class GraduateStudent(Student):
    """This class represents Graduate students"""
    # Enroll Course
    def enroll(self, course):
        print("\nGraduate Student Enrollment")
        super().enroll(course)
    # View Schedule
    def view_schedule(self):
        print("\nGraduate Student Schedule")
        super().view_schedule()
# Faculty Class
class Faculty(Administrator):
    """This class stores Faculty data"""
    def __init__(self, name, faculty_id, department):
        self.name = name
        self.faculty_id = faculty_id
        self.department = department
        self.__courses = []
        self.__students = []
    # Faculty Details
    def details(self):
        print("\n Faculty Details ")
        print(f"Name       : {self.name}")
        print(f"Faculty ID : {self.faculty_id}")
        print(f"Department : {self.department}")
    # Assign Course
    def assign_course(self, course):
        if course not in self.__courses:
            self.__courses.append(course)
            print(f"\n{course.course_name} assigned to {self.name}")
        else:
            print("\nCourse is already assigned")
    # Add Student
    def add_student(self, student):
        if student not in self.__students:
            self.__students.append(student)
            print(f"\n{student.name} added to faculty roster")
        else:
            print("\nStudent is already in the roster")
    # Course Assignments
    def view_course_assignments(self):
        print(f"\n Courses assigned to {self.name}")
        if len(self.__courses) == 0:
            print("No courses assigned")
        else:
            for course in self.__courses:
                print(f"{course.course_id} - {course.course_name}")
    # Student Roster
    def view_student_roster(self):
        print(f"\n student Roster of {self.name}")
        if len(self.__students) == 0:
            print("No students in roster")
        else:
            for student in self.__students:
                print(f"{student.student_id} - {student.name}")
# University Class
class University:
    """This class stores University data"""
    def __init__(self, university_name):
        self.university_name = university_name
        self.students = []
        self.courses = []
        self.faculties = []
    # Add Student
    def add_student(self, student):
        self.students.append(student)
        print(f"\n{student.name} added to university")
    # Add Course
    def add_course(self, course):
        self.courses.append(course)
        print(f"\n{course.course_name} added to university")
    # Add Faculty
    def add_faculty(self, faculty):
        self.faculties.append(faculty)
        print(f"\n{faculty.name} added to university")
    # University Details
    def display_university(self):
        print("\n University Details ")
        print(f"University Name : {self.university_name}")
        print(f"Total Students : {len(self.students)}")
        print(f"Total Courses  : {len(self.courses)}")
        print(f"Total Faculty  : {len(self.faculties)}")
# Department Class
class Department(University):
    """This class represents Department"""
    def __init__(self, university_name, department_name):
        super().__init__(university_name)
        self.department_name = department_name
    # Department Details
    def display_department(self):
        print("\n Department Details")
        print(f"University : {self.university_name}")
        print(f"Department : {self.department_name}")
# University Object
university = University("ABC University")
# Course Objects
course1 = Course("CSE101", "Python Programming", 4)
course2 = Course("CSE102", "Database Management", 3)
course3 = Course("CSE103", "Data Structures", 4)
# Course Details
course1.display_course()
course2.display_course()
course3.display_course()
# Student Objects
student1 = UndergraduateStudent("Lavanya", "Computer Science", 101, "ABC University", 2026, "25-11-2004")
student2 = GraduateStudent("Rahul", "Computer Science", 102, "ABC University", 2026, "10-05-2003")

# Student Details
student1.details()
student2.details()
# Add Students
university.add_student(student1)
university.add_student(student2)
# Add Courses
university.add_course(course1)
university.add_course(course2)
university.add_course(course3)
# Student Enrollment
student1.enroll(course1)
student1.enroll(course2)
student2.enroll(course2)
student2.enroll(course3)
# Student Schedule
student1.view_schedule()
student2.view_schedule()
# Student Grades
student1.add_grade(course1, "A")
student1.add_grade(course2, "A+")
student2.add_grade(course2, "B+")
student2.add_grade(course3, "A")
# Check Grades
student1.check_grades()
student2.check_grades()
# Faculty Objects
faculty1 = Faculty("Dr. Kumar", "F101", "Computer Science")
faculty2 = Faculty("Dr. Priya", "F102", "Computer Science")
# Faculty Details
faculty1.details()
faculty2.details()
# Add Faculty
university.add_faculty(faculty1)
university.add_faculty(faculty2)
# Assign Courses
faculty1.assign_course(course1)
faculty1.assign_course(course2)
faculty2.assign_course(course3)
# Add Students to Faculty
faculty1.add_student(student1)
faculty1.add_student(student2)
faculty2.add_student(student1)
# Course Assignments
faculty1.view_course_assignments()
faculty2.view_course_assignments()
# Student Roster
faculty1.view_student_roster()
faculty2.view_student_roster()
# University Details
university.display_university()
# Department Object
department = Department("ABC University", "Computer Science")
# Department Details
department.display_department()
