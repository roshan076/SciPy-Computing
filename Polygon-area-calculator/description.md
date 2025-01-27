# Polygon Area Calculator

## Rectangle Class

The `Rectangle` class represents a rectangle shape. It includes the following attributes and methods:

### Attributes:
- **width** (float): The width of the rectangle.
- **height** (float): The height of the rectangle.

### Methods:
- **__init__(self, width, height)**: Constructor to initialize the rectangle's width and height.
- **set_width(self, width)**: Method to set the width of the rectangle. If the rectangle is an instance of the `Square` class, it will also set the height to the same value.
- **set_height(self, height)**: Method to set the height of the rectangle. If the rectangle is an instance of the `Square` class, it will also set the width to the same value.
- **get_area(self)**: Returns the area of the rectangle (width * height).
- **get_perimeter(self)**: Returns the perimeter of the rectangle (2 * (width + height)).
- **get_diagonal(self)**: Returns the diagonal length of the rectangle, calculated using the Pythagorean theorem.
- **get_picture(self)**: Returns a string representation of the rectangle in a grid of '*' characters. If the rectangle is too large (either width or height exceeds 50), it returns "Too big for picture." instead.
- **get_amount_inside(self, shape)**: Returns how many times the provided shape can fit inside the rectangle (without rotation).

### Special Method:
- **__str__(self)**: Returns a string representation of the rectangle, which varies depending on whether it's a `Rectangle` or a `Square` instance.

---

## Square Class

The `Square` class is a subclass of `Rectangle`. It represents a square, which is a special type of rectangle where the width and height are equal. The class includes:

### Attributes:
- **side** (float): The length of one side of the square (same as width and height).

### Methods:
- **__init__(self, side)**: Constructor that initializes the square using the side length (width and height are both set to the side length).
- **set_side(self, side)**: Sets the side length of the square. This automatically sets both the width and height to the same value.
