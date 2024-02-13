class Pizza:
    
    def __init__(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price


    def change_price(self, newPrice):
        self.price = newPrice

    #Return json from data
    
    def __json__(self):
        return {'id': self.id, 'name' : self.name, 'price': self.price}