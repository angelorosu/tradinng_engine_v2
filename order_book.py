class OrderBook:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []
        self.trade_log = []

    def add_order(self, order):
        """Add an order to the order book."""
        if order.order_type == 'buy':
            self.buy_orders.append(order)
            self.buy_orders.sort(key=lambda x: x.price, reverse=True)  # Highest price first
        elif order.order_type == 'sell':
            self.sell_orders.append(order)
            self.sell_orders.sort(key=lambda x: x.price)  # Lowest price first

    def add_trade(self, order, trade_price):
        """Add a trade to the trade log."""
        trade_details = {
            'order_id': order.order_id,
            'trader_id': order.trader_id,
            'order_type': order.order_type,
            'trade_price': trade_price,
            'quantity': order.quantity
        }
        self.trade_log.append(trade_details)

    def match_orders(self):
        """Match buy and sell orders."""
        while self.buy_orders and self.sell_orders:
            buy_order = self.buy_orders[0]
            sell_order = self.sell_orders[0]

            if buy_order.price >= sell_order.price:
                trade_price = sell_order.price
                trade_quantity = min(buy_order.quantity, sell_order.quantity)
                
                # Record the trade
                self.add_trade(buy_order, trade_price)
                
                # Update quantities
                buy_order.quantity -= trade_quantity
                sell_order.quantity -= trade_quantity

                # Remove filled orders
                if buy_order.quantity == 0:
                    self.buy_orders.pop(0)
                if sell_order.quantity == 0:
                    self.sell_orders.pop(0)
            else:
                break

    def __repr__(self):
        return (f"Buy Orders: {self.buy_orders}\n"
                f"Sell Orders: {self.sell_orders}\n"
                f"Trade Log: {self.trade_log}")
