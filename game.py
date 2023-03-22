import pygame

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the color of the squares
square_color_1 = (255, 0, 0)
square_color_2 = (0, 255, 0)
square_color_3 = (255, 255, 0)
square_color_4 = (0, 255, 255)


# Set the size and position of the squares
square_size = 50
square_x_1 = 100
square_y_1 = 100
square_x_2 = 300
square_y_2 = 200
square_x_3 = 200
square_y_3 = 300
square_x_4 = 400
square_y_4 = 200

# Set the flag to check if the squares are being dragged
dragging_1 = False
dragging_2 = False
dragging_3 = False
dragging_4 = False

# Create the square surfaces
square_surface_1 = pygame.Surface((square_size, square_size))
square_surface_1.fill(square_color_1)
square_surface_2 = pygame.Surface((square_size, square_size))
square_surface_2.fill(square_color_2)
square_surface_3 = pygame.Surface((square_size, square_size))
square_surface_3.fill(square_color_3)
square_surface_4 = pygame.Surface((square_size, square_size))
square_surface_4.fill(square_color_4)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse is over a square
            if square_x_1 < event.pos[0] < square_x_1 + square_size and \
               square_y_1 < event.pos[1] < square_y_1 + square_size:
                dragging_1 = True
                # Calculate the offset between the mouse position and the square position
                offset_x_1 = event.pos[0] - square_x_1
                offset_y_1 = event.pos[1] - square_y_1

            elif square_x_2 < event.pos[0] < square_x_2 + square_size and \
                 square_y_2 < event.pos[1] < square_y_2 + square_size:
                dragging_2 = True
                # Calculate the offset between the mouse position and the square position
                offset_x_2 = event.pos[0] - square_x_2
                offset_y_2 = event.pos[1] - square_y_2

            elif square_x_3 < event.pos[0] < square_x_3 + square_size and \
                 square_y_3 < event.pos[1] < square_y_3 + square_size:
                dragging_3 = True
                # Calculate the offset between the mouse position and the square position
                offset_x_3 = event.pos[0] - square_x_3
                offset_y_3 = event.pos[1] - square_y_3

            elif square_x_4 < event.pos[0] < square_x_4 + square_size and \
                 square_y_4 < event.pos[1] < square_y_4 + square_size:
                dragging_4 = True
                # Calculate the offset between the mouse position and the square position
                offset_x_4 = event.pos[0] - square_x_4
                offset_y_4 = event.pos[1] - square_y_4

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging_1 = False
            dragging_2 = False
            dragging_3 = False
            dragging_4 = False
        elif event.type == pygame.MOUSEMOTION:
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
    pygame.display.update()
