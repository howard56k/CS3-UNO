import sys
import pygame
import config
from pygame.locals import *

pygame.init()
print(pygame.font.get_fonts())
# Important Global Variables
WIDTH, HEIGHT = 1500, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
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
LIGHT_GREY = (105, 105, 105)
GREY = (169, 169, 169)
DARK_GREY = (192, 192, 192)
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)
FPS = 60
SMALL_FONT = pygame.font.SysFont('franklingothicheavy', 15)
FONT = pygame.font.SysFont('franklingothicheavy', 30)
BIG_FONT = pygame.font.SysFont('franklingothicheavy', 50)
clicked = False
winner = False
player_num = 1
# How many players there are

# Set icon and caption

icon = pygame.image.load('uno_assets_2d/PNGs/small/uno_logo.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("UNO!")


# Create a button class that handles all of the buttons created in the game

class button:
    # button class variables
    text_color = BLACK
    width = 180
    height = 70

    def __init__(self, x, y, text, button_color=RED, hover_color=YELLOW, click_color=BLUE):
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
                # add shading to button
                pygame.draw.line(WIN, WHITE, (self.x, self.y), (self.x + self.width, self.y), 2)
                pygame.draw.line(WIN, WHITE, (self.x, self.y), (self.x, self.y + self.height), 2)
                pygame.draw.line(WIN, BLACK, (self.x, self.y + self.height),
                                 (self.x + self.width, self.y + self.height), 2)
                pygame.draw.line(WIN, BLACK, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height),
                                 2)

                # add text to button
                text_img = FONT.render(self.text, True, self.text_color)
                text_len = text_img.get_width()
                WIN.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 20))

            elif pygame.mouse.get_pressed()[0] == 0 and clicked:
                clicked = False
                action = True
                # add shading to button
                pygame.draw.line(WIN, WHITE, (self.x, self.y), (self.x + self.width, self.y), 2)
                pygame.draw.line(WIN, WHITE, (self.x, self.y), (self.x, self.y + self.height), 2)
                pygame.draw.line(WIN, BLACK, (self.x, self.y + self.height),
                                 (self.x + self.width, self.y + self.height), 2)
                pygame.draw.line(WIN, BLACK, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height),
                                 2)

                # add text to button
                text_img = FONT.render(self.text, True, self.text_color)
                text_len = text_img.get_width()
                WIN.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 20))
            else:
                pygame.draw.rect(WIN, self.hover_color, button_rect)
                # add shading to button
                pygame.draw.line(WIN, WHITE, (self.x, self.y), (self.x + self.width, self.y), 2)
                pygame.draw.line(WIN, WHITE, (self.x, self.y), (self.x, self.y + self.height), 2)
                pygame.draw.line(WIN, BLACK, (self.x, self.y + self.height),
                                 (self.x + self.width, self.y + self.height), 2)
                pygame.draw.line(WIN, BLACK, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height),
                                 2)

                # add text to button
                text_img = FONT.render(self.text, True, self.text_color)
                text_len = text_img.get_width()
                WIN.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 20))
        else:
            pygame.draw.rect(WIN, self.button_color, button_rect)

            # add shading to button
            pygame.draw.line(WIN, WHITE, (self.x, self.y), (self.x + self.width, self.y), 2)
            pygame.draw.line(WIN, WHITE, (self.x, self.y), (self.x, self.y + self.height), 2)
            pygame.draw.line(WIN, BLACK, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
            pygame.draw.line(WIN, BLACK, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

            # add text to button
            text_img = FONT.render(self.text, True, self.text_color)
            text_len = text_img.get_width()
            WIN.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 20))
        return action


