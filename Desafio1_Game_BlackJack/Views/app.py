import sys
sys.path.append(r"C:\Users\renan.ribas\Documents\Github\PadawanTemploPython\Desafio1_Game_BlackJack")
sys.path.append(r"C:\Users\Usuario\Documents\GitHub\PadawanTemploPython\Desafio1_Game_BlackJack")

from Controller.controller_view import ControllerView
from Controller.computer import Computer
from Controller.player import Player


print(f"\n" \
      f"Bem Vindos ao Jogo de cartas!\n" \
      f"------ BlackJack - 21 ------\n")

controller = ControllerView()
computer1 = Computer('')
player1 = Player('')
player2 = Player('')

list_players = [computer1, player1, player2]
list_result_players = []

for index, player in enumerate(list_players):
    print(f"Player{index+1} - {player.name}")

while True:
    
    for index, round_player in enumerate(list_players):   
        print(f"\nPlayer{index+1} - {round_player.name} está na vez!!")
        game_cards = round_player.organization_of_game_cards()
        random_card = round_player.randomize_card(game_cards)
        round_player.player_decision_to_pick_up_the_card(random_card)
                    
        list_result_players.append([round_player.name, round_player.sum_result])
        print(f"\nPlacar: {list_result_players}")
        
    for result in list_result_players: 
        controller.final_result(result[0], result[1])
        
    list_result_players = []
        

    
    