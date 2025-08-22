import pygame

print("Initializing game...")

pygame.init()

screen = pygame.display.set_mode((1024, 768), vsync=True)
display_info =  pygame.display.Info()

clock = pygame.time.Clock()

running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("orange")

    # RENDER YOUR GAME HERE
    pygame.display.set_caption(f'NearMiss2d {pygame.display.get_driver()} @ {round(clock.get_fps())} fps ({display_info.current_w}, {display_info.current_h})')

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()