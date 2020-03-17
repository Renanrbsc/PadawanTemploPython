class BatalhaNaval:
    def __init__(self):
        pass
    
    def create_matriz(self):
        list_bidimension = []
        
        column = ['A','B','C','D','E','F','G','H','I','J']
        for index_column in column:    
            list_unidimension = []
            for index_row in range(10):
                coordinate = {f'{index_column}{index_row}':{"Empty":""}}
                list_unidimension.append(coordinate)
            list_bidimension.append(list_unidimension)
            
        for i in list_bidimension:
            print(i)
   
    def ship_definitions_for_the_game(self):
        """Cada jogador deverá colocar 7 unidades de batalha,
           cada uma ocupando uma determinada quantidade de espaços no tabuleiro.
           As unidades são as seguintes:
        1 Porta Aviões (1x5)        1 Encouraçado (1x4)        1 Cruzador (1x3)
        2 Destroyer (1x2)        2 Submarinos (1x1)"""
        list_of_ships = [{"aircraft_carrier":"Porta-Aviões", "amount":1, "spaces_on_the_board":[1,5]},
                         {"battleship":"Encouraçado", "amount":1, "spaces_on_the_board":[1,4]},
                         {"cruiser_ship":"Cruzador", "amount":1, "spaces_on_the_board":[1,3]},
                         {"destroyer_ship":"Destroyer", "amount":2, "spaces_on_the_board":[1,2]},
                         {"submarine":"Submarino", "amount":2, "spaces_on_the_board":[1,1]}
                         ]
        

game = BatalhaNaval()
game.create_matriz()