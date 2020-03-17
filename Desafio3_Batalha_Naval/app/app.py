class BatalhaNaval:
    def __init__(self):
        self.list_bidimension = None
        self.list_of_ships = None

    @property
    def list_bidimension(self):
        return self._list_bidimension

    @list_bidimension.setter
    def list_bidimension(self, list_bidimension):  
        if list_bidimension is list:
            pass
        else:
            self._list_bidimension = []

    @property
    def list_of_ships(self):
        return self._list_of_ships

    @list_of_ships.setter
    def list_of_ships(self, list_of_ships):
        self._list_of_ships = list_of_ships

    def create_matriz(self):
        """ coordenada  0 = nao tem navio
                        1 = tem navio"""
        column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        for index_column in column:
            list_unidimension = []
            for index_row in range(10):
                coordinate = {"CR":f'{index_column}{index_row}', "Space": 0}
                list_unidimension.append(coordinate)
            self._list_bidimension.append(list_unidimension)
        self.print_coordenadas_completas()
        
    def print_coordenadas_completas(self):
        for i in self.list_bidimension:
            print(i)
        
    def ship_definitions_for_the_game(self):
        """Cada jogador deverá colocar 7 unidades de batalha,
           cada uma ocupando uma determinada quantidade de espaços no tabuleiro.
           As unidades são as seguintes:
        1 Porta Aviões (1x5)        1 Encouraçado (1x4)        1 Cruzador (1x3)
        2 Destroyer (1x2)        2 Submarinos (1x1)"""
        self._list_of_ships = [{"aircraft_carrier": "Porta-Aviões", "amount": 1, "spaces_on_the_board": [1, 5]},
                               {"battleship": "Encouraçado", "amount": 1, "spaces_on_the_board": [1, 4]},
                               {"cruiser_ship": "Cruzador", "amount": 1, "spaces_on_the_board": [1, 3]},
                               {"destroyer_ship": "Destroyer", "amount": 2, "spaces_on_the_board": [1, 2]},
                               {"submarine": "Submarino", "amount": 2, "spaces_on_the_board": [1, 1]}
                               ]

    def informa_a_coordenada_para_navio(self):
        coordenada = input("Informe a Coordenada: ").upper()
        return coordenada
    
    def coloca_navios_no_tabuleiro(self, coordenada):
        list_rows = []
        for index_row in self._list_bidimension:
            list_column = []
            for index_column in index_row:
                if coordenada in index_column["CR"]:
                    index_column['Space'] = 1
                list_column.append(index_column['Space'])
            list_rows.append(list_column)
        
        for row in list_rows:
            print(row)
                
            
            # for ship in self.list_of_ships:
            #     print(ship)


game = BatalhaNaval()
game.create_matriz()
# game.list_bidimension = ['aaa'] excessao que causa erro apenas na segundo round
game.ship_definitions_for_the_game()
coordenada = game.informa_a_coordenada_para_navio()
game.coloca_navios_no_tabuleiro(coordenada)
