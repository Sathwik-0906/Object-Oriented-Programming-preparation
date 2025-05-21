# Problem Statement
# The consultants of WeHire Company help students to get placements in companies registered with it. There are multiple companies registered in WeHire. Students are registered for placement based their on choice of company and vacancies available in those companies.
# Write a python program to implement the class diagram given below.



# Class description:
# Consultant class:

# registered_company_list: List containing names of registered companies
# vacancy_list: List containing number of vacancies in registered companies. There is one to one correspondence between the two lists
# registered_student_dict: Dictionary which stores the company name as key and list of ids of students who have registered with that company as value.
# validate_vacancy(company_name): Check for vacancy in the given company. If available, return the index position of the company in registered_company_list. Else, return -1
# register_student_for_placement(index,student_id): Register the given student id in the company whose index position is passed to the method.
# Update vacancy_list of the company
# Update registered_student_dict so as to add the given student id to the student list of the company
# Student class:

# check_eligibility(): The students can register for a company only they have minimum aggregate percentage of 65 and their year of passing is 2015.
# If the above two conditions are satisfied, return true. Else return false.
# apply_for_job(company_name,consultant): Apply for job in the given company through the given consultant.
# Check if vacancy is available in the given company. (Hint: Invoke consultant.validate_vacancy())
# If available, check if the student is eligible
# If eligible, register the student for placement by invoking appropriate method of consultant
# Else return -1
# Else return -1
# Create objects of Student and Consultant class, invoke appropriate methods and test your program.

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
