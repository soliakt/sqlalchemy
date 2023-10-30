from DAO.LogDAO import LogDAO

class LogService:

    def __init__(self, dao: LogDAO):
        self.dao = dao