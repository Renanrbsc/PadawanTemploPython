from random import choice

class BlackJackDefinitions:

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

         
    def sum_the_results_of_the_cards(self, card):
        self.list_sequence_card.append(card[0])
        self.sum_result += card[1]

        print(self.sum_result)
        print(self.list_sequence_card)

    def final_result(self, list_result_players):

        if self.sum_result == 21 and self.sum_result == max(list_result_players):
            print(f"O Computador {self.name} empatou com um player!")
            exit()
        elif self.sum_result > 21:
            print(f"O Computador {self.name} perdeu a partida!")
            exit()
        elif self.sum_result == 21:
            print(f"O Computador {self.name} venceu a partida!")
            exit()