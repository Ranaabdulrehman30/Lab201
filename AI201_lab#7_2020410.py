class Employee:

    def __init__(self, name=" ", emp_no=0, salary=0):
        self._name = name
        self._emp_no = emp_no
        self._salary = salary

    def set_name(self, name):
        self._name = name

    def set_emp_no(self, emp_no):
        self._emp_no = emp_no

    def set_salary(self, salary):
        self._salary = salary

    def get_name(self):
        return self._name

    def get_emp_no(self):
        return self._emp_no

    def get_salary(self):
        return self._salary

    def show_data(self):
        print("Name :" + str(self.get_name()))
        print("Employee No : " + str(self.get_emp_no()))
        print("Salary : " + str(self.get_salary()))

class Graduate:

    def __init__(self, school=" ", degree=""):
        self._school = school
        self._degree = degree

    def set_school(self, school):
        self._school = school

    def set_degree(self, degree):
        self._degree = degree

    def get_school(self):
        return self._school

    def get_degree(self):
        return self._degree

    def show_data(self):
        print("School :" + str(self.get_school()))
        print("Degree : " + str(self.get_degree()))

class Manager(Employee, Graduate):

    def __init__(self, name, emp_no, salary, profession):
        self._profession = profession
        Employee.__init__(self, name, emp_no, salary)

    def set_profession(self, profession):
        self._profession = profession

    def get_profession(self):
        return self._profession

    def show_data(self):
        print("Profession :" + str(self.get_profession()))

class Scientist(Employee, Graduate):

    def __init__(self, name="", emp_no=0, salary=0, school="", degree="", title="", dues=0, pubs=""):
        self._pubs = pubs
        Employee.__init__(self, name, emp_no, salary)
        Graduate.__init__(self, school, degree)

    def set_pubs(self, pubs):
        self._pubs = pubs

    def get_pubs(self):
        return self._pubs

    def show_data(self):
        print("Pubs :" + str(self.get_pubs()))

class Laborer(Employee):

    def __init__(self, name, emp_no, salary, school, degree, title, dues, pubs):
        self._pubs = pubs
        Employee.__init__(self, name, emp_no, salary)
        Graduate.__init__(self, school, degree)

    def set_pubs(self, pubs):
        self._pubs = pubs

    def get_pubs(self):
        return self._pubs

    def show_data(self):
        print("Pubs :" + str(self.get_pubs()))

class Executive(Manager):
    def __init__(self, profession, bonus, shares):
        self.bonus = bonus
        self.shares = shares

    def set_bonus(self, bonus):
        self.bonus = bonus

    def set_shares(self, shares):
        self.shares = shares

    def get_bonus(self):
        return self.bonus

    def get_shares(self):
        return self.shares

    def show_data(self):
        print("Pubs :" + str(self.get_pubs()))




with open('names.txt', 'r') as f:
    LIST = []
    for line in f:
        for word in line.split():
            LIST.append(word)

print(LIST[0])
b1 = Employee()
b1.set_name(LIST[1])
b1.set_emp_no(LIST[2])
b1.set_salary(LIST[3])
b1.show_data()

g1 = Graduate()
print(LIST[4])
g1.set_school(LIST[5])
g1.set_degree(LIST[6])
g1.show_data()

s1 = Scientist()
print(LIST[7])
s1.set_name(LIST[8])
s1.set_emp_no(LIST[9])
