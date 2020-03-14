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