import pygame
from pygame.locals import *
import os

pygame.init()

# Important Global Variables
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("UNO!")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BORDER = pygame.Rect(WIDTH//2-5, 0, 10, HEIGHT)
FPS = 60
FONT = pygame.font.SysFont('Constantia', 30)
clicked = False

# Create a button class that handles all of the buttons created in the game

class button():

    # button colors
    button_color = (255, 0, 0)
    hover_color = (75, 225, 255)
    click_color = (50, 150, 255)
    text_color = BLACK
    width = 180
    height = 70

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):
        global clicked
        action = False

        # Get the position of the mouse
        pos = pygame.mouse.get_pos()

        # Build the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # Check if the button is clicked
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                clicked = True
                pygame.draw.rect(WIN, self.click_color,button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(WIN, self.hover_color, button_rect)
        else:
            pygame.draw.rect(WIN, self.button_color, button_rect)

            # add shading to button
            pygame.draw.line(WIN, WHITE, (self.x, self.y), (self.x + self.width, self.y), 2)
            pygame.draw.line(WIN, WHITE, (self.x, self.y), (self.x, self.y + self.height), 2)
            pygame.draw.line(WIN, BLACK, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height),
                             2)
            pygame.draw.line(WIN, BLACK, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height),
                             2)

            # add text to button
            text_img = FONT.render(self.text, True, self.text_color)
            text_len = text_img.get_width()
            WIN.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
            return action


# Create buttons for game intro

START_BUTTON = button(200, 300, 'START')
INFO = button(500, 300, 'HELP')
TWO_PLAYERS = button(200, 250, "2 Players")
THREE_PLAYERS = button(400, 250, "3 Players")
FOUR_PLAYERS = button(600, 250, "4 Players")
player_num = 0



def game_intro():
    WIN.fill(WHITE)
    text = FONT.render("UNO!",True, RED)
    WIN.blit(text, (200,200))

    if START_BUTTON.draw_button():
        print("The game has started")
        WIN.fill(WHITE)
        if TWO_PLAYERS.draw_button():
            player_num = 2
        if THREE_PLAYERS.draw_button():
            player_num = 3
        if FOUR_PLAYERS.draw_button():
            player_num

    if INFO.draw_button():
        text = FONT.render('The object of UNO is to be the first one to have all of your cards discarded. The card you place down must match the card on top of the deck in color or number. You may also play a specialty card.', True, BLACK)
        WIN.blit(text, (100,100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        game_intro()
        #pygame.display.update()


    pygame.quit()


if __name__ == "__main__":
    main()