# from datetime import datetime
# from flask import Flask
# from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float

# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import declarative_base



# engine = create_engine('mysql://root:@localhost/MasLeads') # Sqlalchemy se conecta a la BBDD creando un engine


# engine = create_engine('mysql+pymysql://soliakt:@localhost/MasLeads') # Sqlalchemy se conecta a la BBDD creando un engine

#Base = declarative_base()


# class Dominio(Base):
#     __tablename__ = 'Dominios'

#     id = Column(Integer, primary_key = True, autoincrement = True)
#     email = Column(String(40), nullable = True)
#     fechaCreacion = Column(DateTime, nullable = True)
#     fechaExpiracion = Column(DateTime, nullable = True)
#     propietario = Column(String(40), nullable = True)
#     proveedor = Column(String(40), nullable = True)
#     importe = Column(Float, nullable = True)
#     dominio = Column(String(40), nullable = True)

#     def __str__(self):
#         return self.id

# Necesitamos una sesión para conectarnos entre nuestro modelo y nuestra bbdd
# Session = sessionmaker(engine)
# session = Session() # La instancia session es igual a la clase Session


#if __name__ == '__main__':
    # Insertar valores en la BBDD
    # dominioVictor = Dominio(
    #     id=123,
    #     email="victor@regla.com",
    #     fechaCreacion=datetime.now(),
    #     fechaExpiracion='2024-05-24',  # Asegúrate de usar el formato correcto de fecha.
    #     propietario="Victor",
    #     proveedor="Squarespace",
    #     importe=13.05,
    #     dominio="regla.com"
    # )
    # session.add(dominioVictor)

    # Hacer un update:
    # dominio = session.query(Dominio).filter_by(id=13).first()
    # dominio.id = 11
    # session.commit()

    # Hacer un delete:
    # dominio = session.query(Dominio).filter_by(id=12).first()
    # if dominio:
    #     session.delete(dominio)
    #     session.commit()
    # else:
    #     print("Registro no encontrado.")
    # Ver todos los registros de la tabla 'Dominios'
    # dominios = session.query(Dominio).all()

    # # Itera a través de los dominios
    # for registro in dominios:
    #     print(registro.id, registro.email, registro.fechaCreacion, registro.fechaExpiracion,  registro.propietario, registro.proveedor, registro.importe, registro.dominio)
    

        
    # session.close()