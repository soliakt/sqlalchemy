from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float



Base = declarative_base() # Esto hace que sqlalchemy sepa que es una tabla


class DominiosValidados(Base):
    __tablename__ = 'DominiosValidados'

    id = Column(Integer, primary_key = True, autoincrement = True)
    email = Column(String(40), nullable = True)
    fechaCreacion = Column(DateTime, nullable = True)
    fechaExpiracion = Column(DateTime, nullable = True)
    propietario = Column(String(40), nullable = True)
    proveedor = Column(String(40), nullable = True)
    importe = Column(Float, nullable = True)
    dominio = Column(String(40), nullable = True)

    def __str__(self):
        return self.id