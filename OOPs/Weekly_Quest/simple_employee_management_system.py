# Project 1: Creating a Simple Employee Management System
#    • Description: Introduce OOP principles by building an employee management
#                   system. Define an Employee class with attributes like name, ID, position, and salary.
#                   Implement methods to display employee details and update salary.
#    • Tasks:
#       o Create the Employee class.
#       o Implement methods to display employee details and update salary.
#       o Test the system by creating employee instances and performing operations.

class Employe:

    def __init__(self, name, id, position, salary):
        self.name = name
        self.id = id
        self.position = position
        self.salary = salary
    
    def  show_details(self):
        print("Name : ", self.name)
        print("ID : ", self.id)
        print("Position : ", self.position)
        print("Salary : ", self.salary)
        
    def update_salary(self):
        raised_salary = float(input())
        self.salary += raised_salary
        print("Salary Updated")

# Testing the code
Employe1 = Employe("Shubh", 2315510202, 'CEO', 4500000)
Employe1.show_details()
Employe1.update_salary()

