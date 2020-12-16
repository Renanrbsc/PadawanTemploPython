from random import choice


# classe base para herança de jogadores
class BlackJackDefinitions:

    def __init__(self):
        self.sum_result = int()
        self.list_sequence_card = list()
        self.results = list()

    def organization_of_game_cards(self):
        game_cards = {"2": 2, "3": 3, "4": 4, "5": 5,
                      "6": 6, "7": 7, "8": 8, "9": 9,
                      "10": 10, "A": 1, "J": 10,
                      "Q": 10, "K": 10
                      }
        return game_cards

    def randomize_card(self, game_cards):
        list_cards = list(game_cards.items())
        random_card = choice(list_cards)
        return random_card

    def sum_the_results_of_the_cards(self, card):
        self.list_sequence_card.append(card[0])
        self.sum_result += card[1]
        print(f"Carta Recebida: {card}\n" \
              f"Nova Pontuação: {self.sum_result}\n" \
              f"Sequencia de cartas: {self.list_sequence_card}")

    def final_result(self, players: list):
        return self.results.append(players)
