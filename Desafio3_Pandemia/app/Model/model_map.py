from Desafio3_Pandemia.app.Model.model_function import BaseFunction


class Map(BaseFunction):
    def __init__(self):
        self._map_name = ''
        self._size = 0
        self._global_map = ''
        self._ocean = 'X'
        self._not_infected = '0'
        self._number_country = 0
        self._population = 0
        self._map_description = {}

    def get_global_map(self) -> str:
        return self._global_map

    def get_map_name(self) -> str:
        return self._map_name

    def get_map_size(self) -> int:
        return self._size

    def get_population(self) -> int:
        return self._population

    def get_number_country(self) -> int:
        return self._number_country

    def get_map_description(self) -> dict:
        return self._map_description

    def set_map_name(self, name_map: str) -> None:
        self._map_name = str(name_map)

    def set_map_size(self, size: int) -> None:
        self._size = int(size)

    def set_global_map(self, global_map: str) -> None:
        self._global_map = global_map

    def set_map_description(self, map_description: dict) -> None:
        self._map_description = map_description

    def create_random_map(self) -> None:
        """ Cria mapa randomico por porcentagem,
            90% chance = Nao infectado
            10% chance = Oceano """
        global_map = ''
        for part in range(self._size):
            percentage = super().create_percentage()
            if percentage <= 90:
                part_of_the_map = self._not_infected
            else:
                part_of_the_map = self._ocean
            global_map += part_of_the_map
        self.set_global_map(global_map)

    def create_continents_data_on_the_map(self) -> None:
        list_map = self._global_map.split('X')
        for country in list_map:
            if len(country) >= 1:
                self._number_country += 1
        self._population = self._global_map.count('0')

    def generate_map_description_data(self, map_description: dict = None) -> dict:
        if not map_description:
            map_description = {"nome definido": self._map_name,
                                    "tamanho": self._size,
                                    "continentes": self._number_country,
                                    "população": self._population,
                                    "mapa": self._global_map,
                                    "defin. oceano": self._ocean,
                                    "defin. não infectado": self._not_infected}
        self.set_map_description(map_description)

    def __str__(self) -> str:
        string = f"\n------ Mapa Atualizado -------------------------------\n"
        for key in self._map_description:
            string += f"{key.capitalize()}: {self._map_description[key]}\n"
        return string + f"Enviando ao Mapa..."
