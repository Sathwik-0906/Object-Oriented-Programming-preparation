# Care hospital management wants to calculate the charge of lab tests done by its patients.
# Write a python program to implement the class diagram given below.

        

# Class Description:
# LabTestRepository class:

# list_of_hospital_lab_test_ids: Static list which contains the list of test ids of lab tests available in the hospital

# list_of_lab_test_charge: Static list which contains the charge of the lab tests available in the hospital

# The above two lists have one-to-one correspondence

# get_test_charge(lab_test_id): Accept a lab test id and return the corresponding lab test charge. If lab test id is invalid, return -1

 

# Patient class:

# list_of_lab_test_ids: Instance variable which contains the list of test ids of lab tests done by the patient

# calculate_lab_test_charge(): Calculate total charge of the lab tests done by the patient

# Calculate total lab test charge based on test charge of each lab test done by the patient

# If any lab test id provided by the patient is invalid, consider its charge to be 0

# Initialize attribute, lab_test_charge with the total lab test charge

# Note: Perform case sensitive string comparison  

# For testing:

# Create objects of Patient class

# Invoke calculate_lab_test_charge() on Patient object

# Display patient name, patient id, test ids of lab tests done by the patient and total lab test charge