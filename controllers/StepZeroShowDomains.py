from models.Dominios import Dominios


from constants.DatabaseManager import DatabaseManager
from DAO.DominiosDAO import DominiosDAO
from services import BLService # Como no es una clase no se hace el .

if __name__ == '__main__':

    # Crea una instancia de DatabaseManager
    db_manager = DatabaseManager()
    BLService.init_Services(db_manager) # Esto te crea todo el contenido del init_Services
    # Y te crea el servicio, ya que está dentro del init

    BLService.dominios_service.printAllDomains()
    
