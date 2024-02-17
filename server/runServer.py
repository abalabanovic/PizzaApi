#!/usr/bin/env python3.11

from pizzaHandler import PizzaHandler
from userHandler import UserHandler
from orderHandler import OrderHandler
from flask import Flask,request,jsonify
import os

app = Flask(__name__)

user_Handler = UserHandler()
pizzaHandler = PizzaHandler()
orderHandler = OrderHandler()

server_token = '1234'

def tokenCheck(token):

    if token == server_token:
        return True
    else:
        return False

#CLIENT

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return user_Handler.register_user(data)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return user_Handler.login(data)

@app.route('/get_logged_user', methods=['GET'])
def get_logged_user():
    return user_Handler.get_logged_user()

@app.route('/get_menu', methods=['GET'])
def get_menu():
    return pizzaHandler.get_pizzas()

@app.route('/make_order', methods=['POST'])
def make_order():
    data = request.get_json()
    return orderHandler.make_order(data)

@app.route('/get_orders/<user>', methods=['GET'])
def get_orders(user):
    return orderHandler.get_user_orders(user)

@app.route('/cancel_order/<username>/<order_id>', methods=['DELETE'])
def cancel_order(username, order_id):
    return orderHandler.user_cancel_order(username,order_id)

#ADMIN

@app.route('/menu', methods = ['POST'])
def add_pizza():
    data = request.get_json()
    return pizzaHandler.add_pizza_admin(data)

@app.route('/menu/<pizza_id>', methods=['DELETE'])
def delete_admin(pizza_id):
    return pizzaHandler.delete_pizza_admin(pizza_id)

@app.route('/order/<order_id>', methods=['DELETE'])
def cancel_order_admin(order_id):
    return orderHandler.admin_cancel_order(order_id)

@app.route('/get_all_orders', methods=['GET'])
def see_all_orders():
    return orderHandler.get_all_orders()




if __name__ == '__main__':
    app.run(debug=True)