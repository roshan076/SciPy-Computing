# Projectile Trajectory Calculator

This Python script simulates the motion of a projectile under the influence of gravity. It calculates the trajectory of the projectile, generates a table of coordinates, and visualizes the trajectory using ASCII art.

## Classes

### `Projectile`
This class represents a projectile and calculates its motion.

#### Attributes:
- `__speed`: Initial speed of the projectile (in m/s).
- `__height`: Initial height of the projectile (in meters).
- `__angle`: Launch angle of the projectile (in radians).

#### Methods:
- `__init__(self, speed, height, angle)`: Initializes the projectile with speed, height, and angle.
- `__str__(self)`: Returns a string representation of the projectile's details, including speed, height, angle, and displacement.
- `__repr__(self)`: Returns a formal string representation of the `Projectile` object.
- `__calculate_displacement(self)`: Calculates the horizontal displacement of the projectile.
- `__calculate_y_coordinate(self, x)`: Calculates the vertical position (`y`) of the projectile at a given horizontal position (`x`).
- `calculate_all_coordinates(self)`: Generates a list of `(x, y)` coordinates representing the projectile's trajectory.
- Properties (`speed`, `height`, `angle`): Getter and setter methods for the projectile's attributes.

### `Graph`
This class handles the visualization of the projectile's trajectory.

#### Attributes:
- `__coordinates`: A list of `(x, y)` coordinates representing the projectile's trajectory.

#### Methods:
- `__init__(self, args)`: Initializes the `Graph` object with the provided coordinates.
- `__repr__(self)`: Returns a formal string representation of the `Graph` object.
- `create_coordinates_table(self)`: Generates a table of `(x, y)` coordinates.
- `create_trajectory(self)`: Creates an ASCII art representation of the projectile's trajectory.

## Helper Function

### `projectile_helper(speed, height, angle)`
This function initializes a `Projectile` object, calculates its trajectory, and visualizes it using the `Graph` class.

#### Parameters:
- `speed`: Initial speed of the projectile (in m/s).
- `height`: Initial height of the projectile (in meters).
- `angle`: Launch angle of the projectile (in degrees).

#### Output:
- Prints the projectile's details.
- Displays a table of `(x, y)` coordinates.
- Visualizes the trajectory using ASCII art.