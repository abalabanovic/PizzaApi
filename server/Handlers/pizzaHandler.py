from Managers.pizzaMng import PizzaManager
from flask import jsonify

class PizzaHandler:
    def __init__(self):
        self.pizza_manager = PizzaManager()

   
    def get_pizzas(self):
        get_pizzas = self.pizza_manager.get_pizzas()
        return jsonify({'pizzas' : get_pizzas})
        
    def delete_pizza_admin(self, pizza_id):
        print(pizza_id)
        new_pizza_menu = self.pizza_manager.delete_pizza(pizza_id)

        if new_pizza_menu:
            return jsonify({'message' : "Pizza was deleted"}), 200
        else:
            return jsonify({'Erorr': 'Something went wrong!'}), 404

    def add_pizza_admin(self, data):
        add_pizza = self.pizza_manager.add_pizza_in_list(data)

        if add_pizza:
            print(self.pizza_manager.allPizzas)
            return jsonify({'message' : 'Pizza added to menu'}), 201
        else:
            return jsonify({'message' : 'Something went wrong'}), 409
