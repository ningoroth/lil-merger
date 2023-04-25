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
    colors_dict = json.load(read_file)

for i in range(amount):
    print(colors_dict[i]["Color"])

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
dragging = []
square_colors = []
offset_x = []
offset_y = []
for i in range(amount):
    dragging.append(False)
    print(dragging)

    square_colors.append(colors_dict[i]["Color"])
    print(square_colors)

    offset_y.append(0)
    print(offset_y)

    offset_x.append(0)
    print(offset_x)

    x = 550
    y = 100 * i
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
            for i in range(amount):
                if squares[i].x < event.pos[0] < squares[i].x + square.size and \
                squares[i].y < event.pos[1] < squares[i].y + square.size:
                    
                    dragging[i] = True
                    # Calculate the offset between the mouse position and the square position
                    offset_x[i] = event.pos[0] - squares[i].x
                    offset_y[i] = event.pos[1] - squares[i].y
                    print(offset_x, offset_y)
                    
                    



        elif event.type == pg.MOUSEBUTTONUP:
            for i in range(amount):
                dragging[i] = False

        elif event.type == pg.MOUSEMOTION:
            # Check if a square is being dragged
            for i in range(amount):
                if dragging[i]:
                    # Move the first square to the mouse position with the offset
                    squares[i].x = event.pos[0] - offset_x[i]
                    squares[i].y = event.pos[1] - offset_y[i]
           
    
    screen.fill((0, 0, 0))

    pg.draw.rect(screen, (255, 255, 255), (500, 0, 200, 800))

    

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