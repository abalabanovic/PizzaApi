Pizza ordering using HTTP requests

App default port : 8000
ENV variables:
SERVER_IP = ip address of server, example "http://127.0.0.1:8000"
ADMIN_TOKEN = auth token for doing admin actions and to log in as admin


Endpoints on server:

#Client

POST/register - register as a new user, providing username,password and address
POST/login - login as a existing user, providing username and password
GET/get_logged_user - get currently logged user
GET/get_menu - get menu of pizzas available to order
POST/make_order - order pizza providing pizza IDs
GET/get_orders/<user> - get current orders from <user>
DELETE/cancel_order/<username>/<order_id> - cancel order providing order id if the status of order is NOT READY

#ADMIN
#Every admin action requires token validation!
#token is send with header in each HTTP request

POST/menu - add new pizza to menu, providing pizza name and price 
DELETE/menu/<pizza_id> - delete pizza from menu using pizza id
DELETE/order/<order_id> - cancel order providing order id, admin is able to cancel order even if the order is ready to be delivered
GET/get_all_orders - list all available orders

#ADMIN AND CLIENT

GET/logout - logout as a current user

