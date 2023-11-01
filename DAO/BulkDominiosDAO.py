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
    
    def checkDomainsCorrectness(self, bulkDomainsList) -> bool:
        if not bulkDomainsList:
            print("La lista está vacía")
        for bulkDomain in bulkDomainsList:
            if not bulkDomain.email:
                raise ValueError(f"El campo 'email' no puede estar vacío. Fallo en dominio con email: {bulkDomain.email}")
            if not bulkDomain.dominio:
                raise ValueError(f"El campo 'dominio' no puede estar vacío. Fallo en dominio con email: {bulkDomain.email}")
            if bulkDomain.importe is None or bulkDomain.importe < 0:
                raise ValueError(f"El campo 'importe' no es válido. Fallo en dominio con email: {bulkDomain.email}")
            if bulkDomain.fechaCreacion is None:
                raise ValueError(f"El campo 'fechaCreacion' no puede estar vacío. Fallo en dominio con email: {bulkDomain.email}")
            if bulkDomain.fechaExpiracion is None:
                raise ValueError(f"El campo 'fechaExpiracion' no puede estar vacío. Fallo en dominio con email: {bulkDomain.email} ")
            if bulkDomain.fechaCreacion > bulkDomain.fechaExpiracion:
                raise ValueError(f"La fecha de creación debe ser anterior a la fecha de expiración. Fallo en dominio con email: {bulkDomain.email}")
            if not bulkDomain.propietario:
                raise ValueError(f"El campo 'propietario' no puede estar vacío. Fallo en dominio con email: {bulkDomain.email}")
            if not bulkDomain.proveedor:
                raise ValueError(f"El campo 'proveedor' no puede estar vacío. Fallo en dominio con email: {bulkDomain.email}")
        return True


    def insertDomainsIntoBulkBBDD(self, bulkDomainsList) -> None:
    #TODO: itera la lista y cada dominio, comprueba que tiene campo email y si lo tiene, lo insertas en BBBDD
        if self.checkDomainsCorrectness(bulkDomainsList) == True:
            contadorDominiosInsertados = 0
            try:
                for bulkDomain in bulkDomainsList:
                    bulkDomainIn = BulkDominios(
                        id = bulkDomain.id,
                        email = bulkDomain.email,
                        fechaExpiracion = bulkDomain.fechaExpiracion,
                        fechaCreacion = bulkDomain.fechaCreacion,
                        propietario = bulkDomain.propietario,
                        proveedor = bulkDomain.proveedor,
                        importe = bulkDomain.importe,
                        dominio = bulkDomain.dominio
                    )
                    self.session.add(bulkDomainIn)
                    contadorDominiosInsertados += 1
                # Obvio pero: aqui tratamos con DAOs en lugar de DTOs porque es relacion directamente con la BBDD
                self.session.commit()
                print(f"Se han insertado con éxito {contadorDominiosInsertados} registros")
            except Exception as e:
                print(f"Error al insertar dominios en la base de datos: {str(e)}") # Hacemos el parseString porque sino devolveria la excepcion como un objeto en lugar de texto 
