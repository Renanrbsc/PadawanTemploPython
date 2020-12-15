
class Terminal:
    def __init__(self):
        pass

    def define_map_name(self) -> str:
        print("\n------ Definir Mundo ----------------------------------")
        name = input("Escolha um nome para seu Mapa: ")
        return f"Map {name}"

    def define_map_size(self, name_map: str) -> int:
        print("\n------ Definir Dimensão -------------------------------")
        try:
            size = int(input(f"Informe o tamanho de {name_map}: "))
        except ValueError or TypeError:
            print("Invalid value or not an integer, Try again!")
            print("Valor invalido ou não é um número inteiro, Tente novamente!")
            return self.define_map_size(name_map)
        else:
            return size

    def define_map_description(self, map_description: dict) -> None:
        print(f"\n------ Definições Mapa -------------------------------\n")
        print(f"Nome definido: {map_description['nome definido']}\n")
        print(f"Tamanho: {map_description['tamanho']}\n")
        print(f"Continentes: {map_description['continentes']}\n")
        print(f"População: {map_description['população']} pessoas")

    def define_infection(self) -> tuple:
        print("\n------ Definir Agente Etiológico ---------------------- ")
        organism_name = input("Informe o nome do agente infeccioso: ")

        print("\n------ Definir Doença transmitida --------------------- ")
        organism_disease = input("Informe o nome da Doença: ")

        print("\n------ Definir Geração -------------------------------- ")
        organism_mutation = input("Informe o organismo que obteve Mutação: ")

        return organism_name, organism_disease, organism_mutation
    
    def define_infection_description(self, name: str, disease: str, organism: str) -> None:
        print(f"\nSua Pandemia será gerada pelo Agente Etiológico: {name}")
        print(f"\nCausadora da doença: {disease}")
        print(f"\nDesenvolvida atrávez da mutação do microorganismo: {organism}")

    def define_contamination_level(self, contamination_rate: int) -> None:
        print("\n------ Nivel de Contaminação --------------------------")
        if contamination_rate == 100:
            print("Taxa de crescimento: Exponencial Descontrolada")
        print(f"Nivel de transmissão: {contamination_rate}%")
    
    def define_simulation_of_dissemination_cycles(self, transmitters: list) -> None:
        print("\n------ Simulação ---------------------------------------")
        for index, value in enumerate(transmitters):
            print(f"Ciclo{index+1}: {value} casos")

    def define_generated_infection_data(self, infection: dict) -> None:
        print(f"\n------ Desenvolvimento e Simulação concluido ----------")
        print(f"Dados gerados: ")
        for key in infection:
            print(f"     {key.capitalize()}: {infection[key]}")
        print(f"Enviando ao Mapa...")

    def update_description_map(self, model_map) -> None:
        print(model_map)

    def define_current_progress(self, country: int, cycles: int, number_infected: int) -> None:        
        print(f'\n------ Progresso da Infecção -> Ciclo {cycles+1} ------ ')
        print(f'N° Inicial infectados no continente {country+1}: {number_infected} casos')

    def define_final_progress(self, country, number_infected: int) -> None:
        print(f'N° Final infectados no continente {country+1}: {number_infected} casos\n')

    def define_percent(self, population: int, infected: int, percentage: int) -> None:
        print(f"\n------ Estatisticas -----------------------------------")
        print(f"População Total: {population}")
        print(f"População Infectada: {infected}")
        print(f"Porcentagem da população infectada: {percentage:.2f}%")
        
    def ending_pandemic_simulation(self) -> None:
        print(f"\n------ Finalização -----------------------------------")
        print(f"\nA contaminação foi concluida com sucesso!")
        print(f"Finalizando Simulação...")