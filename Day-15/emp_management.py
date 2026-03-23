class employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id= emp_id
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary *0.10
    
class manager(employee):
    def __init__(self, emp_id, name, salary,department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def calculate_bonus(self):
        return self.salary * 0.20
    
e1 = employee (201,'vicky',5000)
m1= manager (301,'ravi',80000,'sales')

print('employee bonus:',e1.calculate_bonus())
print("manager bonus: ",m1.calculate_bonus())