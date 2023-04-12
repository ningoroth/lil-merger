import pygame as pg
import random
import json

# Initialize pg
pg.init()

# Set the size of the screen
screen_width = 640
screen_height = 480
screen = pg.display.set_mode((screen_width, screen_height))
amount = 5

# Set the color of the squares


# Set the flag to check if the squares are being dragged


#jason = open("./colors.json")
#jason = json.load(jason)

# read file
with open("./colors.json", "r") as read_file:
    distros_dict = json.load(read_file)

for distro in distros_dict:
    print(distro['Square'])
    print(distro['Color'])

# parse file
#obj = json.loads(data)

#print("Square: " + str(obj[square]))
    

class Square:
    def __init__(self, x, y, size, color, i):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.i = i

    def draw(self):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
        # TEMP #
        font = pg.font.SysFont(None, 24)
        img = font.render(f'{self.i}', True, "white")
        screen.blit(img, (self.x, self.y))

    # create 5 squares with random positions and sizes
squares = []
for i in range(amount):
    exec(f'dragging_{i} = False')

    square_color_1 = (255, 0, 0)
    square_color_2 = (0, 255, 0)
    square_color_3 = (255, 255, 0)
    square_color_4 = (0, 255, 255)

    x = 100 * i
    y = 100
    size = 50
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
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
            if squares[0].x < event.pos[0] < squares[0].x + square.size and \
               squares[0].y < event.pos[1] < squares[0].y + square.size:
                
                dragging_0 = True
                # Calculate the offset between the mouse position and the square position
                offset_x_1 = event.pos[0] - squares[0].x
                offset_y_1 = event.pos[1] - squares[0].y

            elif squares[1].x < event.pos[0] < squares[1].x + square.size and \
                 squares[1].y < event.pos[1] < squares[1].y + square.size:
                
                dragging_1 = True
                # Calculate the offset between the mouse position and the square position
                offset_x_2 = event.pos[0] - squares[1].x
                offset_y_2 = event.pos[1] - squares[1].y

            elif squares[2].x < event.pos[0] < squares[2].x + square.size and \
                 squares[2].y < event.pos[1] < squares[2].y + square.size:
                
                dragging_2 = True
                # Calculate the offset between the mouse position and the square position
                offset_x_3 = event.pos[0] - squares[2].x
                offset_y_3 = event.pos[1] - squares[2].y

            elif squares[3].x < event.pos[0] < squares[3].x + square.size and \
                 squares[3].y < event.pos[1] < squares[3].y + square.size:
                
                dragging_3 = True
                # Calculate the offset between the mouse position and the square position
                offset_x_4 = event.pos[0] - squares[3].x
                offset_y_4 = event.pos[1] - squares[3].y
            
            elif squares[4].x < event.pos[0] < squares[4].x + square.size and \
                 squares[4].y < event.pos[1] < squares[4].y + square.size:
                
                dragging_4 = True
                # Calculate the offset between the mouse position and the square position
                offset_x_5 = event.pos[0] - squares[4].x
                offset_y_5 = event.pos[1] - squares[4].y

        elif event.type == pg.MOUSEBUTTONUP:
            dragging_0 = False
            dragging_1 = False
            dragging_2 = False
            dragging_3 = False
            dragging_4 = False
        elif event.type == pg.MOUSEMOTION:
            # Check if a square is being dragged
            if dragging_0:
                # Move the first square to the mouse position with the offset
                squares[0].x = event.pos[0] - offset_x_1
                squares[0].y = event.pos[1] - offset_y_1
            elif dragging_1:
                # Move the second square to the mouse position with the offset
                squares[1].x = event.pos[0] - offset_x_2
                squares[1].y = event.pos[1] - offset_y_2
            elif dragging_2:
                # Move the second square to the mouse position with the offset
                squares[2].x = event.pos[0] - offset_x_3
                squares[2].y = event.pos[1] - offset_y_3
            elif dragging_3:
                # Move the second square to the mouse position with the offset
                squares[3].x = event.pos[0] - offset_x_4
                squares[3].y = event.pos[1] - offset_y_4
            elif dragging_4:
                # Move the second square to the mouse position with the offset
                squares[4].x = event.pos[0] - offset_x_5
                squares[4].y = event.pos[1] - offset_y_5
    
    screen.fill((0, 0, 0))
    
    # draw the squares
    for square in squares:
        square.draw()
    
        # check for collisions
    for i in range(len(squares)):
        for j in range(i + 1, len(squares)):
            if check_collision(squares[i], squares[j]):
                if i == 2 and j == 3:
                    print("Merge!")
                
                #print("Collision between square", i, "and square", j)


    # update the display
    pg.display.update()

# quit pygame
pg.quit()