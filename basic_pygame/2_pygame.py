import pygame
pygame.init()
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 500
display_panel = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption("drawing objects")
# define colours as RGB Tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
# Give a background colour to the display
display_panel.fill(WHITE)

# drawing various shapes on our display
# for this we need
# line(surface,color,starting point,ending point,thickness)

            #pygame.draw.line(display_panel, RED, (0, 0), (100, 90), 7)
            #pygame.draw.line(display_panel, BLACK, (100, 90), (250, 250), 7)

# TO DRAW A RECTANGLE
# rectangle(surface,color,(top-left x,top-left y, width, height))
            #pygame.draw.rect(display_panel, CYAN, (500, 0, 100, 100))
            #pygame.draw.rect(display_panel, CYAN, (500, 100, 200, 100))

# to draw a circle
# circle(surface,color,center,radius,thicknes...#you can also put 0 to fill the circle completely in)
pygame.draw.circle(display_panel, BLACK,
                   (WINDOW_HEIGHT//2, WINDOW_WIDTH//2), 90, 7)
pygame.draw.circle(display_panel, BLACK,
                   (WINDOW_HEIGHT//2, WINDOW_WIDTH//2), 50, 7)
pygame.draw.circle(display_panel, BLACK,
                   (WINDOW_HEIGHT//2, WINDOW_WIDTH//2), 70, 7)
pygame.draw.circle(display_panel, BLACK,
                   (WINDOW_HEIGHT//2, WINDOW_WIDTH//2), 30, 7)
pygame.draw.circle(display_panel, RED,
                   (WINDOW_HEIGHT//2, WINDOW_WIDTH//2), 10, 0)


run = True
while run:
    for EVent in pygame.event.get():
        if EVent.type == pygame.QUIT:
            run = False
    # update the display
    pygame.display.update()
pygame.quit()
