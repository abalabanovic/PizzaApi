from Managers.userMng import UserManager
from flask import Flask, request,jsonify
import os

class UserHandler:

    def __init__(self):
        self.userManager = UserManager()

    def register_user(self,data):
        username = data.get('username')
        password = data.get('password')
        address = data.get('address')
        
        if not username or not password or not address:
                return jsonify({'error':'Arguments missing'}), 400

        new_user = self.userManager.register_user(username,password,address)
        
        if new_user:

            return jsonify({'message':'Succesful'}), 201

        else:

            return jsonify({'message' : 'Username is already taken'}), 409
    
    def login(self,data,admin_token_status):

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"error": 'Arguments missing'}), 400

        login_user = self.userManager.login_user(username,password)


        if login_user:

            if login_user.role == 'customer':
                    return jsonify({"Message":"Succesfull login!"}),200

            else:
                    #check token
                    if admin_token_status:
                        return jsonify({"Message": "Welcome admin!"}), 200
                    else:
                        return jsonify({"Message": "Unauthorized!"}), 401
        else : 

                return jsonify({"Error":"User not found"}), 404

    def get_logged_user(self):

    
        logged_user = self.userManager.get_logged_user()

        return jsonify(logged_user)
