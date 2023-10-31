from services.Dominios_Service import Dominios_Service
from DAO.BulkDominiosDAO import BulkDominiosDAO
from constants.DatabaseManager import DatabaseManager


dominios_service = None

def init_Services(db_manager:DatabaseManager):
    global dominios_service
    dominios_service = Dominios_Service(BulkDominiosDAO(db_manager.getSession)) # al ser un @property no hay que poner los parentesis

