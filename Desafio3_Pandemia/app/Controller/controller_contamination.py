from Desafio3_Pandemia.app.Model.model_function import BaseFunction
from Desafio3_Pandemia.app.Model.model_contamination import Contamination
from Desafio3_Pandemia.app.Model.model_map import Map
from Desafio3_Pandemia.app.Views.view_terminal import Terminal


class CtrlContamination:
    def __init__(self):
        self._view = Terminal()
        self._function = BaseFunction()
        self._model = Contamination()
        self._model_map = Map()

    def create_infection_in_map(self, map_desc: dict, infection: dict) -> dict:
        self._function.waiting_time_to_proceed(0.05)
        self._model.set_infection_in_map(infection)
        self._model.set_not_infection_in_map(map_desc)
        self._model.set_ocean_in_map(map_desc)
        new_map_desc = self._model.insert_infected_in_the_map(map_desc, infection)
        self._model_map.generate_map_description_data(new_map_desc)
        self._view.update_description_map(self._model_map)

        return new_map_desc

    def create_cycles_contamination(self, infection: dict, map_desc: dict, cycles: int) -> dict:
        self._function.waiting_time_to_proceed(0.15)
        old_map, new_map = self._model.replicate_maps_for_contamination(map_desc)
        self.population_at_risk = self._model.population_likely_to_be_contaminated(old_map)
        for index_country, country in enumerate(old_map):
            if self._model.search_people_in_map(country):
                if self._model.looking_for_contamination(country) \
                        and self._model.is_not_full_of_contamination(country):
                    number_infected = self._model.get_number_infected()
                    self._view.define_current_progress(index_country, cycles, number_infected)
                    number_infected = self._model.generate_predict_value(infection)
                    new_map = self._model.generate_contamination(country, new_map)
                    self._view.define_final_progress(index_country, number_infected)
                else:
                    new_map = self._model.put_a_country_without_contamination(new_map, country)
            new_map = self._model.put_an_ocean_on_the_new_map(new_map, map_desc)

        self._function.waiting_time_to_proceed(0.05)
        new_map_desc = self._model.mounting_map_with_the_infection(new_map, map_desc)
        self._model_map.generate_map_description_data(new_map_desc)
        self._view.update_description_map(self._model_map)

        self._function.waiting_time_to_proceed(0.05)
        population, self.infected, percent = self._model.percentage_of_infected_population(new_map_desc)
        self._view.define_percent(population, self.infected, percent)

        return new_map_desc

    def in_the_population_is_complete(self) -> bool:
        if self.infected >= self.population_at_risk:
            self._function.waiting_time_to_proceed(0.05)
            self._view.ending_pandemic_simulation()
            return True
        return False
