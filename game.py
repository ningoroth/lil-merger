import pygame as pg
from elements import *

# Initialize pg
pg.init()

# Set the size of the screen
screen_width = 640
screen_height = 480
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Lil Merger")

x = 50
y = 50
size = 50

gameAir = Air(x,y,size)
gameFire = Fire(x,y,size)
gameEarth = Earth(x,y,size)
gameWater = Water(x,y,size)

# Game loop
while True:

    #mouse_position = pg.mouse.get_pos()
    #print(mouse_position)
    
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        elif event.type == pg.MOUSEBUTTONDOWN:

            
            # Check if the mouse is over a square
            if gameAir.x < event.pos[0] < gameAir.x + gameAir.size and \
               gameAir.y < event.pos[1] < gameAir.y + gameAir.size:
                gameAir.dragging = True
                # Calculate the offset between the mouse position and the square position
                gameAir.offset_x = event.pos[0] - gameAir.x
                gameAir.offset_y = event.pos[1] - gameAir.y

            elif gameFire.x < event.pos[0] < gameFire.x + gameFire.size and \
               gameFire.y < event.pos[1] < gameFire.y + gameFire.size:
                gameFire.dragging = True
                # Calculate the offset between the mouse position and the square position
                gameFire.offset_x = event.pos[0] - gameFire.x
                gameFire.offset_y = event.pos[1] - gameFire.y
            
            elif gameEarth.x < event.pos[0] < gameEarth.x + gameEarth.size and \
               gameEarth.y < event.pos[1] < gameEarth.y + gameEarth.size:
                gameEarth.dragging = True
                # Calculate the offset between the mouse position and the square position
                gameEarth.offset_x = event.pos[0] - gameEarth.x
                gameEarth.offset_y = event.pos[1] - gameEarth.y
            
            elif gameWater.x < event.pos[0] < gameWater.x + gameWater.size and \
               gameWater.y < event.pos[1] < gameWater.y + gameWater.size:
                gameWater.dragging = True
                # Calculate the offset between the mouse position and the square position
                gameWater.offset_x = event.pos[0] - gameWater.x
                gameWater.offset_y = event.pos[1] - gameWater.y

        elif event.type == pg.MOUSEBUTTONUP:
            gameAir.dragging = False
            gameFire.dragging = False
            gameEarth.dragging = False
            gameWater.dragging = False
        elif event.type == pg.MOUSEMOTION:

            #if event.pos[0] < 10:
            #    pg.mouse.set_pos((0,mouse_position[1]))
            #elif event.pos[0] > 630:
            #   pg.mouse.set_pos((630,mouse_position[1]))
            #if event.pos[1] < 10:
            #    pg.mouse.set_pos((mouse_position[0], 0))
            #elif event.pos[1] > 470:
            #   pg.mouse.set_pos((mouse_position[0], 470))

            # Check if a square is being dragged
            if gameAir.dragging:
                # Move the first square to the mouse position with the offset
                gameAir.x = event.pos[0] - gameAir.offset_x
                gameAir.y = event.pos[1] - gameAir.offset_y
            
            if gameFire.dragging:
                # Move the first square to the mouse position with the offset
                gameFire.x = event.pos[0] - gameFire.offset_x
                gameFire.y = event.pos[1] - gameFire.offset_y
            
            if gameEarth.dragging:
                # Move the first square to the mouse position with the offset
                gameEarth.x = event.pos[0] - gameEarth.offset_x
                gameEarth.y = event.pos[1] - gameEarth.offset_y
            
            if gameWater.dragging:
                # Move the first square to the mouse position with the offset
                gameWater.x = event.pos[0] - gameWater.offset_x
                gameWater.y = event.pos[1] - gameWater.offset_y


    # Clear the screen
    screen.fill((36, 41, 46))

    gameAir.draw(screen)
    gameFire.draw(screen)
    gameEarth.draw(screen)
    gameWater.draw(screen)

    # Draw the squares

    

    # Update the screen
    pg.display.update()
