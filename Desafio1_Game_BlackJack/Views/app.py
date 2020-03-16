# metodo para trazer o diretorio absoluto do path da pasta
# import sys
# sys.path.append(r"C:\Users\renan.ribas\Documents\Github\PadawanTemploPython\Desafio1_Game_BlackJack")

from Controller.controller_view import ControllerView
from Controller.computer import Computer
from Controller.player import Player



class Game:
    # metodo inicializador ou construtor com composiçoes do tipo associação
    def __init__(self):
                
        self.size = ''
        self.controller = ControllerView()
        self.computer = Computer('')
        self.list_result_players = []
        self.list_winning_player = []
        self.list_losing_player = []
    
    # Decoradores getters e setters
    @property
    def size(self):
        return self._size    
    @size.setter
    def size(self, size):
        if size == '':
            self._size = int(input("Digite a quantidade de jogadores: "))

    # Primeiro loop, para iniciar a quantidade de players na partida
    def loop_menu_instance_players(self):
        self.list_players = [self.computer]
        print("\n------ Jogadores ------\n")
        
        for i in range(0,self._size):
            
            self.list_players.append(Player(''))
            
        for index, player in enumerate(self.list_players):
            print(f"Player{index+1} - {player.name}")

    # Segundo loop, para iniciar cada rodada do jogo
    def loop_round_game(self):
            
        while True:
            
            for index, round_player in enumerate(self.list_players):   
                input()
                print(f"\nPlayer{index+1} - {round_player.name} está na vez!!")
                # instancia das cartas em dicionario
                game_cards = round_player.organization_of_game_cards()
                
                # randomiza um indice do dicionario em formato de tupla
                random_card = round_player.randomize_card(game_cards)
                
                # decisao do computador ou jogador herdado sobre aceitar ou nao uma nova carta
                round_player.player_decision_to_pick_up_the_card(random_card)
                
                # criando uma lista de resultados dos jogadores(nome,pontuação)            
                self.list_result_players.append([round_player.name, round_player.sum_result])
            
            # informa o placar na tela
            print(f"\nPlacar: {self.list_result_players}")
            input("Enter para continuar...\n") # enter de pausa durante a execução
            
            # busca cada pontuação e envia para "controller_view.py", regra de decisao "player perdeu ou nao"
            for result in self.list_result_players: 
                self.controller.final_result(result[0], result[1])
            
            # cria uma lista de jogadores vencedores e perdedores,
            # os duplica da lista de jogadores do game 
            # e estende-os nas listas a cada rodada
            self.list_winning_player.extend(self.controller.remove_winning_players(self.list_result_players))
            self.list_losing_player.extend(self.controller.remove_losing_players(self.list_result_players))
            
            # remove os mesmos da lista principal do game
            self.list_players = self.controller.remove_players_finally(self.list_players, self.list_losing_player, self.list_winning_player)
            
            # verifica o ultimo player restante e o insere na lista de vencedores
            self.controller.check_last_player(self.list_players, self.list_winning_player)                                                       
           
            print(f"Players Vencedores: {self.list_winning_player}")
            print(f"Players Perdedores: {self.list_losing_player}")
            
            # lispa a lista de resultados(nome,pontuação) a cada final de rodada
            self.list_result_players.clear()
            
            # verifica a lista principal de instancia de players se esta vazia
            # se sim, finaliza o loop de rodada e retorna a inserção de players 
            if not self.list_players:
                break

# verifica se é o arquivo mais a ser rodado               
if __name__ == "__main__":
    
    print(f"\n" \
        f"Bem Vindos ao Jogo de cartas!\n" \
        f"------ BlackJack - 21 ------\n")
    
    # instancia da classe game com inicialização do decorador
    # decorador pede a quantidade de players a serem instanciados
    # como composição em uma lista na classe
    game = Game()

    while True:
        # chamada dos loop principais
        game.loop_menu_instance_players()
        game.loop_round_game()
        


    
    