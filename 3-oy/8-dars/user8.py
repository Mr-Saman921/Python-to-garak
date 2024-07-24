from Validator8 import UserValidator
from Db8 import Db
class User(UserValidator, Db):

    def __init__(self, username: str, tg_id: str, name: str, surname: str):
        # super(). __init__(username, tg_id, name, surname)
        self.username = username
        self.tg_id = tg_id
        self.name = name
        self.surname = surname