# Aquí va la lógica

from DAO.BulkDominiosDAO import BulkDominiosDAO

class Dominios_Service:
    def __init__(self, dao: BulkDominiosDAO):
        self.dao = dao

    def printAllDomains(self):
        listaBulkDominiosDTO = self.dao.getAllBulkDomains()
        for bulkDominioDTO in listaBulkDominiosDTO:
            print(bulkDominioDTO.dominio)
    
    def createAndInsertDomains(self):
        return None
    #Crea una lista con 5 dominios (a mano mismo)
    #Usa el metodo del dao para insertarlos