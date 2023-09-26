class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self._age = age
        self.gender = gender

    def say_hello(self):
        print(
            f"Hi, I'm {self.name}. I'm a {self._age} year old {self.gender}")

    def is_adult(self):
        return self._age >= 18

    # age is private. here's a method to see its value
    def get_age(self):
        return self._age


# create a person and test the say_hello() and is_adult() methods
person = Person('George', 28, 'Male')
person.say_hello()
print('age: ', person.get_age())
print('is adult:', person.is_adult())


# Student inherits from person but as some additional fields
class Student(Person):
    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.course = course

    # describe their enrollment details
    def say_enrollment(self):
        print(
            f'My Student ID is {self.student_id} and I am enrolled in {self.course}')


student = Student('George', 28, 'Male', 'C012345', 'FSDM')
student.say_enrollment()


# Teacher also inehrits from person with some additional fields
class Teacher(Person):
    def __init__(self, name, age, gender, teacher_id, subject):
        super().__init__(name, age, gender)
        self.teacher_id = teacher_id
        self.subject = subject

    # introduce themself as a teacher
    def say_hello(self):
        print(f"I'm {self.name}. I teach {self.subject}")


teacher = Teacher('Kate', 47, 'Female', 'T01123', 'Python')
teacher.say_hello()
