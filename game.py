import pygame as pg

# Initialize pg
pg.init()

# Set the size of the screen
screen_width = 640
screen_height = 480
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Lil Merger")

# Set the color of the squares
square_color_1 = (255, 0, 0)
square_color_2 = (0, 255, 0)
square_color_3 = (255, 255, 0)
square_color_4 = (0, 255, 255)


# Set the size and position of the squares
square_size = 50
square_x_1 = 100
square_y_1 = 200
square_x_2 = 200
square_y_2 = 200
square_x_3 = 300
square_y_3 = 200
square_x_4 = 400
square_y_4 = 200

# Set the flag to check if the squares are being dragged
dragging_1 = False
dragging_2 = False
dragging_3 = False
dragging_4 = False

# Create the square surfaces
square_surface_1 = pg.Surface((square_size, square_size))
square_surface_1.fill(square_color_1)
square_surface_2 = pg.Surface((square_size, square_size))
square_surface_2.fill(square_color_2)
square_surface_3 = pg.Surface((square_size, square_size))
square_surface_3.fill(square_color_3)
square_surface_4 = pg.Surface((square_size, square_size))
square_surface_4.fill(square_color_4)

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
            if square_x_1 < event.pos[0] < square_x_1 + square_size and \
               square_y_1 < event.pos[1] < square_y_1 + square_size:
                dragging_1 = True
                # Calculate the offset between the mouse position and the square position
                offset_x_1 = event.pos[0] - square_x_1
                offset_y_1 = event.pos[1] - square_y_1
            # Check if the mouse is over a square
            elif square_x_2 < event.pos[0] < square_x_2 + square_size and \
                 square_y_2 < event.pos[1] < square_y_2 + square_size:
                dragging_2 = True
                # Calculate the offset between the mouse position and the square position
                offset_x_2 = event.pos[0] - square_x_2
                offset_y_2 = event.pos[1] - square_y_2
            # Check if the mouse is over a square
            elif square_x_3 < event.pos[0] < square_x_3 + square_size and \
                 square_y_3 < event.pos[1] < square_y_3 + square_size:
                dragging_3 = True
                # Calculate the offset between the mouse position and the square position
                offset_x_3 = event.pos[0] - square_x_3
                offset_y_3 = event.pos[1] - square_y_3
            # Check if the mouse is over a square
            elif square_x_4 < event.pos[0] < square_x_4 + square_size and \
                 square_y_4 < event.pos[1] < square_y_4 + square_size:
                dragging_4 = True
                # Calculate the offset between the mouse position and the square position
                offset_x_4 = event.pos[0] - square_x_4
                offset_y_4 = event.pos[1] - square_y_4

        elif event.type == pg.MOUSEBUTTONUP:
            dragging_1 = False
            dragging_2 = False
            dragging_3 = False
            dragging_4 = False
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
            if dragging_1:
                # Move the first square to the mouse position with the offset
                square_x_1 = event.pos[0] - offset_x_1
                square_y_1 = event.pos[1] - offset_y_1
            elif dragging_2:
                # Move the second square to the mouse position with the offset
                square_x_2 = event.pos[0] - offset_x_2
                square_y_2 = event.pos[1] - offset_y_2
            elif dragging_3:
                # Move the second square to the mouse position with the offset
                square_x_3 = event.pos[0] - offset_x_3
                square_y_3 = event.pos[1] - offset_y_3
            elif dragging_4:
                # Move the second square to the mouse position with the offset
                square_x_4 = event.pos[0] - offset_x_4
                square_y_4 = event.pos[1] - offset_y_4

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the squares
    screen.blit(square_surface_1, (square_x_1, square_y_1))
    screen.blit(square_surface_2, (square_x_2, square_y_2))
    screen.blit(square_surface_3, (square_x_3, square_y_3))
    screen.blit(square_surface_4, (square_x_4, square_y_4))
    

    # Update the screen
    pg.display.update()
