import pygame

clock = pygame.time.Clock()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

FRICTION_COEFFICIENT = 0.75

class Debug:
    @classmethod
    def font(cls):
        return pygame.font.SysFont("freemono", 16)
