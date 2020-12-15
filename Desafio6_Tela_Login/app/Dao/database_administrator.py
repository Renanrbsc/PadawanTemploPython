from Desafio6_Tela_Login.app.Dao.database import BaseDao
from Desafio6_Tela_Login.app.Model.model_login import AdministratorModel


class AdministratorDao(BaseDao):
    def __init__(self):
        # -- string format(SGBD+conector://user:passwd@url:port/database)
        conection = "mysql+mysqlconnector://root@127.0.0.1:3306/PAD1578"
        super().__init__('ADMINISTRATOR', conection)

    def get_all(self):
        return super().get(AdministratorModel)

    def get_by_id(self, id):
        return super().get(AdministratorModel,id)

    def insert(self, administrator: AdministratorModel) -> str:
        return super().insert(administrator)

    def update(self, id, administrator: AdministratorModel):
        administrator.id = id
        return super().update(administrator)

    def remove(self, id):
        return super().remove(AdministratorModel, id)