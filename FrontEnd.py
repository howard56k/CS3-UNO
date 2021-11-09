import sys
import pygame
from pygame.locals import *
import UNO
import os

pygame.init()

# Important Global Variables
WIDTH, HEIGHT = 1100, 700
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_RED = (139, 0, 0)
LIGHT_RED = (220, 20, 60)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_GREEN = (60, 179, 113)
DARK_GREEN = (0, 128, 0)
GREEN = (46, 139, 87)
YELLOW = (255, 255, 0)
GREY = (192, 192, 192)
BORDER = pygame.Rect(WIDTH//2-5, 0, 10, HEIGHT)
FPS = 60
SMALL_FONT = pygame.font.SysFont('Constantia', 15)
FONT = pygame.font.SysFont('Constantia', 30)
BIG_FONT = pygame.font.SysFont('Constantia', 50)
clicked = False
winner = False
# Set icon and caption

icon = pygame.image.load('uno_assets_2d/PNGs/small/uno_logo.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("UNO!")

# Create a button class that handles all of the buttons created in the game

class button():

    # button class variables
    text_color = BLACK
    width = 180
    height = 70

    def __init__(self, x, y, text, button_color = RED, hover_color = YELLOW, click_color = BLUE):
        self.x = x
        self.y = y
        self.text = text
        self.button_color = button_color
        self.hover_color = hover_color
        self.click_color = click_color

    def draw_button(self):
        global clicked
        action = False

        # Get the position of the mouse
        pos = pygame.mouse.get_pos()

        # Build the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # Check if the button is clicked
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(WIN, self.click_color, button_rect)
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
START_BUTTON = button(450, 500, 'START', GREEN, LIGHT_GREEN, DARK_GREEN)
#INFO = button(600, 500, 'HELP', RED, LIGHT_RED, DARK_RED)
player_num = 0


def game_intro():
    intro = True
    while intro:
        WIN.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        image = pygame.image.load('uno_assets_2d/PNGs/large/uno_cards.png')
        WIN.blit(image, (350, 100))



       # if INFO.draw_button():
        #    text = SMALL_FONT.render('The object of UNO is to be the first one to have all of your cards discarded.',
           #                          True, BLACK)
         #   WIN.blit(text, (10, 600))
        if START_BUTTON.draw_button():
            print("The game has started")
            WIN.fill(WHITE)
            intro = False

        pygame.display.update()

TWO_PLAYERS = button(250, 400, "2 Players", RED,LIGHT_RED, DARK_RED)
THREE_PLAYERS = button(450, 400, "3 Players", RED, LIGHT_RED, DARK_RED)
FOUR_PLAYERS = button(650, 400, "4 Players", RED, LIGHT_RED, DARK_RED)

def game_menu():
    intro = True
    while intro:
        WIN.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        text = BIG_FONT.render('How many players?', True, BLACK)
        WIN.blit(text, (350, 200))
        if TWO_PLAYERS.draw_button():
            player_num = 2
            WIN.fill(WHITE)
            intro = False
        if THREE_PLAYERS.draw_button():
            player_num = 3
            WIN.fill(WHITE)
            intro = False
        if FOUR_PLAYERS.draw_button():
            player_num = 4
            WIN.fill(WHITE)
            intro = False
        pygame.display.update()

GO_BUTTON = button(450, 500, 'GO!', GREEN, LIGHT_GREEN, DARK_GREEN)
def ready_menu():
    intro = True
    while intro:
        WIN.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        sentence = "Player %d it is your turn!" %player_num
        text = BIG_FONT.render(sentence, True, BLACK)
        WIN.blit(text, (350, 200))
        sentence = "Click the GO button when you are ready."
        text = BIG_FONT.render(sentence, True, BLACK)
        WIN.blit(text, (150, 260))
        if GO_BUTTON.draw_button():
            print("Player %d 's turn has started" %player_num)
            WIN.fill(WHITE)
            intro = False

        pygame.display.update()






def display_cards(top_card, player ):
    loop = True
    while loop:
        WIN.fill(GREY)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        # display the deck
        image = pygame.image.load('uno_assets_2d/PNGs/small/card_back.png')
        image2 = pygame.image.load('uno_assets_2d/PNGs/small/card_back.png')
        image3 = pygame.image.load('uno_assets_2d/PNGs/small/card_back.png')
        image4 = pygame.image.load('uno_assets_2d/PNGs/small/card_back.png')
        image5 = pygame.image.load('uno_assets_2d/PNGs/small/card_back.png')
        WIN.blit(image, (550, 100))
        WIN.blit(image2, (547, 103))
        WIN.blit(image3, (544, 106))
        WIN.blit(image4, (541, 109))
        WIN.blit(image5, (538, 112))
        # display the top card
        card = pygame.image.load(top_card.card_file_asset)
        WIN.blit(card, (500, 100))
        # display the players deck




        pygame.display.update()




game_intro()
game_menu()
ready_menu()
display_cards()
