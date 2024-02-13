from pizzaMng import PizzaManager
from flask import jsonify

class PizzaHandler:
    def __init__(self):
        self.pizza_manager = PizzaManager()

   
    def get_pizzas(self):
        get_pizzas = self.pizza_manager.get_pizzas()
        return jsonify({'pizzas' : get_pizzas})
        

