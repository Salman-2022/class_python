print('to find the peremeter of a quadliratral')
length = int(input('Enter the number of sides :\n'))
sides = []
for side in range(0,length):
    element = int(input('enter element'))
    sides.append(element)

class polynomial:
    def __init__(self,sides):
        self.sides = sides

    def get_peremeter(self):
        result = sum(self.sides)
        return result 
poly = polynomial(sides)

t1 = poly.get_peremeter()
print('peremeter is :',t1)

if len(sides) == 3:
    print('Its a triangle')
elif len(sides) == 4:
    print('its a quadrilateral')
elif len(sides) == 5:
    print('its a pentagon')
elif len(sides) == 6:
    print('its a hexagon')
else:
    print('I have no idea')
