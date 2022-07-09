#finding peremeter of a triangle usinf class
print('real :',result.first)
print('imag :',result.second)

#finding peremeter using class

class triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def peremeter(self):
        total = self.a+self.b+self.c
        return total

sides = triangle(3,4,5)
final_value = sides.peremeter()

print('peremeter :',final_value)



#multiplication table

number=int(input('enter your number'))
print('multiplication table of',number)
for count in range(1,11):
    product = count * number
    print(number,'*',count,'=',product)







marks = []
print('Enter the marks of the five subject')
for i in range(0,5):
    ele = int(input())
    marks.append(ele)

def result(marks):
    average = sum(marks)/len(marks)
    print('average is ',average)
    if average >90:
        print('you have scored A')
    elif average > 80:
        print('you have scored B')
    elif average >70:
        print('you have scored C')
    elif average >60:
        print('you have scored D')
    elif average >50:
        print('you have scored E')
    elif average <50:
        print('Fail')
    else:
        print('Invalid input')

result(marks)
