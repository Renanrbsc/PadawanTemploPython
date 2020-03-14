import sys
sys.path.append(r"C:\Users\renan.ribas\Documents\Github\PadawanTemploPython\Desafio1_Game_BlackJack")
sys.path.append(r"C:\Users\Usuario\Documents\GitHub\PadawanTemploPython\Desafio1_Game_BlackJack")

from Controller.controller_view import ControllerView
from Controller.computer import Computer
from Controller.player import Player


print(f"\n" \
      f"Bem Vindos ao Jogo de cartas!\n" \
      f"------ BlackJack - 21 ------\n")


class Game:
    def __init__(self, size):
                
        self.size = size
        self.controller = ControllerView()
        self.computer = Computer('')
        self.list_result_players = []
        self.list_winning_player = []
        self.list_losing_player = []
    
    @property
    def size(self):
        return self._size    
    @size.setter
    def size(self, size):
        if size == '':
            self._size = int(input("Digite a quantidade de jogadores: "))

    def loop_menu_instance_players(self):
        self.list_players = [self.computer]
        print("\n------ Jogadores ------\n")
        
        for i in range(0,self._size):
            
            self.list_players.append(Player(''))
            
        for index, player in enumerate(self.list_players):
            print(f"Player{index+1} - {player.name}")

    def loop_round_game(self):
            
        while True:
            
            for index, round_player in enumerate(self.list_players):   
                input()
                print(f"\nPlayer{index+1} - {round_player.name} está na vez!!")
                game_cards = round_player.organization_of_game_cards()
                random_card = round_player.randomize_card(game_cards)
                round_player.player_decision_to_pick_up_the_card(random_card)
                            
                self.list_result_players.append([round_player.name, round_player.sum_result])
            
            print(f"\nPlacar: {self.list_result_players}")
            input()
                
            for result in self.list_result_players: 
                self.controller.final_result(result[0], result[1])
            
            self.list_winning_player.extend(self.controller.remove_winning_players(self.list_result_players))
            self.list_losing_player.extend(self.controller.remove_losing_players(self.list_result_players))
            
            self.list_players = self.controller.remove_players_finally(self.list_players, self.list_losing_player, self.list_winning_player)
            
            self.controller.check_last_player(self.list_players, self.list_winning_player)                                                       
           
            print(f"Players Vencedores: {self.list_winning_player}")
            print(f"Players Perdedores: {self.list_losing_player}")
            
            self.list_result_players.clear()
            
            if not self.list_players:
                break
                
if __name__ == "__main__":
    game = Game('')
    
    while True:
        game.loop_menu_instance_players()
        game.loop_round_game()
        


    
    