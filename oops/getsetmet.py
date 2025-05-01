class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None
        self.__course_id = None
        self.__fees = None

    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks

    def get_age(self):
        return self.__age

    def get_course_id(self):
        return self.__course_id

    def get_fees(self):
        return self.__fees

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_marks(self, marks):
        self.__marks = marks

    def set_age(self, age):
        self.__age = age

    def set_course_id(self, course_id):
        self.__course_id = course_id

    def set_fees(self, fees):
        self.__fees = fees

    def validate_marks(self):
        return self.__marks is not None and 0 <= self.__marks <= 100

    def validate_age(self):
        return self.__age is not None and self.__age > 20

    def check_qualification(self):
        return self.validate_marks() and self.validate_age() and self.__marks >= 65

    def choose_course(self, course_id):
        course_fees = {1001: 25575.0, 1002: 15500.0}
        if course_id in course_fees:
            self.set_course_id(course_id)
            self.set_fees(course_fees[course_id])
            return True
        return False


# Testing the class
maddy = Student()
maddy.set_student_id(1004)
maddy.set_age(21)
maddy.set_marks(65)

if maddy.check_qualification():
    print("Student has qualified")
    if maddy.choose_course(1002):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")
