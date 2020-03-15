from random import choice

class FruitGame:
    def __init__(self):
        self.hidden_word = []
        self.letter = None
        self.list_object = []
        self.random_word = None
        self.number_of_letters = 0
        
    @property
    def list_object(self):
        return self._list_object
    
    @list_object.setter
    def list_object(self, list_object):
        self._list_object = list_object
        
    @property
    def random_word(self):
        return self._random_word
    
    @random_word.setter
    def random_word(self, random_word):
        if isinstance(random_word, list):
            self._random_word = choice(random_word)
            
    def chosen_a_letter(self, letter = None):
        if isinstance(letter, str):
            self.letter = input("Escolha uma letra: ")
        else:
            self.chosen_a_letter('')
    
    def choose_a_word(self):
        list_of_words = choice([["maca","banana","pera","uva","tomate","abacaxi","pessego"],
                                ["morango","melao","melancia","maracuja"]])
        
        print(list_of_words)
        self.list_object = list_of_words
        self.random_word = self.list_object
        
        
    def hide_random_word_from_the_game(self):    
        for index in self.random_word:
            self.hidden_word.append("_")
        self.number_of_letters = len(self.random_word)
        return self.hidden_word

    def search_letter_in_the_list(self):
        while True:
                
            self.chosen_a_letter()
            
            if self.letter in self.random_word:
                print("Sua Letra foi encontrada na palavra! ")
            else:
                print("Sua Letra não existe na palavra! ")
            
            for index, index_letter in enumerate(self.random_word):
                if self.letter == index_letter:
                    self.hidden_word[index] = self.letter
            print(self.hidden_word)
                     
            if not '_' in self.hidden_word:
                self.hidden_word.clear()
                break
            
        return self.hidden_word
    
if __name__ == "__main__":
    game = FruitGame()
    
    
    while True:
            
        game.choose_a_word()
        hidden_word = game.hide_random_word_from_the_game()
        print(f"A Fruta oculta tem {game.number_of_letters} letras: {hidden_word}")
        game.search_letter_in_the_list()
        
        