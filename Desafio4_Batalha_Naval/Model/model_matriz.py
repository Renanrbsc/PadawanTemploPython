class ModelMatriz:
    def __init__(self):
        self._index_rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.updated_matriz = []
        self.list_bidimension = None

    @property
    def list_bidimension(self):
        return self._list_bidimension

    @list_bidimension.setter
    def list_bidimension(self, list_bidimension):
        if not list_bidimension is list:
            self._list_bidimension = []

    def create_matriz(self) -> list:
        """ ['CR'] = column and row
        coordenada  0 = nao tem navio
                    1 = tem navio"""
        for index_row in self._index_rows:
            list_unidimension = []
            for index_column in range(10):
                coordinate = {"CR": f'{index_row}{index_column}', "Space": 0}
                list_unidimension.append(coordinate)
            self._list_bidimension.append(list_unidimension)
        return self._list_bidimension

    def update_array_spaces(self, matriz: list):
        self.updated_matriz.clear()
        for index_row in matriz:
            list_column = []
            for index_column in index_row:
                list_column.append(index_column['Space'])
            self.updated_matriz.append(list_column)
        print(self.__str__())

    def __str__(self) -> str:
        print(f"     0  1  2  3  4  5  6  7  8  9")
        for index, row in enumerate(self.updated_matriz):
            battle_camp = ' '
            for index_row in row:
                if index_row == 0:
                    battle_camp += '░  '
                elif index_row == 1:
                    battle_camp += '✈  '
                elif index_row == 2:
                    battle_camp += '✪  '
                elif index_row == 3:
                    battle_camp += '✠  '
                elif index_row == 4:
                    battle_camp += '▽  '
                elif index_row == 5:
                    battle_camp += '◎  '
                elif index_row == 'X':
                    battle_camp += '✐  '

            print(f"{self._index_rows[index]} - {battle_camp}")
        return 'Matriz Atualizada!'
