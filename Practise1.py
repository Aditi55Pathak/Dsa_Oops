class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        avg = sum(self.marks) / len(self.marks)
        print(avg)


stu = Student("Aditi", [89, 90, 91])
stu.average()
