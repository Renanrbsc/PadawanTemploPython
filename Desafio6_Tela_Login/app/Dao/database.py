import sqlalchemy as db
from sqlalchemy.orm.session import sessionmaker


class BaseDao:
    def __init__(self, table: str, conection: str):
        self.table = table
        configuration = db.create_engine(conection)
        session_creator = sessionmaker()
        session_creator.configure(bind=configuration)
        self.session = session_creator()

    def get(self, model: object, id=None)-> list:
        if id:
            return self.session.query(model).filter(model.id == id).one()
        return self.session.query(model).all()

    def insert(self, model: object) -> str:
        self.session.add(model)
        self.session.commit()
        return f'Objeto de id {model.id} inserido com sucesso!'

    def update(self, model: object) -> str:
        self.session.merge(model)
        self.session.commit()
        return f'Objeto de id {model.id} alterado com sucesso!'

    def remove(self, model: object, id: int) -> str:
        self.session.delete(self.get(model, id))
        self.session.commit()
        return f'Objeto de id {id} deletado com sucesso!'
