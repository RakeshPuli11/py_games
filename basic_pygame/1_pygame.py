import pygame
# starting pygame
pygame.init()
# creating a display surface and set its captions
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("GAME window !!!")
# main game loop
running = True
while running:
    # loop through a list of event objects that have occured
    for Event in pygame.event.get():  # events will get storedd in a queue
        print(Event)
        if Event.type == pygame.QUIT:
            running = False
pygame.quit()  # end the game
