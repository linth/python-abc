from crud.crud_rxpy.UserCRUD import UserCRUD
from rx import Observer

class UserObserver(Observer):
    
    def on_next(self, value):
        print(value)
        
    def on_error(self, error):
        print('Error:', error)
        
    def on_completed(self):
        print('Completed')
        

if __name__ == '__main__':
    
    user_crud = UserCRUD()

    # Create
    user_crud.create({'name': 'John Doe', 'email': 'johndoe@example.com'}).subscribe(UserObserver())

    # Read
    user_crud.read(1).subscribe(UserObserver())

    # Update
    user_crud.update(1, {'name': 'Jane Doe'}).subscribe(UserObserver())

    # Delete
    user_crud.delete(1).subscribe(UserObserver())
