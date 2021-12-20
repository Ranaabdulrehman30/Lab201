
class Employee:
    def __init__(self, name, scale):
        self._name = name
        self._scale = scale

    def get_name(self):
        return self._name

    def get_scale(self):
        return self._scale


class faculty(Employee):
    def __init__(self, name, scale, degree, area):
        self.__Degree = degree
        self.Area = area
        Employee.__init__(self, name, scale)

    def get_degree(self):
        return self.__Degree

    def get_area(self):
        return self.Area


class staff(Employee):
    def __init__(self, experience, skills):
        self.experience = experience
        self.skills = skills

    def get_exp(self):
        return self.experience

    def get_skills(self):
        return self.skills


class Teacher(faculty):
    def __init__(self, name, scale, degree, area, subject, students):
        self.subject = subject
        self.students = students
        faculty.__init__(self, name, scale, degree, area)

    def show(self):
        print("Name : ", Employee.get_name(self))
        print("Scale : ", Employee.get_scale(self))
        print("Degree : ", faculty.get_degree(self))
        print("Area : ", faculty.get_area(self))
        print("Subject : ", self.subject)
        print("Students : ", self.students)


t1 = Teacher("Asif", "Higher", "PHD CS", "CS", "CS", 10)
t2 = Teacher("Asifdf", "Higher", "PHD CS", "CS", "CS", 11)
t3 = Teacher("Asifzzzz", "Higher", "PHD CS", "CS", "CS", 12)
t1.show()
t2.show()
t3.show()



print("\n\nFor HEAD OF DEPARTMENT\n\n")


class HOD(faculty, staff):

    def __init__(self, name, scale, degree, area, experience, skills, dept, subordinates):
        self.dept = dept
        self.subordinates = subordinates
        faculty.__init__(self, name, scale, degree, area)
        staff.__init__(self, experience, skills)

    def show(self):
        print("Name : ", Employee.get_name(self))
        print("Scale : ", Employee.get_scale(self))
        print("Degree : ", faculty.get_degree(self))
        print("Area : ", faculty.get_area(self))
        print("Experience : ", staff.get_exp(self))
        print("Skills : ", staff.get_skills(self))
        print("Department : ", self.dept)
        print("Subordinate : ", self.subordinates)


H1 = HOD("Zain", "Higher", "PHD CS", "CS", 5, "Pyhton", "FCSC", 9)
H1.show()