import pygame
# starting pygame
pygame.init()
# creating a display surface and set its captions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("blitting images !!!")
# create images.., returns a surface object with the image drawn on it.
# we can then get the rest of the surface and use the rect to position the image.
dragon_left_image = pygame.image.load(" Downloads\dragon_left.png ")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right_image = pygame.image.load(" Downloads\dragon_right.png ")
dragon_right_rect = dragon_left_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)


# main game loop
running = True
while running:
    # loop through a list of event objects that have occured
    for Event in pygame.event.get():  # events will get storedd in a queue

        if Event.type == pygame.QUIT:
            running = False
    # Blit (copy) a surface object at the given coordinates to our display
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)

pygame.quit()  # end the game
