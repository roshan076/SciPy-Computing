import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    def __str__(self):
        return str(self.contents)
    
    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []
            return drawn_balls
        
        for _ in range(num_balls):
            ball = random.choice(self.contents)
            drawn_balls.append(ball)
            self.contents.remove(ball)
        
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls = list(expected_balls.items())
    num_successes = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_dict = {}
        for ball in drawn_balls:
            if ball in drawn_balls_dict:
                drawn_balls_dict[ball] += 1
            else:
                drawn_balls_dict[ball] = 1
        success = True
        for ball, count in expected_balls:
            if ball not in drawn_balls_dict or drawn_balls_dict[ball] < count:
                success = False
                break
        if success:
            num_successes += 1
    return num_successes / num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)
# Return random probability (0.376)