from sqlalchemy.orm import Session

from models.Dominios import Dominios


class DominiosDAO:
    def __init__(self, session: Session):
        self.session = session

    def getAllDomains(self):
        conjuntoDominios = self.session.query(Dominios).all()
        # Recomendación: no devolver un objeto de Model, debemos devolver un objeto de proyecto
        # Es decir, en lugar de pasar un model pasamos un DTO
        return conjuntoDominios