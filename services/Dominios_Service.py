# Aquí va la lógica

from DAO.DominiosDAO import DominiosDAO
from DTO.DominiosDTO import DominiosDTO

class Dominios_Service:
    def __init__(self, dao: DominiosDAO):
        self.dao = dao
    
    def getDomains(self):
        dominiosDAO = self.dao.getAllDomains() # Esto sería más correcto que poner DominiosDAO.get.. POrque asi estoy trabajando en la misma sesion
        dominiosDTO = []
        for dominioDAO in dominiosDAO:
            dominiosDTO.append(DominiosDTO.from_model(dominioDAO)) # Aqui se hace la transformacion de DAO a DTO

        return dominiosDTO
    
    def printAllDomains(self):
        listaDominiosDTO = self.getDomains()
        for dominio in listaDominiosDTO:
            print(dominio.dominio)