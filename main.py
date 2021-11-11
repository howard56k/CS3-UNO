from UNO import *
from FrontEnd import *
global player_num
game_intro()
game_menu()
New_game = Uno(player_num, 7)
ready_menu(player_num)
display_cards()