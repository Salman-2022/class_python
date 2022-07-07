from operator import truediv


class Student:
    def check(something):
        if something.marks >=40:
            return True
        else:
            return False


student1 = Student()
student1.name = 'Harry'
student1.marks = 85

did_pass = student1.check()
print(did_pass)

student2 = Student()
student2.name = 'jannet'
student2.marks = 38

did_pass = student2.check()
print(did_pass)
