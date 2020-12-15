from Desafio4_Batalha_Naval.Model.model_matriz import ModelMatriz


class ModelPlayer:
    def __init__(self, number):
        self.__model_matriz = ModelMatriz()
        self.number = str(number)
        self.name_player = None
        
    @property
    def name_player(self):
        return self._name_player
    
    @name_player.setter
    def name_player(self, name):
        if name == None:
            name = input(f"Player{self.number} -> Informe seu nome:")
        self._name_player = name

    def create_matriz(self):
        
        print(f"\nPlayer{self.number}: {self.name_player}\n" \
              f"Campo de batalha naval 10 X 10")
        self.__main_matriz = self.__model_matriz.create_matriz()
        self.__model_matriz.update_array_spaces(self.__main_matriz)
        return self.__main_matriz
    
    def update_array_spaces(self, matriz):
        print(f"\nCampo de batalha Jogador: {self.name_player}")
        self.__model_matriz.update_array_spaces(matriz)
    
    def informs_the_type_of_ship(self):
        try:
            ship_type = int(input("Informe o tipo de navio: "))
        except ValueError:
            return self.informs_the_type_of_ship()
        return ship_type
        
    def informs_the_coordinate(self):
        print(f"\nPlayer{self.number}: {self.name_player}")
        while True:
            try:
                coordinate = input("Informe a Coordenada: ").upper()
                if len(coordinate) == 2:
                    if coordinate[0] in 'ABCDEFGHIJ' and coordinate[1] in '0123456789':
                            return coordinate  
            except:
                pass 
            else:
                print("Coordenada Incorreta! Tente novamente!")
