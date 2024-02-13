from order import Order
import time
import threading

class OrderManager:
    def __init__(self):

        self.orders = []
        self.order_id = 0

    def make_order(self, user, pizza, address, price, status='Not ready'):

        new_order = Order(self.order_id, user, pizza, price,status,address)
        self.order_id+=1
        self.orders.append(new_order)

        threading.Thread(target=self.change_order_status, args=(new_order,), daemon=True).start()

        return new_order

    def get_user_orders(self, username):

        print(self.orders)
        return [order.__json__() for order in self.orders if order.user == username]

    def get_all_orders(self):

        print(self.orders)
        return [order.__json__() for order in self.orders]

    def change_order_status(self, order):
        time.sleep(60)
        order.status = "Ready to be delivered"
        print(f"Order{order.id} is ready to be delivered")

    def cancel_order(self, username, order_id):
         
         if not self.orders:
            return ("There is no orders at this moment", 404)

         else:

            for order in self.orders:
                if order.id == int(order_id) and order.user == username:
                    if order.status != "Ready to be delivered":
                        self.orders.remove(order)
                        return ("Succesfully removed", 200)
                    else:
                        return ("It is to late to cancel order!", 404)
                else :
                    return ("Order does not exist!",404)

    def cancel_order_admin(self, order_id):

        #Admin can always cancel order
        for order in self.orders:
            if order.id == int(order_id):
                self.orders.remove(order)
                return self.orders
            else:
                return None

