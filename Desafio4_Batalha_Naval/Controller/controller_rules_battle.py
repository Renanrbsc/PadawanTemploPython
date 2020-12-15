from Desafio4_Batalha_Naval.Model.model_matriz import ModelMatriz


class ControllerRulesBattle:
    def __init__(self, ):
        self._sum_amount_ships = 0
        self._model_matriz = ModelMatriz()

    def receives_data_from_the_enemy(self, main_player_enemy):
        self._main_matriz_enemy = main_player_enemy[0]
        self._model_player_enemy = main_player_enemy[1]

    def receive_coordinate_and_check_in_the_board(self, space, coordinate):
        if coordinate == space['CR']:
            return True
        return False

    def check_the_board_if_there_is_a_ship(self, coordinate):
        for index_row in self._main_matriz_enemy:
            for index_colunm in index_row:
                if self.receive_coordinate_and_check_in_the_board(index_colunm, coordinate):
                    if index_colunm['Space'] != 0 and index_colunm['Space'] != 'X':
                        print(f"voce acertou um navio de {self._model_player_enemy.name_player}!")
                        index_colunm['Space'] = 'X'
                        self._sum_amount_ships += 1
                        self._model_matriz.update_array_spaces(self._main_matriz_enemy)
                    else:
                        print("Voçê errou o navio! Espere a proxima vez!")
                        index_colunm['Space'] = 'X'
                        self._model_matriz.update_array_spaces(self._main_matriz_enemy)

    def amount_parts_ships_in_battle(self):
        if self._sum_amount_ships >= 18:
            return True
        return False
