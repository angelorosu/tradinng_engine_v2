class Order:
    def __init__(self, order_id, trader_id, order_type, price, quantity):
        self.order_id = order_id
        self.trader_id = trader_id
        self.order_type = order_type
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Order ID: {self.order_id}, Trader ID: {self.trader_id}, Type: {self.order_type}, Price: {self.price}, Quantity: {self.quantity}"
