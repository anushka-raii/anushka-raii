# Person → Student Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def show_grade(self):
        print(f"Grade: {self.grade}")

student1 = Student("Ananya", 16, "10th")
student1.display_info()
student1.show_grade()
