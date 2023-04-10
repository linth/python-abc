from crud.custom_crud.AbstractCRUD import AbstractCRUD
from crud.custom_crud.User import User


class UserCRUD(AbstractCRUD):
    """ implement the functionalility of user's CRUD. """
    
    def __init__(self):
        self.users = {}
        self.id_counter = 0
            
    def create(self, data):
        user = User(data['name'], data['email'])
        self.id_counter += 1
        self.users[self.id_counter] = user
        return self.id_counter
        
    def read(self, id):
        return self.users.get(id, None)
        
    def update(self, id, data):
        user = self.read(id)
        if user:
            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)
            return True
        else:
            return False
        
    def delete(self, id):
        user = self.users.pop(id, None)
        if user:
            return True
        else:
            return False