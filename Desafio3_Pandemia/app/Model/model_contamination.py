from Desafio3_Pandemia.app.Model.model_function import BaseFunction


class Contamination(BaseFunction):
    def __init__(self):
        self._list_new_map = []
        self.new_map = ''
        self.number_infected = 0

    def set_infection_in_map(self, infection: dict) -> None:
        self.infection = infection["definition_map"]

    def set_not_infection_in_map(self, map_desc: dict) -> None:
        self.not_infected = map_desc["defin. não infectado"]

    def set_ocean_in_map(self, map_desc: dict) -> None:
        self.ocean = map_desc["defin. oceano"]

    def get_number_infected(self) -> int:
        return self.number_infected

    def insert_infected_in_the_map(self, map_desc: dict, infection: dict) -> dict:
        """ Individuos da população inicial tem uma 
            probabilidade de 10% de serem vulneraveis ao contagio """
        rate = 10
        for index in map_desc["mapa"]:
            if index == self.not_infected:
                if super().create_percentage() <= rate:
                    self.new_map += self.infection
                else:
                    self.new_map += self.not_infected
            elif index == self.ocean:
                self.new_map += self.ocean
        map_desc["mapa"] = self.new_map
        return map_desc

    def replicate_maps_for_contamination(self, map_desc: dict) -> tuple:
        list_new_map = []
        list_global_map = map_desc["mapa"].split('X')
        return list_global_map, list_new_map

    def population_likely_to_be_contaminated(self, global_map: list) -> int:
        population = 0
        for index in global_map:
            if self.infection in index:
                population += len(index)
        return population

    def search_people_in_map(self, country: str) -> bool:
        if self.infection or self.not_infected in country:
            return True
        return False

    def looking_for_contamination(self, country: str) -> bool:
        self.number_infected = country.count('1')
        if self.number_infected >= 1:
            return True
        return False

    def is_not_full_of_contamination(self, country: str) -> bool:
        if self.number_infected < len(country):
            return True
        return False

    def generate_predict_value(self, infection: dict) -> int:
        predict_number = super().exponential_contamination(self.number_infected, infection['contamination'])
        self.number_infected += predict_number
        return self.number_infected
        
    def generate_contamination(self, country: str, new_map: list) -> list:
        self.new_country = ''
        for number_infected, index_people in enumerate(country):
            if number_infected < self.number_infected:
                self.new_country += self.infection
            else:
                self.new_country += self.not_infected
        new_map.append(self.new_country)
        return new_map

    def put_a_country_without_contamination(self, new_map:list, country: str) -> list:
        new_map.append(country)
        return new_map
   
    def put_an_ocean_on_the_new_map(self, new_map: list, map_desc: dict) -> list:
        new_map.append(self.ocean)
        return new_map

    def mounting_map_with_the_infection(self, list_new_map: list, new_map_desc: dict) -> dict:
        new_map = ''
        if list_new_map[-1] == self.ocean:
            list_new_map.pop(-1)
        for index_list in list_new_map:
            new_map += index_list
        new_map_desc["mapa"] = new_map
        return new_map_desc

    def percentage_of_infected_population(self, global_map: dict) -> tuple:
        self._infected_population = global_map["mapa"].count('1')
        self._population = global_map["mapa"].count('0') + self._infected_population
        self._percentage_infected = 100 * (self._infected_population/self._population)
        return self._population, self._infected_population, self._percentage_infected

       