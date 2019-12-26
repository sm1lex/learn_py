# example for inheritance and polymorphism

class SchoolMember:
    """This superclass responsible for creating all person in the school and counting him"""

    count_school_member = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialize school member: {}'. format(self.name))

    def tell(self):
        """Details for school member"""
        print('Name {}, Age {}'. format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    """Teacher subclass have one advanced variable <salary>"""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Initialized Teacher: {}'. format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Teacher Salary : "{}"'. format(self.salary))
    SchoolMember.count_school_member +=1 
class Student(SchoolMember):
    def __init__(self, name, age, course):
        SchoolMember.__init__(self, name, age)
        self.course = course
        print('Initialize Student: {}'. format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Our Student study at: {}'. format(self.course))
    SchoolMember.count_school_member +=1

t = Teacher('David Bombal', 40, 30000)
s = Student('smilove', 31, 5)
print()

members = [t, s]
for member in members:
    member.tell()
print('In school we have {} people'. format(SchoolMember.count_school_member))

