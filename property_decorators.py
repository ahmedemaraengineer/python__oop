# Prperty decorators allow us to give our class features like(getters, setters and deleters) ..

class Employee:
    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay
        # (1)
        # self.email = '{}_{}@company.com'.format(first, last)
    
    # (2)- Transforming the class attribute into a method
    # But to access the email of an employee like an attribute and not as a method 
    # We can add the decorator @property
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)    
    
    @property
    def full_name(self):
        return self.first + ' ' + self.last

    # (3)- In order to change the value of the full_name we will use a setter
    @full_name.setter # setter here means that we can give this method a value ..
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # (4)- we can use another decorator called "Deleter" which enables us to use (del) to delete somethong from our instance ...
    @full_name.deleter
    def full_name(self):
        self.first = None
        self.last = None
        print("Deleted Asset!")    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey', 'Smith', 50000)     

#(1)
# print(emp_1.first)
# print(emp_1.full_name())
# print(emp_1.email)
# emp_1.first = "Kem"
# print(emp_1.first)
# print(emp_1.full_name())
# print(emp_1.email)

# We see here that the first name of our employee has been changed successfully 
# but the email still has the old first name reserved !

# (2)
# print(emp_1.first)
# print(emp_1.full_name())
# print(emp_1.email)
# emp_1.first = "Kem"
# print(emp_1.first)
# print(emp_1.full_name())
# print(emp_1.email)

# (3)
# emp_1.full_name = "Kem Adam"
# print(emp_1.full_name)
# print(emp_1.email)

# (4)
# del emp_1.full_name