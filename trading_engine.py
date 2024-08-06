import yfinance as yf
from order_book import OrderBook
from order import Order
class TradingEngine:
    def __init__(self):
        self.order_book = OrderBook()
        self.current_price = None

    def fetch_live_data(self, ticker):
        """Fetch live data for a specific stock ticker."""
        stock = yf.Ticker(ticker)
        self.current_price = stock.history(period='1d').iloc[-1]['Close']
        return self.current_price

    def place_order(self, order_id, trader_id, order_type, price, quantity):
        """Place an order in the market."""
        if self.current_price is None:
            raise ValueError("Current price not set. Cannot place order.")
        
        if price < self.current_price * 0.5 or price > self.current_price * 1.5:
            raise ValueError(f"Order price {price} is outside realistic bounds.")

        order = Order(order_id, trader_id, order_type, price, quantity)
        self.order_book.add_order(order)
        self.order_book.match_orders()  # Attempt to match orders after placing a new one

    def get_trade_log(self):
        """Return the trade log from the order book."""
        return self.order_book.trade_log

    def __repr__(self):
        return str(self.order_book)
