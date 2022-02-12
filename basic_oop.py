# Here we will discuss the basics of Object-Oriented Programming (OOP)
# Discussing class initialization, variables, and methods

class Employee:
    # defining class variables :
    # Like the instance variables, class variables are variables that are shared among all the class instances .
    raise_amount = 1.04
    # Initialize the number of instances :
    num_of_emps = 0

    # Initialization of our class ..
    # Giving the attributes which are have to be shared among all class instances .
    def __init__(self, first: str, last: str, pay: int):
        # Giving its attributes ..
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '_' + last + '@company.com'
        # Incrementing the number of employees by 1 for every call for the init method :
        Employee.num_of_emps += 1

    def full_name(self):
        return self.first + ' ' + self.last

    # 1- Using a constant
    # def apply_raise(self):
    #     self.pay = int(self.pay * 1.04)

    # 2- Using a class variable
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # in this method we are dealing with the class instead of the instance :
    # We can use the class method to update
    # our class variables that will be shared among the instances that we are going to deal with .
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    # Suppose that we want to pass in a date and we want to know whether this
    # day is a working day or not :
    # Here we want to declare a method that doesn't need the instance to be
    # passed in but it has a logical connection with the class
    # Here we will use the ("static method")
    # Notice that it doesn't need (self) to be passed in

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


emp_1 = Employee("khan", "academy", 10000)
emp_2 = Employee("mike", "joey", 20000)

# We can update the class variable :
# Employee.raise_amount = 1.6
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# emp_1.apply_raise()
# We can update the class variable for only one instance :
# emp_1.raise_amount = 1.6
# print(emp_1.pay)

# print (Employee.raise_amount)
# print(emp_1.__dict__)
# print(Employee.__dict__)
# print(Employee.num_of_emps)

# We can update our class variable using our class method which we have created :
# Employee.set_raise_amt(1.7)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# Creating class instances from a string that contains all the information :

# emp_str_1 = "John-Doe-70000"
# emp_str_2 = "Steve-Smith-30000"
# emp_str_3 = "Jane-Doe-90000"
#
# first, last, pay = emp_str_1.split('-')
# pay = int(pay)
# new_emp_1 = Employee(first, last, pay)
# new_emp_1.apply_raise()
# print(new_emp_1.pay)

# new_emp_2 = Employee.from_string("John-stat-5000")
# print(new_emp_2.email)
# print(new_emp_2.pay)

# import datetime
#
# my_date = datetime.date(2016, 7, 10)
# print(Employee.is_workday(my_date))
