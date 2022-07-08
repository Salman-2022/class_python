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

#second code


class Student:
    def check(something):
        if something.marks >=40:
            return True
        else:
            return False

    def __init__(something,name,marks):
        something.name = name
        something.marks = marks


student1 = Student('Harry', 85)
did_pass = student1.check()
print(did_pass)

student2 = Student('jannet',38)
did_pass = Student.check()
print(did_pass)



#Third code for class to add numbers

class something:
    def __init__(self,first,second):
        self.first = first
        self.second = second

    def add(self,number):
        real = self.first + number.first
        imag = self.second + number.second
        result = something(real,imag)
        return result

n1 = something(4,7)

n2 = something(-5,9)

result = n1.add(n2)
print('real :',result.first)
print('imag :',result.second)

