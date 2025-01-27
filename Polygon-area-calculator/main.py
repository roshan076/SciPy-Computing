class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
        if isinstance(self, Square):
            self.height = width

    def set_height(self, height):
        self.height = height
        if isinstance(self, Square):
            self.width = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if (self.width > 50 or self.height > 50):
            return 'Too big for picture.'

        picture = ""
        for i in range(self.height):
            picture += '*' * self.width + '\n'

        return picture

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        if self.__class__.__name__ == 'Square':
            return f'{self.__class__.__name__}(side={self.width})'
        
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'
        

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

rect = Rectangle(10, 5)
print(rect)
print('Area:', rect.get_area())
print('Perimeter:', rect.get_perimeter())
print(rect.get_picture())

sq = Square(4)
print(sq)
print('Area:', sq.get_area())
print('Diagonal:', sq.get_diagonal())
print(sq.get_picture())