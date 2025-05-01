class Bill:
    def __init__(self,bill_id,patient_name):
        self.__bill_id=bill_id
        self.__patient_name=patient_name
        self.bill_amount=None
        self.quantity_list=[]
        self.price_list=[]

    def get_bill_id(self):
        return self.__bill_id
    def get_patient_name(self):
        return self.__patient_name
    def get_bill_amount(self):
        return self.__bill_amount
    
    def set_bill_id(self,bill_id):
        self.__bill_id = bill_id
    def set_patient_name(self,patient_name):
        self.__patient_name=patient_name
    def set_bill_amount(self,bill_amount):
        self.__bill_amount=bill_amount

    def calculate_bill_amount(self,consulation_fees,quantity_list,price_list):
        total_amount= consulation_fees+sum(quantity_list[i]*price_list[i] for i in range(len(quantity_list)))
        self.set_bill_amount(total_amount)

    def display(self):
        print(f"Bill ID :{self.get_bill_id()}")
        print(f"Patient name :{self.get_patient_name()}")
        print(f"Bill amount: {self.get_bill_amount()}")