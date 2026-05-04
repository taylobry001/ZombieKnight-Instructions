import pygame
pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 736
FPS = 60


# TODO: assign pygame.math.Vector2 to vector

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display_caption = pygame.display.set_caption("Zombie Knight")

pygame_time_clock = pygame.time.Clock()

# TODO: assign pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) to display_surface
# TODO: call pygame.display.set_caption() and pass in "Zombie Knight" as it's only argument

# TODO: assign pygame.time.Clock() to clock