import pygame as pg
import random
import json

# Initialize pg
pg.init()

# Set the size of the screen
screen_width = 640
screen_height = 480
screen = pg.display.set_mode((screen_width, screen_height))
amount = 6

# read file
with open("./colors.json", "r") as read_file:
    colors_dict = json.load(read_file)

#for i in range(amount):
#    print(colors_dict[i]["Color"])
    

class Square:
    def __init__(self, x, y, size, color, i):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.i = i
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        

    def draw(self):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
        # TEMP #
        font = pg.font.SysFont(None, 24)
        img = font.render(f'{self.i}', True, "white")
        screen.blit(img, (self.x, self.y))


squares = []

for i in range(amount):
    #dragging.append(False)
    #print(dragging)

    #square_colors.append(colors_dict[i]["Color"])
    #print(square_colors)

    x = 100 * i
    y = 100
    size = 50
    #colors_dict[i]["Color"]= tuple(colors_dict[i]["Color"])
    color = colors_dict[i]["Color"]
    color = tuple(color)
    print(color)
    square = Square(x, y, size, color, i)
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
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            # Check if the mouse is over a square
            for i in range(amount):
                if squares[i].x < event.pos[0] < squares[i].x + square.size and \
                squares[i].y < event.pos[1] < squares[i].y + square.size:
                    
                    squares[i].dragging = True
                    # Calculate the offset between the mouse position and the square position
                    squares[i].offset_x = event.pos[0] - squares[i].x
                    squares[i].offset_y = event.pos[1] - squares[i].y

                    break

        elif event.type == pg.MOUSEBUTTONUP:
            for i in range(amount):
                squares[i].dragging = False

        elif event.type == pg.MOUSEMOTION:
            # Check if a square is being dragged
            for i in range(amount):
                if squares[i].dragging:
                    # Move the first square to the mouse position with the offset
                    squares[i].x = event.pos[0] - squares[i].offset_x
                    squares[i].y = event.pos[1] - squares[i].offset_y
    
    screen.fill((36, 41, 46))
    
    # draw the squares
    for square in squares:
        square.draw()
    
        # check for collisions
    for i in range(len(squares)):
        for j in range(i + 1, len(squares)):
            if check_collision(squares[i], squares[j]):
                if i == 2 and j == 3:
                    print(f"Merge with square {i} and square {j}")


    # update the display
    pg.display.update()

# quit pygame
pg.quit()