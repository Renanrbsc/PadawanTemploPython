from Desafio6_Tela_Login.app.Controller.controller_administrator import AdministratorController
from Desafio6_Tela_Login.app.Model.model_login import AdministratorModel


class AdministratorView:
    def __init__(self):
        self.controller = AdministratorController()
        self.model = None
        self.login = None
        self.psswd = None
        self.op = None
        self.id = None
        self.table = ''

    def authentication(self):
        admin_all = self.controller.get()
        for admin in admin_all:
            if str(self.login).lower() == str(admin.username).lower()\
                    or str(self.login).lower() == str(admin.email).lower():
                if self.psswd == str(admin.password).lower():
                    return self.menu()
        print('-=' * 20, '\nLogin Administrador')
        self.login = input("Insira seu username ou email: ")
        self.psswd = input("Informe sua senha: ")
        return self.authentication()

    def menu(self):
        print('-=' * 20,'\n-- MENU ADMINISTRADOR --\n', '-=' * 20)
        self.table = 'Administrador'

        print(f'1 - Listar {self.table}')
        print(f'2 - Buscar {self.table} ID')
        print(f'3 - Inserir {self.table}')
        print(f'4 - Alterar {self.table}')
        print(f'5 - Deletar {self.table}')
        print('-=' * 20)
        self.op = int(input("Digite a opcao: "))
        print('-=' * 20)

    def parameters(self):
        if self.op == 2 or self.op == 4 or self.op == 5:
            self.id = int(input(f"Digite a id do {self.table}:"))
        if self.op == 3 or self.op == 4:
            self.model = AdministratorModel()
        return self.model

    def conditions(self):
        if self.op == 1:
            model_all = self.controller.get()
            for model in model_all:
                print(model)

        if self.op == 2:
            print(f'----Buscar ID {self.table}----')
            self.parameters()
            print(self.controller.get(self.id))

        if self.op == 3:
            print(f'----Adicionar {self.table}----')
            model = self.parameters()
            print(self.controller.post(model))

        if self.op == 4:
            print(f'----Alterar {self.table}----')
            model = self.parameters()
            print(self.controller.put(self.id, model))

        if self.op == 5:
            print(f'----Remover {self.table}----')
            self.parameters()
            print(self.controller.delete(self.id))

