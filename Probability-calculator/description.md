# Probability Calculator

This Python script simulates a probability experiment using a `Hat` class and an `experiment` function. The goal is to calculate the probability of drawing a specific combination of balls from the hat.

## Components

### `Hat` Class
- **Purpose**: Represents a hat containing balls of different colors.
- **Attributes**:
  - `contents`: A list of ball colors, where each color appears as many times as specified.
- **Methods**:
  - `__init__(self, **kwargs)`: Initializes the hat with balls based on the provided keyword arguments.
  - `__str__(self)`: Returns a string representation of the hat's contents.
  - `draw(self, num_balls)`: Draws a specified number of balls from the hat at random. If the number of balls to draw exceeds the available balls, all balls are returned.

### `experiment` Function
- **Purpose**: Conducts multiple experiments to estimate the probability of drawing a specific combination of balls.
- **Parameters**:
  - `hat`: An instance of the `Hat` class.
  - `expected_balls`: A dictionary specifying the desired combination of balls (e.g., `{'red': 2, 'green': 1}`).
  - `num_balls_drawn`: The number of balls to draw in each experiment.
  - `num_experiments`: The number of experiments to perform.
- **Process**:
  - For each experiment, a deep copy of the hat is created to ensure the original hat remains unchanged.
  - Balls are drawn from the hat, and the count of each color is recorded.
  - The experiment is considered a success if the drawn balls match or exceed the expected combination.
- **Returns**: The probability of success, calculated as the number of successful experiments divided by the total number of experiments.