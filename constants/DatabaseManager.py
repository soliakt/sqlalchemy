from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


class DatabaseManager:
    def __init__(self):
        self.engine = create_engine('mysql://root:@localhost/MasLeads') # Sqlalchemy se conecta a la BBDD creando un engine
        # Necesitamos una sesión para conectarnos entre nuestro modelo y nuestra bbdd
        self.session = sessionmaker(bind = self.engine)
    
    @property
    def getSession(self):
        return self.session()