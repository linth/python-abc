from crud.custom_crud.CRUDInterface import CRUDInterface
from crud.custom_crud.UserCRUD import UserCRUD


class UserAPI(CRUDInterface):
    """ user's RESTful API. """
    
    def __init__(self):
        self.crud = UserCRUD()
        
    def create(self, data):
        return self.crud.create(data)
    
    def read(self, id):
        return self.crud.read(id)
    
    def update(self, id, data):
        return self.crud.update(id, data)
    
    def delete(self, id):
        return self.crud.delete(id)
    
    