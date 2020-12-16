from random import choice, randint
from sys import exit


class BlackJack:
    def __init__(self):
        self.sum_result = 0
        self.list_sequence_card = []

    def organization_of_game_cards(self):
        game_cards = {"2":2,"3": 3,"4": 4,"5": 5,
                    "6": 6,"7": 7,"8": 8,"9": 9,
                    "10": 10,"A": 1,"J": 10,
                    "Q": 10,"K": 10
                    }
        return game_cards

    def randomize_card(self, game_cards):
        list_cards = list(game_cards.items())
        random_card = choice(list_cards)
        return random_card

    def computer_decision_to_pick_up_the_card(self, card, list_result_players):
        if self.sum_result >= 11:
            random_decision = randint(0,1)
            if random_decision:
                print("O computador aceitou uma nova carta!")
                self.sum_the_results_of_the_cards(card)
            else:
                print("O computador desistiu da proxima carta!")  
                print(f"Sua pontuação final: {self.sum_result}")
                print(f"Sua Sequencia de cartas: {self.list_sequence_card}")
        else:
            self.sum_the_results_of_the_cards(card)

        if self.sum_result == 21 and self.sum_result == max(list_result_players):
            print("O Computador empatou com um player!")
            exit()
        elif self.sum_result > 21:
            print("O Computador perdeu a partida!")
            exit()
        elif self.sum_result == 21:
            print("O Computador venceu a partida!")
            exit()

    def sum_the_results_of_the_cards(self, card):
        self.list_sequence_card.append(card[0])
        self.sum_result += card[1]

        print(self.sum_result)
        print(self.list_sequence_card)


game = BlackJack()
list_result_players = [5,6,14,17]

while True:

    print(f"Sistema escolheu uma carta!")
    input()    

    game_cards = game.organization_of_game_cards()
    random_card = game.randomize_card(game_cards)
    game.computer_decision_to_pick_up_the_card(random_card, list_result_players)
