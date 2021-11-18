from UNO import *
import config
from FrontEnd import *


# is there a reverse?
reverse = config.reverse
gameLoop = True
while gameLoop:
    # Opening introduction to the game
    game_intro()

    # Finds out how many players will be playing the game
    game_menu()
    player_headcount = config.player_headcount
    print(config.player_headcount)
    # Creates the new game with the amount of players selected above, starting with 7 cards
    New_game = Uno(player_headcount, 3)

    # Game loop
    discard_Deck = []
    discard_Deck.append(New_game.tableDeck.deck[New_game.tableDeck.getDeckSize()-1])
    New_game.tableDeck.removeFromDeck(New_game.tableDeck.getDeckSize()-1)

    players_list = []
    playerA = New_game.listOfPlayers[0]
    players_list.append(playerA)
    playerB = New_game.listOfPlayers[1]
    players_list.append(playerB)
    if player_headcount > 2:
        playerC = New_game.listOfPlayers[2]
        players_list.append(playerC)
    if player_headcount > 3:
        playerD = New_game.listOfPlayers[3]
        players_list.append(playerD)

    while New_game.checkIfWinner() == None :
        # Prompts the first player to get ready for their turn
        ready_menu()
        display_cards(players_list, discard_Deck, New_game.board)

        # Move to the next players turn, if reverse, move in the other direction
        if reverse:
            if player_headcount == 2:
                if config.player_num == 0:
                    config.player_num = 1
                elif config.player_num == 1:
                    config.player_num = 0
            elif player_headcount == 3:
                if config.player_num == 0:
                    config.player_num = 2
                else:
                    config.player_num -= 1
            elif player_headcount == 4:
                if config.player_num == 0:
                    config.player_num = 3
                else:
                    config.player_num -= 1
        else:
            if player_headcount == 2:
                if config.player_num == 0:
                    config.player_num = 1
                elif config.player_num == 1:
                    config.player_num = 0
            elif player_headcount == 3:
                if config.player_num == 2:
                    config.player_num = 0
                else:
                    config.player_num += 1
            elif player_headcount == 4:
                if config.player_num == 3:
                    config.player_num = 0
                else:
                    config.player_num += 1
        for i in range(len(players_list)):
            if (len(players_list[i].deck.deck) == 0):
                print('WINNER FOUND')
                gameLoop = winner_screen(players_list)
                break