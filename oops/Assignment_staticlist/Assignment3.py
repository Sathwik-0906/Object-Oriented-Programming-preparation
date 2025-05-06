# Problem Statement
# A company is in the process of providing annual hike to its employees based on incentives and performance of the employee.
# A partial python program has been written for the above requirement, complete the code by using the information and part of class diagram given below:



# Class Description:

# The program has three classes – Company, Employee and PermanentEmployee. Company and Employee classes are already coded for you. Refer starter code.

# Employee class:

# Every employee is given a performance rating (1-3) at the end of every year
# Last five year's performance rating of an employee is stored in the attribute, performance_list
#      Refer table for example and interpretation of data in performance_list, assuming current year is 2015

# Permanent Employee class:

# identify_performance_hike():
# Permanent employees are eligible for performance hike based on their last three years performance as given in table
# Identify the hike % and return it. If hike is not applicable, return None
    

# Performance for last three years

# Hike %


# identify_job_level_hike():
# Permanent employees are eligible for hike based on job level
# Identify job level based hike using the information provided in the Company class and return it. If hike cannot be identified, return None
# identify_incentive():
# Permanent employees are eligible for company level, employee level and permanent employee level incentives
# Calculate total incentive (in Rs) and return it
# calculate_salary(): Calculate total salary
# Implement it in the same way as it is implemented in Employee class
# Note: Perform case sensitive string comparison  
# For testing:

# Create objects of Company class and PermanentEmployee class

# Invoke calculate_salary() on PermanentEmployee object

# Display the details of the employee


class Company:
    # Stores hike% based on job level.
    dict_hike = {"A": 5, "B": 6, "C": 10, "D": 11}
    # Company-level incentive (private)
    __c_incentive = 5000

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_c_incentive():
        return Company.__c_incentive


class Employee:
    def __init__(self, emp_id, e_incentive, job_level, salary, performance_list):
        self.emp_id = emp_id
        self.__e_incentive = e_incentive
        self.__salary = salary
        self.__job_level = job_level
        self.__performance_list = performance_list

    def get_e_incentive(self):
        return self.__e_incentive

    def get_performance_list(self):
        return self.__performance_list

    def get_salary(self):
        return self.__salary

    def get_job_level(self):
        return self.__job_level

    def identify_performance_hike(self):
        return None

    def identify_job_level_hike(self):
        return None

    def identify_incentive(self):
        return None

    def update_salary(self, hike, incentive):
        self.__salary = (self.__salary + self.__salary * hike / 100) + incentive

    def calculate_salary(self):
        jl_hike = self.identify_job_level_hike()
        ex_hike = self.identify_performance_hike()
        if jl_hike is not None:
            hike = jl_hike
            if ex_hike is not None:
                hike += ex_hike
            incentive = self.identify_incentive()
            self.update_salary(hike, incentive)
            return True
        else:
            return False


class PermanentEmployee(Employee, Company):
    def __init__(self, emp_id, e_incentive, job_level, salary, performance_list, p_incentive):
        super().__init__(emp_id, e_incentive, job_level, salary, performance_list)
        self.__p_incentive = p_incentive

    def get_p_incentive(self):
        return self.__p_incentive

    def identify_performance_hike(self):
        performance = self.get_performance_list()
        if len(performance) < 2:
            return None
        last = performance[-1]
        second_last = performance[-2]
        third_last = performance[-3] if len(performance) >= 3 else None

        if last == 1 and second_last == 1:
            return 5
        if last == 1 and second_last == 2 and third_last == 1:
            return 3
        return None

    def identify_job_level_hike(self):
        job_level = self.get_job_level()
        return Company.dict_hike.get(job_level, None)

    def identify_incentive(self):
        return self.get_p_incentive() + Company.get_c_incentive() + self.get_e_incentive()


# ----- Testing -----

# Create Company (just for formality)
company = Company("TechCorp")

# Create a PermanentEmployee
# Performance: [1, 2, 1, 1, 1] => last 3 years: [1, 1, 1] => 5% hike
# Job Level: "B" => 6% hike
# e_incentive: 3000, p_incentive: 2000, c_incentive: 5000 => Total incentive: 10000
emp = PermanentEmployee("EMP101", 3000, "B", 40000, [1, 2, 1, 1, 1], 2000)

# Calculate salary
if emp.calculate_salary():
    print("Salary calculation successful.")
    print("Updated Salary:", emp.get_salary())
else:
    print("Salary calculation failed due to invalid job level.")

