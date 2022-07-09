class polygon:
    def __init__(self,sides):
        self.sides = sides

    def display_info(self):
        print('A polygon is a 2D shape with straight line')

    def get_peremeter(self):
        peremeter = sum(self.sides)
        return peremeter

class triangle(polygon):
    def display_info(self):
        print('A triangle has 3 sides')
        return super().display_info()
sides = [4,5,6]
t1 = triangle(sides)
t1.display_info()
