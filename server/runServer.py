#!/usr/bin/env python3.10

from Handlers.pizzaHandler import PizzaHandler
from Handlers.userHandler import UserHandler
from Handlers.orderHandler import OrderHandler
from flask import Flask,request,jsonify
import os

app = Flask(__name__)

user_Handler = UserHandler()
pizzaHandler = PizzaHandler()
orderHandler = OrderHandler()

server_token = 'ABC123'

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
    token = request.headers.get('Authorization').split(' ')[1]
    if tokenCheck(token):
        admin_status = True
    else:
        admin_status = False
    return user_Handler.login(data, admin_status)

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
    token = request.headers.get('Authorization').split(' ')[1]
    if tokenCheck(token):
        return pizzaHandler.add_pizza_admin(data)
    else:
        return jsonify({'message': 'Unauthorized'}), 401


@app.route('/menu/<pizza_id>', methods=['DELETE'])
def delete_admin(pizza_id):
    token = request.headers.get('Authorization').split(' ')[1]
    if tokenCheck(token):
        return pizzaHandler.delete_pizza_admin(pizza_id)
    else:
        return jsonify({'message': 'Unauthorized'}), 401

@app.route('/order/<order_id>', methods=['DELETE'])
def cancel_order_admin(order_id):
    token = request.headers.get('Authorization').split(' ')[1]
    if tokenCheck(token):
        return orderHandler.admin_cancel_order(order_id)
    else:
        return jsonify({'message': 'Unauthorized'}), 401

@app.route('/get_all_orders', methods=['GET'])
def see_all_orders():
    token = request.headers.get('Authorization').split(' ')[1]
    if tokenCheck(token):
        return orderHandler.get_all_orders()
    else:
        return jsonify({'message': 'Unauthorized'}), 401



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
