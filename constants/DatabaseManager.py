from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
# from services.BLService import VictorLocalHostService


class DatabaseManager:
    def __init__(self):
        self.engine = create_engine('mysql://root:@localhost/MasLeads') # Sqlalchemy se conecta a la BBDD creando un engine
        # Necesitamos una sesión para conectarnos entre nuestro modelo y nuestra bbdd
        self.session = sessionmaker(bind = self.engine)
        # self.session = VictorLocalHostService("MasLeads") # La instancia session es igual a la clase Session
    
    @property
    def getSession(self):
        return self.session()