from Desafio3_Pandemia.app.Model.model_function import BaseFunction
from Desafio3_Pandemia.app.Model.model_map import Map
from Desafio3_Pandemia.app.Views.view_terminal import Terminal


class CtrlMap:
    def __init__(self):
        self._function = BaseFunction()
        self._model = Map()
        self._view = Terminal()

    def create_map(self) -> dict:
        self._function.waiting_time_to_proceed(0.05)
        map_name = self._view.define_map_name()
        size = self._view.define_map_size(map_name)
        self._model.set_map_name(map_name)
        self._model.set_map_size(size)
        
        self._function.waiting_time_to_proceed(0.05)
        self._model.create_random_map()
        self._model.create_continents_data_on_the_map()
        self._model.generate_map_description_data()
        map_description = self._model.get_map_description()
        self._view.define_map_description(map_description)

        self._function.waiting_time_to_proceed(0.05)
        self._view.update_description_map(self._model)

        return map_description



