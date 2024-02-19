class Order:
    def __init__(self, id, user, pizza, price, status, address):
        self.id = id
        self.user = user
        self.pizza = pizza
        self.status = status
        self.price = price
        self.address = address

    def __json__(self):
        return {'id': self.id, 'user': self.user, 'pizza': self.pizza, 'price' : self.price, 'status': self.status, 'address': self.address}