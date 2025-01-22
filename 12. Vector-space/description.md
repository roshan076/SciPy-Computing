# Vector Space

This Python script defines two classes `R2Vector` and `R3Vector` that represent 2D and 3D vectors, respectively. The `R2Vector` class is the base class, and the `R3Vector` class inherits from it, adding functionality specific to 3D vectors.

---
## R2Vector Class

The `R2Vector` class represents a 2D vector with `x` and `y` components.

### Methods:
- **`__init__(self, *, x, y)`**: Initializes the vector with `x` and `y` values.
- **`norm(self)`**: Returns the Euclidean norm (magnitude) of the vector.
- **`__str__(self)`**: Returns a string representation of the vector as a tuple `(x, y)`.
- **`__repr__(self)`**: Returns a more detailed string representation of the vector in the form `R2Vector(x=..., y=...)`.
- **`__add__(self, other)`**: Adds another `R2Vector` or scalar to the current vector.
- **`__sub__(self, other)`**: Subtracts another `R2Vector` or scalar from the current vector.
- **`__mul__(self, other)`**: Multiplies the vector by a scalar or computes the dot product with another vector.
- **`__eq__(self, other)`**: Compares two vectors for equality.
- **`__ne__(self, other)`**: Compares two vectors for inequality.
- **`__lt__(self, other)`**: Compares the vectors based on their norm (magnitude), checking if the current vector is smaller.
- **`__gt__(self, other)`**: Compares the vectors based on their norm, checking if the current vector is larger.
- **`__le__(self, other)`**: Checks if the vector is smaller than or equal to the other based on the norm.
- **`__ge__(self, other)`**: Checks if the vector is larger than or equal to the other based on the norm.

---
## R3Vector Class

The `R3Vector` class extends the `R2Vector` class to represent a 3D vector with `x`, `y`, and `z` components.

### Methods:
- **`__init__(self, *, x, y, z)`**: Initializes the vector with `x`, `y`, and `z` components by calling the parent constructor for `x` and `y` and adding the `z` component.
- **`cross(self, other)`**: Computes the cross product of two 3D vectors and returns a new `R3Vector` instance with the resulting components.
