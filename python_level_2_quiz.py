class Circle:
    def __init__(self):
        self.__r = 0
        self.read()

    def read(self):
        radius = float(input('Radius = '))
        if radius < 0:
            print('Error; radius must be >= 0.')
            self.read()
        else:
            self.__r = radius

    def getArea(self):
        return 3.14 * self.__r * self.__r

    def getPerimiter(self):
        return 3.14 * self.__r * 2

    def printCharateristics(self):
        print('Area = ', self.getArea(), ' cm^2')
        print('Perimiter = ', self.getPerimiter(), ' cm')
/////////////////////////////////////////////////////////////////////////////////////////
class Cylinder(Circle):
    def __init__(self):
        self.__h = 0
        self.read()

    def read(self):
        super().read()
        h = float(input('Heigh = '))
        if h < 0:
            print('Error; height must be >= 0.')
            self.read()
        else:
            self.__h = h

    def getVolume(self):
        return self.getArea() * self.__h

    def printCharateristics(self):
        super().printCharateristics()
        print('Volume = ', self.getVolume(), ' cm^3')
///////////////////////////////////////////////////////////////////////////////////
while True:
    shape = input('Enter the shape from [Circle, Cylinder]')

    if shape == 'Circle':
        c = Circle()
        c.printCharateristics()

    elif shape == 'Cylinder':
        c = Cylinder()
        c.printCharateristics()

