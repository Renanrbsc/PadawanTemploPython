from Desafio4_Batalha_Naval.Model.model_player import ModelPlayer
from Desafio4_Batalha_Naval.Model.model_matriz import ModelMatriz
from Desafio4_Batalha_Naval.Controller.controller_rules_ships import ControllerRulesShips
from Desafio4_Batalha_Naval.Controller.controller_rules_battle import ControllerRulesBattle


class BatalhaNaval:
    def __init__(self, number_player):
        self._model_player = ModelPlayer(number_player)
        self._model_matriz = ModelMatriz()
        self._controller_rules_ships = ControllerRulesShips()
        self._controller_rules_battle = ControllerRulesBattle()
    
    def main_initialize_game(self):
        self._main_matriz = self._model_player.create_matriz()
        self._controller_rules_ships.ship_definitions_for_the_game()
        
    def main_initialize_ships_in_field(self):
        while True:
            print(self._controller_rules_ships.model_ship)
            coordinate = self._model_player.informs_the_coordinate()
            type_ship = self._model_player.informs_the_type_of_ship()
            self._controller_rules_ships.reduces_the_number_of_ships(coordinate, type_ship,
                                                                      self._model_player, self._main_matriz)

            if self._controller_rules_ships.amount_ships_from_battle_start() <= 0:
                print(f"Fim da rodada de colocação {self._model_player.name_player}!")
                return self._main_matriz, self._model_player
    
    def receives_data_from_the_enemy(self, main_player_enemy):
        self._controller_rules_battle.receives_data_from_the_enemy(main_player_enemy)
    
    def main_initialize_naval_battle(self):
            coordinate = self._model_player.informs_the_coordinate()
            self._controller_rules_battle.check_the_board_if_there_is_a_ship(coordinate)
            
    def amount_parts_ships_in_battle(self):
        if self._controller_rules_battle.amount_parts_ships_in_battle():
            print(f"Vendedor da batalha: {self._model_player.name_player}")
            return True
        return False
    
        
player_one = BatalhaNaval(1)
player_two = BatalhaNaval(2)

while True:
    player_one.main_initialize_game()
    player_two.main_initialize_game()
    main_player_one = player_one.main_initialize_ships_in_field()
    main_player_two = player_two.main_initialize_ships_in_field()
    player_one.receives_data_from_the_enemy(main_player_two)
    player_two.receives_data_from_the_enemy(main_player_one)
    while True:
        player_one.main_initialize_naval_battle()
        player_two.main_initialize_naval_battle()
        if player_one.amount_parts_ships_in_battle() or player_two.amount_parts_ships_in_battle():
            break
    break
