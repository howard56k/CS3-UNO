import sys
import pygame
import config
from pygame.locals import *
from UNO import *
from time import sleep

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
LIGHT_BLUE = (0, 128, 255)
DARK_BLUE = (0, 0, 190)
LIGHT_GREEN = (60, 179, 113)
DARK_GREEN = (0, 128, 0)
GREEN = (46, 139, 87)
YELLOW = (255, 255, 0)
LIGHT_YELLOW = (255, 255, 102)
DARK_YELLOW = (204, 204, 0)
LIGHT_GREY = (105, 105, 105)
GREY = (169, 169, 169)
DARK_GREY = (192, 192, 192)
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)
FPS = 60
SMALL_FONT = pygame.font.SysFont('franklingothicheavy', 20)
FONT = pygame.font.SysFont('franklingothicheavy', 40)
BIG_FONT = pygame.font.SysFont('franklingothicheavy', 60)
JUMBO_FONT = pygame.font.SysFont('franklinothicheavy', 120)
clicked = False
winner = False


# How many players there are

# Set icon and caption

icon = pygame.image.load('uno_assets_2d/PNGs/small/uno_logo.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("UNO!")


# Create a button class that handles all of the buttons created in the game
class button:
    # button class variables
    text_color = BLACK
    width = 200
    height = 80

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

# A function that draws cards
def draw_card( x, y, img):
        global clicked
        action = False

        # Get the position of the mouse
        pos = pygame.mouse.get_pos()

        card = pygame.image.load(img)
        # a rectangle in the same spot as the card
        rect = Rect(x, y, 130, 182)
        # Check if the card clicked
        if rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                WIN.blit(card, (x - 10, y - 10))


            elif pygame.mouse.get_pressed()[0] == 0 and clicked:
                clicked = False
                action = True

            else:
                WIN.blit(card, (x - 5, y - 5))
        else:
            WIN.blit(card, (x , y ))

        return action

# Create buttons for game intro
START_BUTTON = button(WIDTH // 2 - 100, HEIGHT // 2 + 200, 'START', GREEN, LIGHT_GREEN, DARK_GREEN)

# Introduction to the game
def game_intro():
    intro = True
    while intro:
        WIN.fill(DARK_RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        image = pygame.image.load('uno_assets_2d/PNGs/large/uno_cards.png')
        WIN.blit(image, (WIDTH // 2 - 207, HEIGHT // 2 - 250))

        # if INFO.draw_button():

        if START_BUTTON.draw_button():
            print("The game has started")
            WIN.fill(DARK_RED)
            intro = False

        pygame.display.update()

TWO_PLAYERS = button(WIDTH // 2 - 400, HEIGHT // 2, "2 Players", GREY, LIGHT_GREY, DARK_GREY)
THREE_PLAYERS = button(WIDTH // 2 - 100, HEIGHT // 2, "3 Players", GREY, LIGHT_GREY, DARK_GREY)
FOUR_PLAYERS = button(WIDTH // 2 + 200, HEIGHT // 2, "4 Players", GREY, LIGHT_GREY, DARK_GREY)

# game menu that finds out how many players are playing
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

GO_BUTTON = button(WIDTH // 2 - 100, HEIGHT // 2, 'GO!', GREEN, LIGHT_GREEN, DARK_GREEN)

# Prompts the player to be ready to play
def ready_menu():
    intro = True
    while intro:
        WIN.fill(DARK_RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        temp = config.player_num+1
        sentence = "Player %d it is your turn!" % temp
        text = BIG_FONT.render(sentence, True, BLACK)
        WIN.blit(text, (400, 200))
        sentence = "Click the GO button when you are ready."
        text = BIG_FONT.render(sentence, True, BLACK)
        WIN.blit(text, (200, 300))
        if GO_BUTTON.draw_button():
            print("Player %d 's turn has started" % temp)
            WIN.fill(DARK_RED)
            intro = False

        pygame.display.update()

# Color change prompt box
def color_change():
    print ("inside color changer function")
    pygame.draw.rect(WIN, BLACK, pygame.Rect(500, 500, WIDTH//2 - 250, HEIGHT//2 - 250))
    text = BIG_FONT.render("What color do you want to change to?", True, WHITE)
    WIN.blit(text, (500, 300))
    RED_BUTTON = button(600, 400, "RED", RED, LIGHT_RED, DARK_RED)
    BLUE_BUTTON = button(600, 800 , "BLUE", BLUE, LIGHT_BLUE, DARK_BLUE)
    GREEN_BUTTON = button(800, 400 , "GREEN", GREEN, LIGHT_GREEN, DARK_GREEN)
    YELLOW_BUTTON = button(800, 800, "YELLOW", YELLOW, LIGHT_YELLOW, DARK_YELLOW)
    if RED_BUTTON.draw_button():
        return "red"
    elif BLUE_BUTTON.draw_button():
        return "blue"
    elif GREEN_BUTTON.draw_button():
        return "green"
    elif YELLOW_BUTTON.draw_button():
        return "yellow"

    pygame.display.update()


def display_cards(Players, discardDeck, pickUpPile):
    # image = pygame.image.load('uno_assets_2d/PNGs/small/card_back.png')
    pause = False
    loop = True
    while loop:
        WIN.fill(DARK_RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        # Display the arrows
        arrowA = pygame.image.load('uno_assets_2d/PNGs/large/Arrow.png')
        if config.reverse:
            top_Right = pygame.transform.flip(arrowA, True, False)
            top_Right = pygame.transform.rotate(top_Right, 90)
            WIN.blit(top_Right, (855, 340))
            bottom_Left = pygame.transform.rotate(top_Right, 180)
            WIN.blit(bottom_Left, (540, 540))
        else:
            top_Right = pygame.transform.rotate(arrowA, 180)
            WIN.blit(top_Right, (840, 320))
            bottom_Left = pygame.transform.flip(top_Right, True, True)
            WIN.blit(bottom_Left, (550, 560))

        # display the deck
        image = pygame.image.load('uno_assets_2d/PNGs/small/card_back.png')
        Y = 400
        for i in range(5):
            WIN.blit(image, (615, Y))
            Y += 3

        # Add a new random card from the pickup deck and exit function
        if draw_card(615, 415, 'uno_assets_2d/PNGs/small/card_back.png'):
            Players[config.player_num].addCard(pickUpPile.returnCardFromDeck())
            return 0

        # display card at the top of the discard pile
        dispCard = pygame.image.load(discardDeck[len(discardDeck) - 1].cardFileAsset())
        WIN.blit(dispCard, (770, 415))

        # print the active players deck of cards
        split = 1500 // Players[config.player_num].getAmountOfCards()
        for i in range(Players[config.player_num].getAmountOfCards()):
            card_file = Players[config.player_num].deck.deck[i].cardFileAsset()

            # draws all of the card options
            if draw_card(split, 800, card_file):

                # if the card can be placed
                print(Players[config.player_num].deck.deck[i].getCardColor(), end=" ")
                print(Players[config.player_num].deck.deck[i].getCardNumber())
                print("is card placeable -> ", end="")
                print(Players[config.player_num].deck.deck[i].isCardPlaceable(Players[config.player_num].deck.deck[i]))
                print("is card special -> ", end="")
                print(Players[config.player_num].deck.deck[i].special)
                if discardDeck[len(discardDeck) - 1].isCardPlaceable(Players[config.player_num].deck.deck[i]):
                    print("IM INSIDE THE PLACEABLE LOOP")
                    # if card is reverse
                    if Players[config.player_num].deck.deck[i].getCardNumber == 'reverse':

                        config.reverse = not config.reverse
                        print("TIME TO REVERSE -> ", end="")
                        print(config.reverse)
                    # if card is skip
                    elif Players[config.player_num].deck.deck[i].getCardNumber == 'skip':

                        if config.reverse:
                            if config.player_headcount == 2:
                                if config.player_num == 0:
                                    config.player_num = 0
                                elif config.player_num == 1:
                                    config.player_num = 1
                            elif config.player_headcount == 3:
                                if config.player_num == 0:
                                    config.player_num = 2
                                else:
                                    config.player_num -= 1
                            elif config.player_headcount == 4:
                                if config.player_num == 0:
                                    config.player_num = 3
                                else:
                                    config.player_num -= 1
                        else:
                            if config.player_headcount == 2:
                                if config.player_num == 0:
                                    config.player_num = 1
                                elif config.player_num == 1:
                                    config.player_num = 0
                            elif config.player_headcount == 3:
                                if config.player_num == 2:
                                    config.player_num = 0
                                else:
                                    config.player_num += 1
                            elif config.player_headcount == 4:
                                if config.player_num == 3:
                                    config.player_num = 0
                                else:
                                    config.player_num += 1
                        print("TIME TO SKIP -> next player is ")
                        print(config.player_num)
                    # if card is plus two
                    elif Players[config.player_num].deck.deck[i].getCardNumber == 'picker':
                        if config.reverse:
                            Players[config.player_num - 1].addCard(pickUpPile.returnCardFromDeck())
                            Players[config.player_num - 1].addCard(pickUpPile.returnCardFromDeck())
                        else:
                            Players[config.player_num + 1].addCard(pickUpPile.returnCardFromDeck())
                            Players[config.player_num + 1].addCard(pickUpPile.returnCardFromDeck())

                    # if card is special
                    elif Players[config.player_num].deck.deck[i].special:
                        #if the card played is a plus four
                        print( "the specialty card number is -> ", end="")
                        print(Players[config.player_num].deck.deck[i].getCardNumber())
                        if Players[config.player_num].deck.deck[i].getCardNumber() == 'pick_four':
                            print("inside pick 4 card loop")
                            if config.reverse:
                                Players[config.player_num - 1].addCard(pickUpPile.returnCardFromDeck())
                                Players[config.player_num - 1].addCard(pickUpPile.returnCardFromDeck())
                                Players[config.player_num - 1].addCard(pickUpPile.returnCardFromDeck())
                                Players[config.player_num - 1].addCard(pickUpPile.returnCardFromDeck())
                            else:
                                Players[config.player_num + 1].addCard(pickUpPile.returnCardFromDeck())
                                Players[config.player_num + 1].addCard(pickUpPile.returnCardFromDeck())
                                Players[config.player_num + 1].addCard(pickUpPile.returnCardFromDeck())
                                Players[config.player_num + 1].addCard(pickUpPile.returnCardFromDeck())
                            #function that prompts color change
                            new_color = color_change()
                            Players[config.player_num].deck.deck[i].setCardColor(new_color)

                        # If the card is a color changer
                        elif Players[config.player_num].deck.deck[i].getCardNumber() == 'color_changer':
                            print("inside color change card loop")
                            Players[config.player_num].deck.deck[i].setCardColor(color_change())
                    discardDeck.append(Players[config.player_num].deck.deck[i])
                    Players[config.player_num].deck.removeFromDeck(i)
                    return 0

                # Else if the card doesnt match, Create a fading pop up that says that the card does not match - text prompt - card not placeable
                else:
                    pause = True
                    #wrong card pop up
                    text = JUMBO_FONT.render("CARD NOT VALID", True, RED)
                    WIN.blit(text, (400, 450))
            split += 150

        # Print the board for only 2 players playing
        if config.player_headcount == 2:
            image = pygame.transform.flip(image, True, True)
            A, B = 500, 100
            # print the other players cards face down
            if config.player_num == 0:

                for i in range(Players[1].getAmountOfCards()):
                    WIN.blit(image, (A, B))
                    A += 50
            else:
                for i in range(Players[0].getAmountOfCards()):
                    WIN.blit(image, (A, B))
                    A += 50

        # Display with 3 people
        if config.player_headcount == 3:
            A, B = 100, 300
            C, D = 1200, 300
            if config.player_num == 0:
                image = pygame.transform.rotate(image, 270)
                for i in range(Players[1].getAmountOfCards()):
                    WIN.blit(image, (A, B))
                    B += 50
                image = pygame.transform.rotate(image, 180)
                for i in range(Players[2].getAmountOfCards()):
                    WIN.blit(image, (C, D))
                    D += 50
            elif config.player_num == 1:
                image = pygame.transform.rotate(image, 270)
                for i in range(Players[0].getAmountOfCards()):
                    WIN.blit(image, (A, B))
                    B += 50
                image = pygame.transform.rotate(image, 180)
                for i in range(Players[2].getAmountOfCards()):
                    WIN.blit(image, (C, D))
                    D += 50

            elif config.player_num == 2:
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

            if config.player_num == 0:
                # player to the right
                imageR = pygame.transform.rotate(image, 270)
                for i in range(Players[3].getAmountOfCards()):
                    WIN.blit(imageR, (A, B))
                    B += 50

                # player at the top
                imageT = pygame.transform.rotate(image, 180)
                for i in range(Players[2].getAmountOfCards()):
                    WIN.blit(imageT, (C, D))
                    C += 50

                # Player to the left
                imageL = pygame.transform.rotate(image, 90)
                for i in range(Players[1].getAmountOfCards()):
                    WIN.blit(imageL, (E, F))
                    F += 50

            elif config.player_num == 1:
                # player to the right
                imageR = pygame.transform.rotate(image, 270)
                for i in range(Players[0].getAmountOfCards()):
                    WIN.blit(imageR, (A, B))
                    B += 50

                # player at the top
                imageT = pygame.transform.rotate(image, 180)
                for i in range(Players[3].getAmountOfCards()):
                    WIN.blit(imageT, (C, D))
                    C += 50

                # Player to the left
                imageL = pygame.transform.rotate(image, 270)
                for i in range(Players[2].getAmountOfCards()):
                    WIN.blit(imageL, (E, F))
                    F += 50

            elif config.player_num == 2:
                # player to the right
                imageR = pygame.transform.rotate(image, 270)
                for i in range(Players[1].getAmountOfCards()):
                    WIN.blit(imageR, (A, B))
                    B += 50

                # player at the top
                imageT = pygame.transform.rotate(image, 180)
                for i in range(Players[0].getAmountOfCards()):
                    WIN.blit(imageT, (C, D))
                    C += 50

                # Player to the left
                imageL = pygame.transform.rotate(image, 270)
                for i in range(Players[3].getAmountOfCards()):
                    WIN.blit(imageL, (E, F))
                    F += 50

            elif config.player_num == 3:
                # player to the right
                imageR = pygame.transform.rotate(image, 270)
                for i in range(Players[2].getAmountOfCards()):
                    WIN.blit(imageR, (A, B))
                    B += 50

                # player at the top
                imageT = pygame.transform.rotate(image, 180)
                for i in range(Players[0].getAmountOfCards()):
                    WIN.blit(imageT, (C, D))
                    C += 50

                # Player to the left
                imageL = pygame.transform.rotate(image, 270)
                for i in range(Players[1].getAmountOfCards()):
                    WIN.blit(imageL, (E, F))
                    F += 50

        if pause:
            pygame.display.update()
            sleep(1.5)
            pause = False
        pygame.display.update()

# WINNING AND GAME OVER DIALOGUE BOX