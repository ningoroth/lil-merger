import pygame as pg
import random

# Initialize pg
pg.init()

# Set the size of the screen
screen_width = 640
screen_height = 480
screen = pg.display.set_mode((screen_width, screen_height))

# Set the color of the squares
square_color_1 = (255, 0, 0)
square_color_2 = (0, 255, 0)
square_color_3 = (255, 255, 0)
square_color_4 = (0, 255, 255)

# Set the flag to check if the squares are being dragged
dragging_1 = False
dragging_2 = False
dragging_3 = False
dragging_4 = False

class Square:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    # create 5 squares with random positions and sizes
squares = []
for i in range(7):
    x = 100 * i
    y = 100
    size = 50
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    square = Square(x, y, size, color)
    squares.append(square)

# define collision detection function
def check_collision(square1, square2):
    if (square1.x < square2.x + square2.size and
        square1.x + square1.size > square2.x and
        square1.y < square2.y + square2.size and
        square1.y + square1.size > square2.y):
        return True
    else:
        return False

# Game loop
while True:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        
        '''
        elif event.type == pg.MOUSEBUTTONDOWN:
            # Check if the mouse is over a square
            if square_x["1"] < event.pos[0] < square_x["1"] + square_size and \
               square_y["1"] < event.pos[1] < square_y["1"] + square_size:
                dragging_1 = True
                # Calculate the offset between the mouse position and the square position
                offset_x_1 = event.pos[0] - square_x["1"]
                offset_y_1 = event.pos[1] - square_y["1"]

            elif square_x["2"] < event.pos[0] < square_x["2"] + square_size and \
                 square_y["2"] < event.pos[1] < square_y["2"] + square_size:
                dragging_2 = True
                # Calculate the offset between the mouse position and the square position
                offset_x_2 = event.pos[0] - square_x["2"]
                offset_y_2 = event.pos[1] - square_y["2"]

            elif square_x["3"] < event.pos[0] < square_x["3"] + square_size and \
                 square_y["3"] < event.pos[1] < square_y["3"] + square_size:
                dragging_3 = True
                # Calculate the offset between the mouse position and the square position
                offset_x_3 = event.pos[0] - square_x["3"]
                offset_y_3 = event.pos[1] - square_y["3"]

            elif square_x["4"] < event.pos[0] < square_x["4"] + square_size and \
                 square_y["4"] < event.pos[1] < square_y["4"] + square_size:
                dragging_4 = True
                # Calculate the offset between the mouse position and the square position
                offset_x_4 = event.pos[0] - square_x["4"]
                offset_y_4 = event.pos[1] - square_y["4"]

        elif event.type == pg.MOUSEBUTTONUP:
            dragging_1 = False
            dragging_2 = False
            dragging_3 = False
            dragging_4 = False
        elif event.type == pg.MOUSEMOTION:
            # Check if a square is being dragged
            if dragging_1:
                # Move the first square to the mouse position with the offset
                square_x["1"] = event.pos[0] - offset_x_1
                square_y["1"] = event.pos[1] - offset_y_1
            elif dragging_2:
                # Move the second square to the mouse position with the offset
                square_x["2"] = event.pos[0] - offset_x_2
                square_y["2"] = event.pos[1] - offset_y_2
            elif dragging_3:
                # Move the second square to the mouse position with the offset
                square_x["3"] = event.pos[0] - offset_x_3
                square_y["3"] = event.pos[1] - offset_y_3
            elif dragging_4:
                # Move the second square to the mouse position with the offset
                square_x["4"] = event.pos[0] - offset_x_4
                square_y["4"] = event.pos[1] - offset_y_4
                '''
    
    # draw the squares
    for square in squares:
        square.draw()
    
        # check for collisions
    for i in range(len(squares)):
        for j in range(i + 1, len(squares)):
            if check_collision(squares[i], squares[j]):
                print("Collision between square", i, "and square", j)


    # update the display
    pg.display.flip()

# quit pygame
pg.quit()