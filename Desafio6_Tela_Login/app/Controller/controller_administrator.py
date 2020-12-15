from Desafio6_Tela_Login.app.Dao.database_administrator import AdministratorDao


class AdministratorController:
    def __init__(self):
        self.dao = AdministratorDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.get_all()

    def post(self, Model):
        return self.dao.insert(Model)

    def put(self, id, Model):
        return self.dao.update(id, Model)

    def delete(self, id):
        return self.dao.remove(id)


