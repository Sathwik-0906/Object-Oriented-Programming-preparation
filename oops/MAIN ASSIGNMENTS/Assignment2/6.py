# Problem Statement
# Infosys wants to automate the visitor management process in the campus. An employee can register only one visitor at a time. Employee should register the visitor details in advance so that the security team will have the details when the visitors arrive in the campus.
# Write a python program to implement the class diagram given below.



# Class description
# Security class:

# employee_list: Static list which contains the list of employees in the company. Initialize it to an empty list

# visitor_list: Static list which contains the objects of visitor who are registered by the employees. Initialize it to an empty list. There is one-to-one correspondence between the two lists

# Constructor: Initialize Security.employee_list using the value passed to it. Initialize Security.visitor_list with a list of same size as that of Employee.employee_list containing None in all index positions.

# security_check(employee,visitor): Check the visitor details at the time of arrival against the registered details based on the rules given below.

# The given employee should be present in Security,employee_list

# If present, employee should have already registered the given visitor

# If registered, visitor should have a valid id proof. Valid id proofs are "Passport", "Voter id" and "PAN Card"

# Employee class:
# register_visitor(visitor): Register the given visitor based on the rules given below.

# Employee should be present in Security.employee_list. [Hint: validate using employee_id]

# Employee should not have registered any visitor

# Validate the relationship of the visitor with the employee. Relationship can be "Parent", "Sibling", "Spouse" or "Child"

# If all the above three rules are satisfied, update the visitor object in Security.visitor_list at the index position corresponding to the employee and return true


# If all the rules are satisfied return true. Else return false.
# Perform case sensitive comparison.
# Create objects of Employee, Visitor and Security classes, invoke appropriate methods and test your program.


class Consultant:
    registered_company_list = ["Infosys", "TCS", "Wipro"]
    vacancy_list = [2, 1, 3]
    registered_student_dict = {}

    def validate_vacancy(self, company_name):
        try:
            index = Consultant.registered_company_list.index(company_name)
            if Consultant.vacancy_list[index] > 0:
                return index
            else:
                return -1
        except ValueError:
            return -1

    def register_student_for_placement(self, index, student_id):
        company = Consultant.registered_company_list[index]
        Consultant.vacancy_list[index] -= 1
        if company in Consultant.registered_student_dict:
            Consultant.registered_student_dict[company].append(student_id)
        else:
            Consultant.registered_student_dict[company] = [student_id]

class Student:
    def __init__(self, student_id, aggregate_percentage, year_of_passing):
        self.student_id = student_id
        self.aggregate_percentage = aggregate_percentage
        self.year_of_passing = year_of_passing

    def check_eligibility(self):
        return self.aggregate_percentage >= 65 and self.year_of_passing == 2015

    def apply_for_job(self, company_name, consultant):
        index = consultant.validate_vacancy(company_name)
        if index == -1:
            return -1
        if self.check_eligibility():
            consultant.register_student_for_placement(index, self.student_id)
        else:
            return -1


consultant = Consultant()

student1 = Student("S001", 70, 2015)
student2 = Student("S002", 60, 2015)
student3 = Student("S003", 75, 2016)
student4 = Student("S004", 80, 2015)

student1.apply_for_job("Infosys", consultant)
student2.apply_for_job("TCS", consultant)
student3.apply_for_job("Wipro", consultant)
student4.apply_for_job("TCS", consultant)

print(Consultant.registered_student_dict)
print(Consultant.vacancy_list)
