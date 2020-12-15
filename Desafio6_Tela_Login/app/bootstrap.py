from Desafio6_Tela_Login.app.Views.terminal_view import AdministratorView
from Desafio6_Tela_Login.app.Views.web_login import WebView


class Startup:
    def __init__(self):
        self.terminal = AdministratorView()
        self.web = WebView()
        self.option = 0

    def initial_menu(self):
        print(f"1 - Menu Terminal\n" \
              f"2 - Menu WEB")
        self.option = int(input("Selecione a forma de menu: "))

    def sub_menu(self):
        if self.option == 1:
            while True:
                self.terminal.authentication()
                self.terminal.conditions()
        elif self.option == 2:
            self.web.run_flask()
