from pizza import Pizza

class PizzaManager():
    def __init__(self):
        self.allPizzas = []
        
        pizza1 = Pizza(0, 'Bianka', 15)
        pizza2 = Pizza(1, 'Capricciosa', 12)
        pizza3 = Pizza(2, 'Quatro staggione', 20)
        pizza4 = Pizza(3, 'BBQ chicken', 17)
        pizza5 = Pizza(4, 'Pepperoni',14)
        pizza6 = Pizza(5, 'Pesto', 16)
        self.allPizzas.append(pizza1)
        self.allPizzas.append(pizza2)
        self.allPizzas.append(pizza3)
        self.allPizzas.append(pizza4)
        self.allPizzas.append(pizza5)
        self.allPizzas.append(pizza6)

        self.next_id = len(self.allPizzas) - 1


    def delete_pizza(self, id):


        for pizza in self.allPizzas:
           if pizza.id == int(id):
               self.allPizzas.remove(pizza)
               return self.allPizzas

        return None    

    def get_pizzas(self):
        info = []
        for pizza in self.allPizzas:
            info.append(pizza.__json__())
        return info
    
    def change_price_pizza(self, search_id, newPrice):
        
        for pizza in self.allPizzas:
            if pizza.id == search_id:
                pizza.change_price(newPrice)

    def add_pizza_in_list(self, data):
        
         new_id = self.next_id + 1
         pizza = Pizza(new_id,name=data['name'], price=data['price'])
         self.allPizzas.append(pizza)
         return pizza