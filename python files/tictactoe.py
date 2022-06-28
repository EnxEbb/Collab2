from turtle import width
import pygame
import sys

pygame.init()

WIDTH = 600
HEIGHT = 600

RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)


pygame.draw.line(screen, RED, (10, 10), (300, 300), 10)


def draw_lines():
    pass

# mainloop


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
