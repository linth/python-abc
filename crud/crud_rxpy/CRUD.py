from abc import ABC, abstractmethod
from rx import Observable

class CRUDInterface(ABC):
    
    @abstractmethod
    def create(self, data):
        pass
    
    @abstractmethod
    def read(self, id):
        pass
    
    @abstractmethod
    def update(self, id, data):
        pass
    
    @abstractmethod
    def delete(self, id):
        pass

class AbstractUserCRUD(CRUDInterface, ABC):
    
    @abstractmethod
    def get_collection(self):
        pass
    
    def create(self, data):
        return Observable.create(lambda observer: 
            observer.on_next(self.get_collection().insert_one(data).inserted_id))
        
    def read(self, id):
        return Observable.create(lambda observer:
            observer.on_next(self.get_collection().find_one({'_id': id})))
        
    def update(self, id, data):
        return Observable.create(lambda observer:
            observer.on_next(self.get_collection().update_one({'_id': id}, {'$set': data}).modified_count > 0))
        
    def delete(self, id):
        return Observable.create(lambda observer:
            observer.on_next(self.get_collection().delete_one({'_id': id}).deleted_count > 0))