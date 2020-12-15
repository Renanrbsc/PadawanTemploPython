from flask import Flask, render_template, request, redirect

from Desafio6_Tela_Login.app.Controller.controller_administrator import AdministratorController


class WebView:
    def __init__(self):    
        self.login = []
        
    def run_flask(self):
        app = Flask(__name__)

        @app.route('/')
        def index():
            return render_template('index.html')

        @app.route('/login')
        def login_admin():
            Admin_controller = AdministratorController()
            admin_all = Admin_controller.get()
            username = request.args['username']
            passwd = request.args['password']

            for admin in admin_all:
                if str(username).lower() == str(admin.username).lower() \
                        or str(username).lower() == str(admin.email).lower():
                    if passwd == str(admin.password).lower():
                        self.login.append(username)
                        self.login.append(passwd)
                        return render_template('menu.html')
            return render_template('login.html')

        @app.route('/menu')
        def menu_admin():
            if self.login:
                return render_template('menu.html')
            else:
                return render_template('login.html')

        @app.route('/sair')
        def sair_admin():
            # busca a variavel global para modificar
            self.login.clear()
            return redirect('/')

        app.run(debug=True, port=80)
