from Desafio4_Batalha_Naval.Model.model_ship import ModelShip


class ControllerRulesShips:
    def __init__(self):
        self.model_ship = ModelShip()
        
    def ship_definitions_for_the_game(self):    
        self.model_ship.ship_definitions_for_the_game()
        
    def checks_ship_type_exists_in_the_list(self,ship_type, ship_type_list):
        if ship_type == ship_type_list:
            return True
        return False
        
    def checks_number_of_ships_ran_out(self, amount_ship):
        if amount_ship <= 0:
            return True
        return False
    
    def checks_ship_in_the_matrix_space(self, coordinate, matriz):
        for index_row in matriz:
            for index_column in index_row:
                if coordinate in index_column["CR"] and index_column['Space'] == 0:
                    return True
        return False
    
    def checks_for_parts_of_the_ship(self, spaces_on_the_board):
        if spaces_on_the_board >= 0:
            return True
        return False
        
    def put_ship_reference_in_the_matrix(self, coordinate, ship_type, player_matriz, matriz):
        for index_row in matriz:
            for index_column in index_row:
                if coordinate in index_column["CR"]:
                    index_column['Space'] = ship_type

        player_matriz.update_array_spaces(matriz)
               
    def checks_the_space_on_the_board_is_zero(self, space_on_the_board):
        if space_on_the_board == 0:
            return True
        return False
    
    def checks_amount_ship_is_greater_than_zero(self, amount_ship):
        if amount_ship > 0:
            return True
        return False
    
    def reduces_the_number_of_ships(self, coordinate, ship_type, player_matriz, matriz):
        for ship in self.model_ship.list_of_ships:                
            if self.checks_ship_type_exists_in_the_list(ship_type, ship['type']):
                if self.checks_number_of_ships_ran_out(ship['amount']):     
                    print(f"\nNavio escolhido: {ship['name']}")          
                    print(f"Quantidade de navios: {ship['amount']}")
                    print(f"Quantidade de partes de cada {ship['name']}: {ship['spaces_on_the_board'][1]}")
                else:
                    print(f"\nNavio escolhido: {ship['name']}")          
                    print(f"Quantidade de navios: {ship['amount']}")
                    print(f"Quantidade de partes do {ship['name']} Atuais: {ship['spaces_on_the_board'][1]}")
                    if self.checks_ship_in_the_matrix_space(coordinate, matriz):
                        ship['spaces_on_the_board'][1] -= 1
                        if self.checks_for_parts_of_the_ship(ship['spaces_on_the_board'][1]):
                            self.put_ship_reference_in_the_matrix(coordinate, ship_type, player_matriz, matriz)
                        print(f"Quantidade de partes do {ship['name']} restante: {ship['spaces_on_the_board'][1]}")
                        if self.checks_the_space_on_the_board_is_zero(ship['spaces_on_the_board'][1]):
                            ship['amount'] -= 1
                            print(f"Quantidade de navios {ship['name']} restante: {ship['amount']}")
                            if self.checks_amount_ship_is_greater_than_zero(ship['amount']):
                                for space in self.model_ship.spaces_on_the_board:
                                    if self.checks_ship_type_exists_in_the_list(ship_type, space['type']):      
                                        ship['spaces_on_the_board'][1] = space['spaces_on_the_board']

    def amount_ships_from_battle_start(self):
        sum_amount_ships = 0
        for ship in self.model_ship.list_of_ships:
            sum_amount_ships += ship['amount']
        return sum_amount_ships
