import tkinter as tk
import time
import random
import snake

class gui:

    def __init__(self, width, height, framerate):
        self.WIDTH = width
        self.HEIGHT = height
        self.FRAMERATE = framerate
        self.root = tk.Tk()
        self.CANVAS = tk.Canvas(self.root, width=self.WIDTH, height=self.HEIGHT)
        self.CANVAS.pack()
        self.CANVAS.bind_all('<Left>', self.left_key)
        self.CANVAS.bind_all('<Right>', self.right_key)
        self.CANVAS.bind_all('<Up>', self.up_key)
        self.CANVAS.bind_all('<Down>', self.down_key)
        self.pixel_size = 5
        self.snake = snake.snake(self.CANVAS, self.WIDTH, self.HEIGHT, self.pixel_size)
        self.snake.place_snake()
        self.food_postition = None
        self.place_food()

    def console(self, lines):
        print('>>> {}...'.format(lines))

    def left_key(self, event):
        if self.snake.direction != 'right':
            self.snake.direction = 'left'

    def right_key(self, event):
        if self.snake.direction != 'left':
            self.snake.direction = 'right'

    def up_key(self, event):
        if self.snake.direction != 'down':
            self.snake.direction = 'up'

    def down_key(self, event):
        if self.snake.direction != 'up':
            self.snake.direction = 'down'

    def place_food(self):
        self.CANVAS.delete(self.CANVAS.find_withtag('food'))
        x = random.randint(0, ((self.WIDTH - self.pixel_size) / self.pixel_size)) * self.pixel_size
        y = random.randint(0, ((self.HEIGHT - self.pixel_size) / self.pixel_size)) * self.pixel_size
        self.food_position = (x, y)
        self.snake.food = self.food_position
        self.CANVAS.create_rectangle((x, y), (x + self.pixel_size, y + self.pixel_size), tag='food', outline='white', fill='black')

    def update_frames(self, tags):
        if tags:
            for tag in tags:
                for obj in self.CANVAS.find_withtag(tag):
                    self.CANVAS.delete(obj)
        if self.snake.update_snake() == True:
            self.place_food()

    def initialise(self):
        self.console('initialised')
        while True:
            time.sleep(self.FRAMERATE)
            self.CANVAS.update()
            self.update_frames(['snake_body'])


