from UNO import *
import config
from FrontEnd import *
global player_num

# is there a reverse?
reverse = config.reverse


# Opening introduction to the game
game_intro()

# Finds out how many players will be playing the game
game_menu()
player_headcount = config.player_headcount
print(config.player_headcount)
# Creates the new game with the amount of players selected above, starting with 7 cards
New_game = Uno(player_headcount, 7)

# Game loop
while New_game.checkIfWinner() == None :

    # Prompts the first player to get ready for their turn
    ready_menu()
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

    display_cards(players_list)
    for i in range(playerA.getAmountOfCards()):
        print(playerA.deck.deck[i].getCardColor())
        print(playerA.deck.deck[i].getCardNumber())

    # Move to the next players turn, if reverse, move in the other direction
    if reverse:
        if player_num == 4:
            player_num = 1
        else:
            player_num += 1
    else:
        if player_num == 1:
            player_num = 4
        else:
            player_num -= 1
