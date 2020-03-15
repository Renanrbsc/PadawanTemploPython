from random import choice

class FruitGame:
    def __init__(self, random_word = ''):
        self.hidden_word = []
        self.chosen_letter = "a"
        self.list_object = ["maca","banana","pera","uva","tomate","abacaxi","pessego"]
        self.random_word = random_word
        self.number_of_letters = 0
        
    # @property
    # def list_object(self):
    #     return self._list_object
    
    # @list_object.setter
    # def list_object(self, list_object):
    #     if isinstance(list_object, str):
    #         self._list_object = ["maca","banana","pera","uva","tomate","abacaxi","pessego"]
        
    @property
    def random_word(self):
        return self._random_word
    
    @random_word.setter
    def random_word(self, random_word):
        if isinstance(random_word, str):
            self._random_word = choice(self.list_object)
        
    def hide_random_word_from_the_game(self):    
        for index in self.random_word:
            self.hidden_word.append("_")
        self.number_of_letters = len(self.random_word)
        return self.hidden_word

    def search_letter_in_the_list(self):
        if self.chosen_letter in self.random_word:
            print("Sua Letra foi encontrada na palavra! ")
        else:
            print("Sua Letra não existe na palavra! ")
        for index, letter in enumerate(self.random_word):
            if self.chosen_letter == letter:
                self.hidden_word[index] = self.chosen_letter
        print(self.hidden_word)
        return self.hidden_word
    
if __name__ == "__main__":
    game = FruitGame()
    hidden_word = game.hide_random_word_from_the_game()
    print(f"A Fruta oculta tem {game.number_of_letters} letras: {hidden_word}")
    game.search_letter_in_the_list()
        