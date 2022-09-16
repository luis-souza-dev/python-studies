class SchoolMember:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        print('(Initialized School Member {}'.format(self.name))
        
    def tell(self):
        print('Name: "{}" Age: "{}"'.format(self.name, self.age), end=' ')
        
class Teacher(SchoolMember):
    def __init__(self, name, age, salary) -> None:
        super().__init__(name, age)
        self.salary = salary
        print('(Initialized Teacher {})'.format(self.name))
    def tell(self):
        super().tell()
        print('Salary: "{:d}"'.format(self.salary))
        
class Student(SchoolMember):
    def __init__(self, name, age, marks) -> None:
        super().__init__(name, age)
        self.marks = marks
        print('(Initialized student {})'.format(name))
        
    def tell(self):
        super().tell()
        print('Marks: "{:d}"'.format(self.marks))
        
t = Teacher('Mr. Ronaldo', 65, 60000)
s = Student('Luis', 23, 100)

print()

members = [t,s]

for member in members:
    member.tell()