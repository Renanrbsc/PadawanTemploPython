from Desafio3_Pandemia.app.Model.model_function import BaseFunction
from Desafio3_Pandemia.app.Model.model_infection import Infection
from Desafio3_Pandemia.app.Views.view_terminal import Terminal


class CtrlInfection:
    def __init__(self):
        self._function = BaseFunction()
        self._view = Terminal()
        self._model = Infection()

    def create_infection(self) -> dict:
        self._function.waiting_time_to_proceed(0.05)
        organism_name, organism_disease, organism_mutation = self._view.define_infection()
        self._model.organism_name(organism_name)
        self._model.organism_disease(organism_disease)
        self._model.organism_mutation(organism_mutation)

        self._function.waiting_time_to_proceed(0.05)
        self._view.define_infection_description(organism_name, organism_disease, organism_mutation)

        self._function.waiting_time_to_proceed(0.05)
        contagion_level = self._model.generate_contagion_level()
        self._view.define_contamination_level(contagion_level)

        self._function.waiting_time_to_proceed(0.05)
        data_cases_simulation = self._model.simulation_of_dissemination_cycles()
        self._view.define_simulation_of_dissemination_cycles(data_cases_simulation)

        self._function.waiting_time_to_proceed(0.05)
        infection = self._model.generate_infection_data()
        self._view.define_generated_infection_data(infection)

        return infection
