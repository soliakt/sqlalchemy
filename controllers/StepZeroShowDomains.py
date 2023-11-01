from constants.DatabaseManager import DatabaseManager
from services import BLService # Como no es una clase no se hace el .

if __name__ == '__main__':

    # Crea una instancia de DatabaseManager
    db_manager = DatabaseManager()
    BLService.init_Services(db_manager) # Esto te crea todo el contenido del init_Services
    # Y te crea el servicio, ya que está dentro del init

    # Esto deberia estar dentro de un metodo del controlador
    BLService.dominios_service.printAllDomains()
    
# El controlador recibe las peticiones