# Aquí va la lógica

from DAO.BulkDominiosDAO import BulkDominiosDAO
from models.BulkDominios import BulkDominios
from datetime import datetime
from typing import List

class Dominios_Service:
    def __init__(self, dao: BulkDominiosDAO):
        self.dao = dao

    def printAllDomains(self):
        listaBulkDominiosDTO = self.dao.getAllBulkDomains()
        for bulkDominioDTO in listaBulkDominiosDTO:
            print(bulkDominioDTO.fechaCreacion)
    
    def createAndInsertDomains(self) -> None:
        # Crea una lista con 5 dominios (a mano mismo)
        # Usa el metodo del dao para insertarlos
        listaDominiosAInsertar = []

        dominio1 = BulkDominios(
            dominio = "lanjaron.com",
            email = "example@lanjaron.com",
            fechaCreacion = datetime(2022, 1, 15),
            fechaExpiracion = datetime(2023, 1, 15),
            propietario = "John Doe",
            proveedor = "Hosting Company",
            importe = 49.99
        )
        listaDominiosAInsertar.append(dominio1)

        dominio2 = BulkDominios(
            dominio = "hotel.net",
            email = "info@hotel.net",
            fechaCreacion = datetime(2022, 3, 20),
            fechaExpiracion = datetime(2023, 3, 20),
            propietario = "Jane Smith",
            proveedor = "Domain Registrar",
            importe = 29.99
        )
        listaDominiosAInsertar.append(dominio2)

        dominio3 = BulkDominios(
            dominio = "mercadona.com",
            email = "contact@mercadona.com",
            fechaCreacion = datetime(2022, 2, 10),
            fechaExpiracion = datetime(2023, 2, 10),
            propietario = "Mark Johnson",
            proveedor = "Hosting Company",
            importe = 39.99
        )
        listaDominiosAInsertar.append(dominio3)

        dominio4 = BulkDominios(
            dominio ="webapp.io",
            email = "support@webapp.io",
            fechaCreacion = datetime(2022, 4, 5),
            fechaExpiracion = datetime(2023, 4, 5),
            propietario = "Emily Davis",
            proveedor = "Cloud Hosting",
            importe = 59.99
        )
        listaDominiosAInsertar.append(dominio4)

        dominio5 = BulkDominios(
            dominio = "dondominio.com",
            email = "info@dondominio.com",
            fechaCreacion = datetime(2022, 1, 30),
            fechaExpiracion = datetime(2023, 1, 30),
            propietario = "Mike Wilson",
            proveedor = "Domain Registrar",
            importe = 34.99
        )
        listaDominiosAInsertar.append(dominio5)

        self.dao.insertDomainsIntoBulkBBDD(listaDominiosAInsertar)