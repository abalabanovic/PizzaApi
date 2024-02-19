class User:
    
    def __init__(self,username,password,address,role='customer'):
        self.username = username
        self.password = password
        self.address = address
        self.role = role

    def __json__(self):
        return {'username': self.username, 'password': self.password, 'address': self.address,'role' : self.role}