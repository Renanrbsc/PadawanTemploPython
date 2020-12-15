class ModelShip:
    def __init__(self):
        self.list_of_ships = None
        self.spaces_on_the_board = None

    @property
    def list_of_ships(self):
        return self._list_of_ships

    @list_of_ships.setter
    def list_of_ships(self, list_of_ships):
        self._list_of_ships = list_of_ships

    @property
    def spaces_on_the_board(self):
        return self._spaces_on_the_board

    @spaces_on_the_board.setter
    def spaces_on_the_board(self, spaces_on_the_board):
        self._spaces_on_the_board = spaces_on_the_board

    def ship_definitions_for_the_game(self):
        self._list_of_ships = [{"type": 1, "name": "Porta-Aviões", "amount": 1, "spaces_on_the_board": [1, 5]},
                               {"type": 2, "name": "Encouraçado", "amount": 1, "spaces_on_the_board": [1, 4]},
                               {"type": 3, "name": "Cruzador", "amount": 1, "spaces_on_the_board": [1, 3]},
                               {"type": 4, "name": "Destroyer", "amount": 2, "spaces_on_the_board": [1, 2]},
                               {"type": 5, "name": "Submarino", "amount": 2, "spaces_on_the_board": [1, 1]}]

        self._spaces_on_the_board = [{"type": 1, "spaces_on_the_board": 5},
                                     {"type": 2, "spaces_on_the_board": 4},
                                     {"type": 3, "spaces_on_the_board": 3},
                                     {"type": 4, "spaces_on_the_board": 2},
                                     {"type": 5, "spaces_on_the_board": 1}]

    def __str__(self):
        ships = ''
        for i in self.list_of_ships:
            ships += i['name'] + ' Quantidade:  ' + str(i['amount']) + ' | '

        return f"Navios: {ships}"
