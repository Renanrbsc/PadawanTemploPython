from sys import path, exit
path.append(r"C:\Users\renan.ribas\Documents\Github\PadawanTemploPython\Desafio1_Game_BlackJack")

from random import randint

from Controller.game_base import BlackJackDefinitions


class Player(BlackJackDefinitions):
    def __init__(self, name):
        self.name = name
        super().__init__()

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if name == '':
            self._name = input("Digite o Nome do player: ")

    def organization_of_game_cards(self):
        return super().organization_of_game_cards()
        
    def randomize_card(self, game_cards):
        return super().randomize_card(game_cards)
        
    def player_decision_to_pick_up_the_card(self, card):
        if self.sum_result >= 11:
            
            print("Deseja obter a proxima carta?")
            random_decision = int(input("(Sim - 1, Não - 0): "))

            if random_decision:
                if card[0] == "A" and self.list_sequence_card is None:
                    card = ("A", 11)
                print(f"O Jogador {self.name} aceitou uma nova carta!")
                super().sum_the_results_of_the_cards(card)
            else:
                print(f"O Jogador {self.name} desistiu da proxima carta!")  
                print(f"Sua pontuação final: {self.sum_result}")
                print(f"Sua Sequencia de cartas: {self.list_sequence_card}")
        else:
            super().sum_the_results_of_the_cards(card)

