import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"

class Projectile:
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)

    def __str__(self):
        details = '\nProjectile details:\n'
        details += f'speed: {self.speed} m/s\n'
        details += f'height: {self.height} m\n'
        details += f'angle: {self.angle}°\n'
        details += f'displacement: {round(self.__calculate_displacement(), 1)} m\n'
        return details
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.speed}, {self.height}, {self.angle})'

    def __calculate_displacement(self):
        temp1 = self.__speed * math.cos(self.__angle)
        temp2 = self.__speed * math.sin(self.__angle)
        temp3 = math.sqrt(self.__speed**2 * math.sin(self.__angle)**2 + 2 * GRAVITATIONAL_ACCELERATION * self.__height)
        return (temp1 * (temp2 + temp3)) / GRAVITATIONAL_ACCELERATION
    
    def __calculate_y_coordinate(self, x):
        return self.__height + x * math.tan(self.__angle) - (GRAVITATIONAL_ACCELERATION * x**2) / (2 * self.__speed**2 * math.cos(self.__angle)**2)
    
    def calculate_all_coordinates(self):
        coordinates = []
        for x in range(0, math.ceil(self.__calculate_displacement())):
            coordinates.append((x, self.__calculate_y_coordinate(x)))
        return coordinates
    
    @property
    def speed(self):
        return self.__speed
    @property
    def height(self):
        return self.__height
    @property
    def angle(self):
        return round(math.degrees(self.__angle))
    
    @speed.setter
    def speed(self, speed):
        self.__speed = speed
    @height.setter
    def height(self, height):
        self.__height = height
    @angle.setter
    def angle(self, angle):
        self.__angle = math.radians(angle)
    
class Graph:
    __slots__ = ('__coordinates')

    def __init__(self, args):
        self.__coordinates = args

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__coordinates})'
    
    def create_coordinates_table(self):
        x_label = 'x'
        y_label = 'y'
        table = f'{x_label:>3}{y_label:>7}\n'
        for (x, y) in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'
        return table
    
    def create_trajectory(self):
        rounded_coords = [(round(x), round(y)) for (x, y) in self.__coordinates]
        
        x_max = max([x for (x, _) in rounded_coords])
        y_max = max([y for (_, y) in rounded_coords])

        matrix_list = [[' ' for _ in range(x_max + 1)] for _ in range (y_max + 1)]

        for (x, y) in rounded_coords:
            matrix_list[y_max - y][x] = PROJECTILE

        matrix_list = ["".join(row) for row in matrix_list]

        matrix_list = [y_axis_tick + row for row in matrix_list]
        matrix_list.append(' ' + x_axis_tick*len(matrix_list[0]))

        matrix_list = '\n' + '\n'.join(matrix_list) + '\n'

        return matrix_list

def projectile_helper(speed, height, angle):
    ball = Projectile(speed, height, angle)
    print(ball)
    coordinates = ball.calculate_all_coordinates()
    graph = Graph(coordinates)
    print(graph.create_coordinates_table())
    print(graph.create_trajectory())

projectile_helper(10, 3, 45)