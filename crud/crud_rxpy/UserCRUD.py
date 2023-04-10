from pymongo import MongoClient
from crud.crud_rxpy.CRUD import AbstractUserCRUD


class UserCRUD(AbstractUserCRUD):
    
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['user_management']
        self.collection = self.db['users']
        
    def get_collection(self):
        return self.collection