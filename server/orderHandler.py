from orderMng import OrderManager
from flask import jsonify
import threading

class OrderHandler:
    def __init__(self):
        self.order_manager = OrderManager()

    def make_order(self, data):
        user = data.get('username')
        address = data.get('address')
        pizza = data.get('pizza')

        add_order = self.order_manager.make_order(user,
        pizza['name'], address, pizza['price'])
        

        if add_order:
            return jsonify({'message':"Order has been created"}),201        


    
    def get_user_orders(self,user):
        orders = self.order_manager.get_user_orders(user)

        if orders:
            return jsonify({'orders': orders}), 200
        else:
            return jsonify({'message' : 'Orders not found'}), 404

    
    def user_cancel_order(self, username, order_id):
        cancel_order = self.order_manager.cancel_order(username, order_id)

        return jsonify({'message': cancel_order[0],}), cancel_order[1]

   
        