# Create buttons for game intro
START_BUTTON = button(WIDTH // 2 - 100, HEIGHT // 2 + 200, 'START', GREEN, LIGHT_GREEN, DARK_GREEN)


# INFO = button(600, 500, 'HELP', RED, LIGHT_RED, DARK_RED)


def game_intro():
    intro = True
    while intro:
        WIN.fill(DARK_RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        image = pygame.image.load('uno_assets_2d/PNGs/large/uno_cards.png')
        WIN.blit(image, (WIDTH // 2 - 180, HEIGHT // 2 - 250))

        # if INFO.draw_button():

        if START_BUTTON.draw_button():
            print("The game has started")
            WIN.fill(DARK_RED)
            intro = False

        pygame.display.update()


TWO_PLAYERS = button(WIDTH // 2 - 400, HEIGHT // 2, "2 Players", GREY, LIGHT_GREY, DARK_GREY)
THREE_PLAYERS = button(WIDTH // 2 - 100, HEIGHT // 2, "3 Players", GREY, LIGHT_GREY, DARK_GREY)
FOUR_PLAYERS = button(WIDTH // 2 + 200, HEIGHT // 2, "4 Players", GREY, LIGHT_GREY, DARK_GREY)


def game_menu():
    intro = True
    while intro:
        WIN.fill(DARK_RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        text = BIG_FONT.render('How many players?', True, BLACK)
        WIN.blit(text, (WIDTH // 2 - 250, HEIGHT // 2 - 250))
        if TWO_PLAYERS.draw_button():
            config.player_headcount = 2
            WIN.fill(DARK_RED)
            intro = False
        if THREE_PLAYERS.draw_button():
            config.player_headcount = 3
            WIN.fill(DARK_RED)
            intro = False
        if FOUR_PLAYERS.draw_button():
            config.player_headcount = 4
            WIN.fill(DARK_RED)
            intro = False
        pygame.display.update()


GO_BUTTON = button(700, 500, 'GO!', GREEN, LIGHT_GREEN, DARK_GREEN)


def ready_menu():
    intro = True
    while intro:
        WIN.fill(DARK_RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        sentence = "Player %d it is your turn!" % player_num
        text = BIG_FONT.render(sentence, True, BLACK)
        WIN.blit(text, (450, 200))
        sentence = "Click the GO button when you are ready."
        text = BIG_FONT.render(sentence, True, BLACK)
        WIN.blit(text, (300, 260))
        if GO_BUTTON.draw_button():
            print("Player %d 's turn has started" % player_num)
            WIN.fill(DARK_RED)
            intro = False

        pygame.display.update()


# def display_cards(top_card, player ):
def display_cards(Players):
    image = pygame.image.load('uno_assets_2d/PNGs/small/card_back.png')
    loop = True
    while loop:
        WIN.fill(DARK_RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        # Display with 2 people
        arrowA = pygame.image.load('uno_assets_2d/PNGs/large/Arrow.png')
        arrowA = pygame.transform.rotate(arrowA, 270)
        WIN.blit(arrowA, (750, 400))
        arrowB = pygame.transform.flip(arrowA, True, True)
        WIN.blit(arrowB, (450, 400))

        # print the active players deck of cards
        split = 1500 // Players[player_num - 1].getAmountOfCards()
        for i in range(Players[player_num - 1].getAmountOfCards()):
            print(Players[player_num].deck.deck[i].getCardColor())
            print(Players[player_num].deck.deck[i].getCardNumber())
            card = pygame.image.load(Players[player_num].deck.deck[i].cardFileAsset())
            WIN.blit(card, (split, 800))
            split += 150

        # Print the board for only two players playing
        if config.player_headcount == 2:
            image = pygame.transform.flip(image, True, True)
            A, B = 500, 100
            # print the other players cards face down
            if player_num == 1:

                for i in range(Players[1].getAmountOfCards()):
                    WIN.blit(image, (A, B))
                    A += 50
            else:
                for i in range(Players[0].getAmountOfCards()):
                    WIN.blit(image, (A, B))
                    A += 50

        # Display with three people
        if config.player_headcount == 3:
            A, B = 100, 300
            C, D = 1200, 300
            if player_num == 1:
                image = pygame.transform.rotate(image, 270)
                for i in range(Players[1].getAmountOfCards()):
                    WIN.blit(image, (A, B))
                    B += 50
                image = pygame.transform.rotate(image, 180)
                for i in range(Players[2].getAmountOfCards()):
                    WIN.blit(image, (C, D))
                    D += 50
            elif player_num == 2:
                image = pygame.transform.rotate(image, 270)
                for i in range(Players[0].getAmountOfCards()):
                    WIN.blit(image, (A, B))
                    B += 50
                image = pygame.transform.rotate(image, 180)
                for i in range(Players[2].getAmountOfCards()):
                    WIN.blit(image, (C, D))
                    D += 50

            elif player_num == 3:
                image = pygame.transform.rotate(image, 270)
                for i in range(Players[1].getAmountOfCards()):
                    WIN.blit(image, (A, B))
                    B += 50
                image = pygame.transform.rotate(image, 180)
                for i in range(Players[0].getAmountOfCards()):
                    WIN.blit(image, (C, D))
                    D += 50

        # Display for 4 people
        if config.player_headcount == 4:
            A, B = 100, 300
            C, D = 500, 100
            E, F = 1200, 300

            if player_num == 1:
                # player to the right

                for i in range(Players[3].getAmountOfCards()):
                    WIN.blit(image, (A, B))
                    B += 50

                # player at the top
                image = pygame.transform.rotate(image, 90)
                for i in range(Players[2].getAmountOfCards()):
                    WIN.blit(image, (C, D))
                    C += 50

                # Player to the left
                image = pygame.transform.rotate(image, 180)
                for i in range(Players[1].getAmountOfCards()):
                    WIN.blit(image, (E, F))
                    F += 50

            elif player_num == 2:
                # player to the right
                for i in range(Players[0].getAmountOfCards()):
                    WIN.blit(image, (A, B))
                    B += 50

                # player at the top
                image = pygame.transform.rotate(image, 90)
                for i in range(Players[3].getAmountOfCards()):
                    WIN.blit(image, (C, D))
                    C += 50

                # Player to the left
                image = pygame.transform.rotate(image, 180)
                for i in range(Players[2].getAmountOfCards()):
                    WIN.blit(image, (E, F))
                    F += 50

            elif player_num == 3:
                # player to the right
                for i in range(Players[1].getAmountOfCards()):
                    WIN.blit(image, (A, B))
                    B += 50

                # player at the top
                image = pygame.transform.rotate(image, 90)
                for i in range(Players[0].getAmountOfCards()):
                    WIN.blit(image, (C, D))
                    C += 50

                # Player to the left
                image = pygame.transform.rotate(image, 180)
                for i in range(Players[3].getAmountOfCards()):
                    WIN.blit(image, (E, F))
                    F += 50

            elif player_num == 4:
                # player to the right

                for i in range(Players[2].getAmountOfCards()):
                    WIN.blit(image, (A, B))
                    B += 50

                # player at the top
                image = pygame.transform.rotate(image, 90)
                for i in range(Players[0].getAmountOfCards()):
                    WIN.blit(image, (C, D))
                    C += 50

                # Player to the left
                image = pygame.transform.rotate(image, 180)
                for i in range(Players[1].getAmountOfCards()):
                    WIN.blit(image, (E, F))
                    F += 50

        # display the deck
        image = pygame.image.load('uno_assets_2d/PNGs/small/card_back.png')
        image2 = pygame.image.load('uno_assets_2d/PNGs/small/card_back.png')
        image3 = pygame.image.load('uno_assets_2d/PNGs/small/card_back.png')
        image4 = pygame.image.load('uno_assets_2d/PNGs/small/card_back.png')
        image5 = pygame.image.load('uno_assets_2d/PNGs/small/card_back.png')

        WIN.blit(image, (650, 400))
        WIN.blit(image2, (647, 403))
        WIN.blit(image3, (644, 406))
        WIN.blit(image4, (641, 409))
        WIN.blit(image5, (638, 412))

        # display the top card
        # card = pygame.image.load(top_card.card_file_asset)

        pygame.display.update()
