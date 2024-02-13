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
  
if __name__ == '__main__':
    app.run(debug=True)