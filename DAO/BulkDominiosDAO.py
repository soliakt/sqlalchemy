from sqlalchemy.orm import Session
from typing import List

from DTO.BulkDominiosDTO import BulkDominiosDTO
from models.BulkDominios import BulkDominios


class BulkDominiosDAO:
    def __init__(self, session: Session):
        self.session = session

    def getAllBulkDomains(self) -> List[BulkDominiosDTO]:
        # Recomendación: no devolver un objeto de Model, debemos devolver un objeto de proyecto

        conjuntoDominios = self.session.query(BulkDominios).all() # Esto sería más correcto que poner DominiosDAO.get.. Porque así estoy trabajando en la misma sesion
        dominiosDTO = []
        for dominioDAO in conjuntoDominios:
            dominiosDTO.append(BulkDominiosDTO.from_model(dominioDAO)) # Aqui se hace la transformacion de DAO a DTO
        
        return dominiosDTO


    def insertDomains(self, listDomains):
        return None
    #TODO: itera la lista y cada dominio, comprueba que tiene campo email y si lo tiene, lo insertas en BBBDD