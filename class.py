class Circle:
    def __init__(self,radius,color):
        self.radius = radius
        self.color = color
    def get_radius(self):
        return self.radius
    def get_color(self):
        return self.color
    def get_area(self):
        return self.radius * self.radius * 3.14
if __name__ == "__main__":
    obj = Circle(3,"black")
    print(obj.get_area())
    print(obj.get_color())
    print(obj.get_radius())
