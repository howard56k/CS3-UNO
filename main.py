from UNO import *
from FrontEnd import *
global player_headcount
game_intro()
game_menu()
New_game = Uno(player_headcount, 7)
ready_menu()
display_cards()