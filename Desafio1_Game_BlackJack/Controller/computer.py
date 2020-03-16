from random import randint

from Controller.game_base import BlackJackDefinitions

# Jogador tipo computador herdando do arquivo game_base
class Computer(BlackJackDefinitions):
    def __init__(self, name):
        self.name = name
        super().__init__()

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if name == '':
            self._name = f"Computer{randint(1000,9999)}"

    def organization_of_game_cards(self):
        return super().organization_of_game_cards()

    def randomize_card(self, game_cards):
        return super().randomize_card(game_cards)

    def player_decision_to_pick_up_the_card(self, card):
        print(f"Pontuação Atual: {self.sum_result}")
        
        if card[0] == "A" and not self.list_sequence_card:
            card = ("A", 11)
            
        if self.sum_result >= 11:
            random_decision = randint(0,1) 
            if random_decision:
                print(f"O Computador {self.name} aceitou uma nova carta!")
                super().sum_the_results_of_the_cards(card)
            else:
                print(f"O Computador {self.name} desistiu da proxima carta!")  
                print(f"Sua pontuação final: {self.sum_result}")
                print(f"Sua Sequencia de cartas: {self.list_sequence_card}")
        else:
            super().sum_the_results_of_the_cards(card)
