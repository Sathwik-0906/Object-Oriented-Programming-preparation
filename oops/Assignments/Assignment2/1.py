class Employee:
    employee_count = 1000

    def __init__(self):
        self.employee_id = None

    def generate_employee_id(self):
        Employee.employee_count += 1
        self.employee_id = "E" + str(Employee.employee_count)


class Project:
    def __init__(self, project_id):
        self.project_id = project_id
        self.number_of_employees = 0

    def update_number_of_employees(self):
        self.number_of_employees += 1


class Department:
    dep_project_list = []
    employee_dict = {}

    @staticmethod
    def add_project(project_list):
        if len(Department.dep_project_list) + len(project_list) <= 5:
            Department.dep_project_list.extend(project_list)
        else:
            return -1

    @staticmethod
    def add_employee(employee, project_id):
     
        project_found = None
        for proj in Department.dep_project_list:
            if proj.project_id == project_id:
                project_found = proj
                break

        if not project_found:
            print(f"Project with ID {project_id} not found in department.")
            return -1

       
        if project_found.number_of_employees >= 10:
            print(f"Cannot add employee: Project {project_id} already has 10 employees.")
            return -2

       
        employee.generate_employee_id()
        Department.employee_dict[employee.employee_id] = project_id
        project_found.update_number_of_employees()




p1 = Project("P100")
p2 = Project("P101")
p3 = Project("P102")


project_list = [p1, p2, p3]
add_proj_result = Department.add_project(project_list)
if add_proj_result == -1:
    print("Cannot add projects: limit exceeded")

for i in range(11): 
    emp = Employee()
    result = Department.add_employee(emp, "P100")
    if result == -2:
        print(f"Employee {i+1} could not be added: Project full")
    elif result == -1:
        print(f"Employee {i+1} could not be added: Project not found")


print("\nEmployee allocations:")
for emp_id, proj_id in Department.employee_dict.items():
    print(f"{emp_id} -> {proj_id}")