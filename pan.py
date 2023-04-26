import pygame

pygame.init()

# Set up the display
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Panable window with mouse")

# Load the image
image = pygame.image.load("image.png")
image_width, image_height = image.get_size()

# Set up the initial position of the image
x = (screen_width - image_width) // 2
y = (screen_height - image_height) // 2

# Set up the drag flag and mouse position variables
dragging = False
start_pos = None

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Start dragging
            dragging = True
            start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # Stop dragging
            dragging = False
            start_pos = None

    if dragging:
        # Get the current mouse position
        current_pos = pygame.mouse.get_pos()

        # Calculate the distance the mouse has moved
        offset = (current_pos[0] - start_pos[0], current_pos[1] - start_pos[1])

        # Adjust the position of the image accordingly
        x -= offset[0]
        y -= offset[1]

        # Update the start position
        start_pos = current_pos

    # Clip the image so that it doesn't go off the screen
    clipped_rect = pygame.Rect(x, y, screen_width, screen_height).clip(pygame.Rect(0, 0, image_width, image_height))

    # Adjust the clipped rectangle if the image is smaller than the screen
    if image_width < screen_width:
        clipped_rect.x = (screen_width - image_width) // 2
    if image_height < screen_height:
        clipped_rect.y = (screen_height - image_height) // 2

    # Blit the image onto the display surface
    screen.blit(image, (0, 0), clipped_rect)
    pygame.draw.rect(screen, (0,0,0), (100,100,50,50))

    # Update the display
    pygame.display.update()
