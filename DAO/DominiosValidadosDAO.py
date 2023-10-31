from sqlalchemy.orm import Session
from typing import List

from DTO.BulkDominiosDTO import BulkDominiosDTO
from models.BulkDominios import BulkDominios
from models.DominiosValidados import DominiosValidados


class DominiosValidadosDAO:
    def __init__(self, session: Session):
        self.session = session

    def getAllBulkDomains(self) -> List[BulkDominiosDTO]:
        # Recomendación: no devolver un objeto de Model, debemos devolver un objeto de proyecto

        conjuntoDominios = self.session.query(BulkDominios).all() # Esto sería más correcto que poner DominiosDAO.get.. Porque así estoy trabajando en la misma sesion
        dominiosDTO = []
        for dominioDAO in conjuntoDominios:
            dominiosDTO.append(BulkDominiosDTO.from_model(dominioDAO)) # Aqui se hace la transformacion de DAO a DTO
        
        return dominiosDTO


    def insertDomains(self, bulkDomainsListDTO):
        if not bulkDomainsListDTO:
            print("La lista está vacía")
        for bulkDomain in bulkDomainsListDTO:
            if bulkDomain.email is not None:
                dominioValidado = DominiosValidados(
                    id = bulkDomain.id,
                    email = bulkDomain.email,
                    fechaExpiracion = bulkDomain.fecha_expiracion,
                    fechaCreacion = bulkDomain.fecha_creacion,
                    propietario = bulkDomain.propietario,
                    proveedor = bulkDomain.proveedor,
                    importe = bulkDomain.importe,
                    dominio = bulkDomain.dominio
                )
                self.session.add(dominioValidado)
        self.session.commit()