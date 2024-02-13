#!/usr/bin/env python3.11

import os
import sys
import getpass
import time
import requests
import json

baseUrl = 'http://127.0.0.1:5000'


def createOrder(user, pizza):
    data = {'username': user['username'], 'address': user['address'], 'pizza': pizza}
    response = requests.post(baseUrl + "/make_order", json=data)

    if response.status_code == 201:
        print("Order is created")
        print(response.text)
    else:
        print(f"Error:{response.status_code}")

def get_log_user():

    response = requests.get(baseUrl + "/get_logged_user")
    
    if response.status_code == 200:
        user = response.json()

    menu_list(user)

def switch(choice,user):

    if choice == "4":
        showMenu()

    elif choice == "1":
        response = showMenu()
        pizza_list = response.json().get('pizzas')
            
        if pizza_list:
            pizza_choice = int(input("Enter pizza id"))
            selected_pizza = next((pizza for pizza in pizza_list if pizza['id'] == pizza_choice),None)

            if selected_pizza:
                    
                createOrder(user, selected_pizza)

            else:
                    print("Invalid pizza id!")
        else:
                print("Pizza list is empty!")

    elif choice == '2':
        response = requests.get(baseUrl + f"/get_orders/{user['username']}")

        print(f'{response.text} {response.status_code}')

        if response.status_code == 200:
            orders = response.json().get('orders')
            print(orders)

    elif choice == '3':
        order_number = input("Enter order id: ")

        response = requests.delete(baseUrl + f"/cancel_order/{user['username']}/{order_number}")
        print(response.text)
        print(response.status_code)

def menu_list(user):

    while True:

        print("-----MENU------")
        print("1.Create order")
        print("2.Check order status")
        print("3.Cancel order")
        print("4.Show menu")
        print("5.Logout")
        print("---------------")

        choice = input("Enter your choice: ")
        
        switch(choice,user)

def showMenu():

    response = requests.get(baseUrl + "/get_menu")
    
    if response.status_code == 200:
        pizza_list = response.json().get('pizzas')
        if not pizza_list:
            print("Pizza menu is empty!")
        else:
            print("--------PIZZA MENU-------")
            for pizza in pizza_list:
                print(f"{pizza['id']}. {pizza['name']} {str(pizza['price'])}$")

    return response

def loginMenu():

        while True:

            print("----Welcome to loging menu----")
            print("1----Login")
            print("2----Main menu")
            answer2 = input("Choose an option")

            if answer2 == "1":
                username = input("Enter your username:\n")
                password = getpass.getpass("Enter your password\n")

                data = {'username': username, 'password': password}
                response = requests.post(baseUrl + "/login", json=data)
                print(f'{response.text} {response.status_code}')

                get_log_user()

            elif answer2 == '2':
                startMenu()



def registerUser(username,password,address):

    data = {'username':username, 'password':password, 'address': address}

    response = requests.post(baseUrl + "/register",json=data)
    print(response.text)
    print(response.status_code)

    if response.status_code == 201:
            print(f"Welcome {username}, please log in to continue!")
            time.sleep(1)
            loginMenu()
            
    elif response.status_code == 409:
            print("Username already exist!Please use another one")

    elif response.status_code == 400:
            print("Arguments are missing!Please try again!")

def registerMenu():

    username = input("Please enter a username:\n")
    password = None

    while True:
        password1 = getpass.getpass('Enter your password\n')
        password2 = getpass.getpass('Please confirm your password\n')
        if password1 == password2:
            password = password1
            break
        else:
            print("Your passwords don't match!Please try again")
            continue

    address = input("Please enter your address:\n")
    registerUser(username,password,address)


    
def startMenu():

    while True:

        print("Welcome to client")
        time.sleep(1)
        print("1--------LOGIN")
        print("2--------REGISTER")
        print("3--------EXIT")
        answer1 = input("Please choose an option\n")

        if answer1 == '3':
            sys.exit()

        elif answer1 == '2':
            registerMenu()

        elif answer1 == '1':
            loginMenu()


if __name__ == "__main__":
    startMenu()
