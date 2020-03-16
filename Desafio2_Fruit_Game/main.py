from random import choice

class FruitGame:
    def __init__(self):
        self.hidden_word = []
        self.letter = None
        self.list_object = []
        self.random_word = None
        self.number_of_letters = 0
        self.wrong_attempts = 0
        
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
            
    def choose_a_letter(self, letter = None):
        if isinstance(letter, str):
            self.letter = input("Escolha uma letra: ").lower()
        else:
            self.choose_a_letter('')
    
    def choose_a_word(self):
        list_of_words = ["maca","banana","pera",
                         "uva","tomate","abacaxi",
                         "pessego","morango","melao",
                         "melancia","maracuja","laranja"
                         ]
        self.list_object = list_of_words
        self.random_word = self.list_object
        return list_of_words
        
    def hide_random_word_from_the_game(self):    
        for index in self.random_word:
            self.hidden_word.append("_")
        self.number_of_letters = len(self.random_word)
        print(f"A Fruta oculta tem {self.number_of_letters} letras: {self.hidden_word}\n")

    def ensure_that_exists_in_the_list(self):  
        if self.letter in self.random_word:
            print("\nSua Letra foi encontrada na palavra! ")
        else:
            print("\nSua Letra não existe na palavra! ")
            self.increment_wrong_attempts()
            
    def increment_wrong_attempts(self):
        print(f"Tentativas Atuais: {abs(5-self.wrong_attempts)} ") 
        self.wrong_attempts += 1
        print(f"Tentativas restantes: {abs(5-self.wrong_attempts)} ") 
        
    def finds_letter_in_the_word(self):
        for index, index_letter in enumerate(self.random_word):
            if self.letter == index_letter:
                self.hidden_word[index] = self.letter
        print(f"Posiçoes das letras: {self.hidden_word}\n")
        
    def transforms_the_list_in_a_string(self):
        word = ''
        for index in self.hidden_word:
            word += index
        print(f"A Fruta encontrada foi: {word.capitalize()}\n")
        
    def main_round_loop(self):
        while True:
            self.choose_a_letter()
            self.ensure_that_exists_in_the_list()
            self.finds_letter_in_the_word()
                     
            if self.wrong_attempts >= 5:
                print("Suas tentativas acabaram.\n" \
                    "Tente uma nova palavra!\n")
                self.wrong_attempts = 0
                self.hidden_word.clear()
                break
            
            if not '_' in self.hidden_word:
                self.transforms_the_list_in_a_string()
                self.wrong_attempts = 0
                self.hidden_word.clear()
                break
            
    
if __name__ == "__main__":
    game = FruitGame()
    
    print(f"\n#----- Jogo da Fruta -----#\n" \
            f" --  Forca de Palavras  -- \n")   
    
    for index in range(10):
        
        print(f"#----- Rodada {index+1} -----#\n" \
              f"Voce tem 5 chances de acertar a palavra!\n")
        
        print(f"Lista de Palavras: {game.choose_a_word()}\n")
        game.hide_random_word_from_the_game()
        game.main_round_loop()
        
        