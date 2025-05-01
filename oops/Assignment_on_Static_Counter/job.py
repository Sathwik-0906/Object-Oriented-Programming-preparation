# Problem Statement
# "Infinity" IT solution wants to automate their recruitment process. They have decided to accept 5 applications for each of the three job bands ("A", "B" and "C") in the company.

# Write a Python program to implement the class diagram given below.

                                 

# Method/Attribute description:

# Initialize static variable, applicant_id_count to 1000
# application_dict: Dictionary which store application count (value) for each job band (key)
# generate_applicant_id(): Auto-generate applicant id starting from 1001 and initialize attribute, applicant_id
# apply_for_job(job_band): Accept the job band for which the applicant is applying.
# Check if application count for the applied job band has reached the maximum limit, 5. If so, return -1.
# Else,
# increment application count for the applied job band by 1 in the dictionary
# generate applicant id and
# initialize attribute, job_band with the applied job_band
# For testing:

# Create objects of Applicant class
# Invoke apply_for_job(job_band) method on Applicant object by passing the job band for which applicant is applying
# If application is accepted, display applicant id, name and job band
# Else, display appropriate error message

class Applicant:
    __application_dict={"A": 0, "B": 5, "C": 0}
    __applicant_id_count=1000
    def __init__(self,applicant_name):
        self.__applicant_id=None
        self.__applicant_name=applicant_name
        self.__job_band=None

    def get_application_dict(self):
        return self.__application_dict
    def get_applicant_id(self):
        return self.__applicant_id
    def get_applicant_name(self):
        return self.__applicant_name
    def get_job_band(self):
        return self.__job_band
    def generate_applicant_id(self):
        Applicant.__applicant_id_count+=1
        self.__applicant_id=Applicant.__applicant_id_count
    def apply_for_job(self,job_band):
        if job_band not in Applicant.__application_dict:
            return -1
        if Applicant.__application_dict[job_band] >= 5:
            return -1
        
        Applicant.__application_dict[job_band]+=1
        self.generate_applicant_id()
        self.__job_band=job_band
        return 1
    def display(self):
        print(f"Applicant ID:{self.get_applicant_id()}")
        print(f"Applicant name:{self.get_applicant_name()}")
        print(f"Applicant JOB_band:{self.get_job_band()}")


applicants = [
    Applicant("Alice"),
    Applicant("Bob"),
    Applicant("Charlie"),
    Applicant("David"),
    Applicant("Eva"),
    Applicant("Frank")
]

for applicant in applicants:
    result = applicant.apply_for_job("A")
    if result == -1:
        print(f"Application for {applicant.get_applicant_name()} rejected. Job band full or invalid.")
    else:
        print(applicant.display())
    