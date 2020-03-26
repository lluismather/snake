import math

class snake:

    def __init__(self, canvas, width, height, pixel):
        self.CANVAS = canvas
        self.WIDTH = width
        self.HEIGHT = height
        self.pixel_size = pixel
        self.food = None
        self.direction = 'left'
        self.length = 10
        self.start_coord = (math.floor(self.WIDTH / 2), math.floor(self.HEIGHT / 2))
        self.body = [(self.start_coord[0] + (i * 5), self.start_coord[1]) for i in range(self.length)]
        self.git = "Testing"

    def place_snake(self):
        for pixel in self.body:
            c1 = pixel
            c2 = (pixel[0] + self.pixel_size, pixel[1] + self.pixel_size)
            self.CANVAS.create_rectangle(c1, c2, fill='black', outline='white', tag='snake_body')

    def update_snake(self):
        if self.direction == 'left':
            new_val = (self.body[0][0] - 5, self.body[0][1])
        elif self.direction == 'right':
            new_val = (self.body[0][0] + 5, self.body[0][1])
        elif self.direction == 'up':
            new_val = (self.body[0][0], self.body[0][1] - 5)
        elif self.direction == 'down':
            new_val = (self.body[0][0], self.body[0][1] + 5)
        if new_val == self.food:
            self.body = [new_val] + [self.body[i] for i in range(len(self.body))]
            eaten = True
        else:
            self.body = [new_val] + [self.body[i] for i in range(len(self.body) - 1)]
            eaten = False

        for i in range(len(self.body)):
            if self.body[i][0] < 0:
                self.body[i] = (self.WIDTH - self.pixel_size, self.body[i][1])
            elif self.body[i][0] > self.WIDTH:
                self.body[i] = (0, self.body[i][1])
            elif self.body[i][1] < 0:
                self.body[i] = (self.body[i][0], self.HEIGHT - self.pixel_size)
            elif self.body[i][1] > self.HEIGHT:
                self.body[i] = (self.body[i][0], 0)

        self.check_losing(new_val)
        self.place_snake()
        return eaten

    def snake_eat(self):
        self.length += 1

    def check_losing(self, start):
        for pixel in self.body[1:len(self.body)]:
            if pixel == start:
                print('GAME OVER!!!')

