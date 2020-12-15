from Desafio3_Pandemia.app.Controller.controller_map import CtrlMap
from Desafio3_Pandemia.app.Controller.controller_infection import CtrlInfection
from Desafio3_Pandemia.app.Controller.controller_contamination import CtrlContamination


class Startup:
    def __init__(self):
        self._controller_map = CtrlMap()
        self._controller_infection = CtrlInfection()
        self._controller_contamination = CtrlContamination()

    def execute(self) -> None:
        global_map_desc = self._controller_map.create_map()
        infection = self._controller_infection.create_infection()
        new_map_desc = self._controller_contamination.create_infection_in_map(global_map_desc,
                                                                              infection)
        for cycles in range(10):
            new_map_desc = self._controller_contamination.create_cycles_contamination(infection,
                                                                                      new_map_desc, cycles)
            if self._controller_contamination.in_the_population_is_complete():
                return
