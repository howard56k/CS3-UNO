# Code to see the font options

import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 1600, 1000
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
size = len(pygame.font.get_fonts())
fonts = pygame.font.get_fonts()
go = True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def test():
    x = 10
    y = 10
    global go
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        if go:
            WIN.fill(WHITE)
            for i in range(size):
                A = fonts[i]
                print(A)
                SMALL_FONT = pygame.font.SysFont(A, 13)
                text = SMALL_FONT.render(A, True, BLACK)
                WIN.blit(text, (x, y))
                x += 150
                if i % 10 == 0 and i != 1:
                    y += 50
                    x = 10
            go = False

        pygame.display.update()
test()
