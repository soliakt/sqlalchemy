from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float



Base = declarative_base() # Esto hace que sqlalchemy sepa que es una tabla


class BulkDominios(Base):
    __tablename__ = 'BulkDomains'

    id = Column(Integer, primary_key = True, autoincrement = True)
    email = Column(String(40), nullable = False)
    fechaCreacion = Column(DateTime, nullable = False)
    fechaExpiracion = Column(DateTime, nullable = False)
    propietario = Column(String(40), nullable = False)
    proveedor = Column(String(40), nullable = False)
    importe = Column(Float, nullable = False)
    dominio = Column(String(40), nullable = False)

    def __str__(self):
        return self.id