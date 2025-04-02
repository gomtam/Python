class SchoolMember:
    """Represents any school member."""
    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = mark
        print(f'{self.name} 초대되었습니다.')
    
    def tell(self):
        """Tell my details."""
        print(f'이름: "{self.name}" 나이: "{self.age}"')

class Teacher(SchoolMember):
    """Represents a teacher."""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(f'{self.name} 선생님이 초대되었습니다.')
        print(f'initialized Teacher: {self.name}')
        
    def tell(self):
        SchoolMember.tell(self)
        print(f'salary: "{self.salary}"')

class Student(SchoolMember):
    """Represents a student."""
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print(f'{self.name} 학생이 초대되었습니다.')
        print(f'initialized Student: {self.name}')
        
    def tell(self):
        SchoolMember.tell(self)
        print(f'marks: "{self.marks}"')

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

members = [t, s]
for member in members:
    member.tell()


    
