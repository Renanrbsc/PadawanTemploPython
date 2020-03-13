import sys
sys.path.append(r"C:\Users\renan.ribas\Documents\Github\PadawanTemploPython\Desafio1_Game_BlackJack")

from Controller.computer import Computer
from Controller.player import Player

computer1 = Computer('')
player1 = Player('')
player2 = Player('')

list_players = [computer1, player1, player2]
list_result_players = []

for player in list_players: 
    player.name   
    list_result_players.append(player.sum_result)

while True:

    for player in list_players:   
        print(f"Player {player.name} está na vez!!")
        input()    
        game_cards = player.organization_of_game_cards()
        random_card = player.randomize_card(game_cards)
        player.player_decision_to_pick_up_the_card(random_card)
    
    list_result_players = [computer1.sum_result,player1.sum_result,player2.sum_result]
    for player in list_players:   
        player.final_result(list_result_players)

    
    