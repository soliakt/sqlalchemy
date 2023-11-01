from dataclasses import dataclass

@dataclass
class BulkDominiosDTO:
    def __init__(self, id, email, fechaCreacion, fechaExpiracion, propietario, proveedor, importe, dominio):
        self.id = id
        self.email = email
        self.fechaCreacion = fechaCreacion
        self.fechaExpiracion = fechaExpiracion
        self.propietario = propietario
        self.proveedor = proveedor
        self.importe = importe
        self.dominio = dominio

    @classmethod
    def from_model(cls, model): # Cls simboliza clase de classmethod, y se le pasa un modelo como argumento
        if model is None:
            return None
        # Crear un diccionario con los atributos del modelo
        model_dict = {
            "id": model.id if hasattr(model, 'id') else None,
            "email": model.email,
            "fechaCreacion": model.fechaCreacion,
            "fechaExpiracion": model.fechaExpiracion,
            "propietario": model.propietario,
            "proveedor": model.proveedor,
            "importe": model.importe,
            "dominio": model.dominio
        }
        return cls(**model_dict) # los ** que es?

    def to_model(self):
        return BulkDominiosDTO(**self.__dict__)