class ControllerView:
    def __init__(self):
        pass

    def final_result(self, name, sum_result):
        if sum_result > 21:
            print(f"O Player {name} perdeu a partida!")
        elif sum_result == 21:
            print(f"O Player {name} venceu a partida!")
        else:
            print(f"O Player {name} continua no jogo!")
            
    def remove_winning_players(self, list_result_players):
        list_winning_players = []
        for player in list_result_players:
            if player[1] == 21:
                list_winning_players.append(player)
        return list_winning_players
                
    def remove_losing_players(self, list_result_players):
        list_losing_players = []
        for player in list_result_players:
            if player[1] > 21:
                list_losing_players.append(player)
        return list_losing_players
    
    def remove_players_finally(self, list_players, list_losing_player, list_winning_players):
        for player_losing in list_losing_player:
            for player in list_players:
                if player_losing[0] == player.name:
                    list_players.remove(player)
        for player_winning in list_winning_players:
            for player in list_players:
                if player_winning[0] == player.name:
                    list_players.remove(player)
        return list_players
    
    def check_last_player(self, list_players, list_winning_players):
        if len(list_players) == 1:
            for player in list_players:
                list_winning_players.append([player.name, player.sum_result])
                list_players.remove(player)
