from Desafio3_Pandemia.app.Model.model_function import BaseFunction


class Infection(BaseFunction):
    def __init__(self):
        self.infection = {}
        self.data_cases_simulation = []

    def organism_name(self, name: str) -> None:
        self._organism_name = name

    def organism_disease(self, organism_disease: str) -> None:
        self._organism_disease = organism_disease

    def organism_mutation(self, organism_mutation: str) -> None:
        self._organism_mutation = organism_mutation

    def generate_contagion_level(self) -> int:
        self._contagion_level = super().create_percentage()
        return self._contagion_level

    def simulation_of_dissemination_cycles(self) -> list:
        """ Simulação de 10 ciclos de contaminação """
        transmitter = 1
        for round in range(10):
            self.data_cases_simulation.append(transmitter)
            transmitter += super().exponential_contamination(transmitter, self._contagion_level)
        return self.data_cases_simulation
        
    def generate_infection_data(self) -> dict:
        self.infection = {"name": self._organism_name,
                          "disease": self._organism_disease,
                          "contamination": self._contagion_level,
                          "mutation_of": self._organism_mutation,
                          "definition_map": '1'}
        return self.infection
