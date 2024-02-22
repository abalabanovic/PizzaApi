from baseModels.user import User

class UserManager:

    def __init__(self):
        self.users = []
        self.logged_user = None
        admin = User('admin', 'admin', None, 'admin')
        #FOR TESTING ONLY
        self.users.append(admin)
        

    def login_user(self,username,password):
        for user in self.users:
            if user.username == username:
                if user.password == password:
                    self.logged_user = user
                    return user
                
        return None
    def register_user(self, username, password, address, role= 'customer'):

        for user in self.users:
            if user.username == username:
                print("Username already exists!")
                return None
        
        new_user = User(username,password, address, role)
        self.users.append(new_user)
        return new_user
    
    def get_all_users(self):

        all_users = []
        for user in self.users:
            all_users.append(user.__json__())
        return all_users

    def get_logged_user(self):

        try:
            
            if self.logged_user is not None:
                return self.logged_user.__json__()
            else:
                print("User is not found!")
                return None            
        except AttributeError as e:
            print("AttributeError:", e)
            return None
        except Exception as e:
            print("Error:", e)
            return None
    
    def logout(self):
        self.logged_user = None
