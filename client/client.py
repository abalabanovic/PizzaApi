#!/usr/bin/env python3.11

import os
import sys
import getpass
import time
import requests
import json

#baseUrl = 'http://127.0.0.1:5000'
try:
    baseUrl = os.environ['SERVER_IP']
except KeyError:
    print("Please give server ip to SERVER_IP in env!")
    sys.exit(1)
try:
    admin_token = os.environ['ADMIN_TOKEN']
except KeyError:
    print("Admin token is not provided!")
    print("ADMIN_TOKEN in env is not defined!")
    time.sleep(1)
    admin_token = " "

headers = {'Authorization': f'Bearer {admin_token}', 'Content-Type': 'application/json'}

def deletePizza():
    showMenu()
    id = input("Enter pizza id:\n")
    response = requests.delete(baseUrl+ f'/menu/{id}', headers=headers)
    print(f'{response.text} {response.status_code}')
    showMenu()

def createPizza():
    pizza_name = input("Enter pizza name:\n")
    pizza_price = input("Enter pizza price:\n")

    pizza_info = {'name': pizza_name,'price': pizza_price}
    response = requests.post(baseUrl + "/menu", json = pizza_info, headers = headers)

    print(f'{response.text} {response.status_code}')

def adminMenu():

    while True:

        admin_string = """
        1.Add pizza to menu
        2.Delete pizza from menu
        3.Show pizza menu
        4.Cancel order(regardless of status)
        5.Logout
        """
        print(admin_string)
        option = input("Choose an option:\n")

        if option == '1':
            createPizza()


        elif option == '2':
            deletePizza()
        
        elif option == '3':
            showMenu()

        elif option == '4':

            status = show_all_orders()
            if status:

                id = int(input("Enter order id to cancel it:\n"))

                response = requests.delete(baseUrl + f'/order/{id}', headers = headers)
                if response.status_code == 200:
                    print(f'{response.text}{response.status_code}')
                    show_all_orders()

                else:
                    print(f'{response.text}{response.status_code}')

        elif option == '5':
            sys.exit()

def show_all_orders():

    response = requests.get(baseUrl + '/get_all_orders', headers = headers)
    print(f'{response.text} {response.status_code}')
    if response.status_code == 401:
        return False
    else:
        return True

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
        
        if user is not None:

            if user['role'] == 'customer':
                menu_list(user)
            elif user['role'] == 'admin':
                adminMenu()
        else:
            print("User does not exist!Please register!")


    else:
        print(f"{response.text} {response.status_code}")

def switch(choice,user):

    if choice == "4":
        showMenu()

    elif choice == "1":
        response = showMenu()
        pizza_list = response.json().get('pizzas')
            
        if pizza_list:
            pizza_choice = int(input("Enter pizza id:\n"))
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



    elif choice == '3':
        order_number = input("Enter order id: ")

        response = requests.delete(baseUrl + f"/cancel_order/{user['username']}/{order_number}")
        print(response.text)
        print(response.status_code)

    elif choice == '5':
        sys.exit()

def menu_list(user):

    while True:

        menu_string= '''
        -----MENU------
        1.Create order
        2.Check order status
        3.Cancel order
        4.Show menu
        5.Logout
        '''
        print(menu_string)

        choice = input("Enter your choice:\n")
        
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

def lm():
    login_string = '''
Welcome to login menu:
1-----Login
2-----Go back
    '''
    print(login_string)

def loginMenu():

        while True:

            lm()
            answer2 = input("Choose an option:\n")

            if answer2 == "1":
                username = input("Enter your username:\n")
                password = getpass.getpass("Enter your password\n")

                data = {'username': username, 'password': password}
                response = requests.post(baseUrl + "/login", json=data, headers=headers)
                print(f'{response.text} {response.status_code}')

                if(response.status_code == 401):
                    continue
                else:
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

    else:
            if 400 <= response.status_code < 500:
                print(f"Client Error! {response.status_code}")
            elif 500 <= response.status_code < 600:
                print(f"Server Error! {response.status_code}")
            else:
                print(f"Unknown error! {response.status_code}")

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
        
        try:
            answer1 = input("Please choose an option\n")
        except KeyboardInterrupt:
            sys.exit()

        if answer1 == '3':
            sys.exit()

        elif answer1 == '2':
            registerMenu()

        elif answer1 == '1':
            loginMenu()


if __name__ == "__main__":
    startMenu()
