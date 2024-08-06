import tkinter as tk
from tkinter import messagebox
from trading_engine import TradingEngine

class TradingGUI:
    def __init__(self, root):
        self.engine = TradingEngine()
        self.root = root
        self.root.title("Trading Engine")

        # Create widgets
        self.create_widgets()

        # Example ticker
        self.ticker = 'AAPL'
        self.update_market_data()

    def create_widgets(self):
        # Order Form
        form_frame = tk.Frame(self.root)
        form_frame.pack(padx=10, pady=10)

        tk.Label(form_frame, text="Order ID:").grid(row=0, column=0, padx=5, pady=5)
        self.order_id_entry = tk.Entry(form_frame)
        self.order_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Trader ID:").grid(row=1, column=0, padx=5, pady=5)
        self.trader_id_entry = tk.Entry(form_frame)
        self.trader_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Order Type:").grid(row=2, column=0, padx=5, pady=5)
        self.order_type_var = tk.StringVar(value='buy')
        tk.Radiobutton(form_frame, text="Buy", variable=self.order_type_var, value='buy').grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        tk.Radiobutton(form_frame, text="Sell", variable=self.order_type_var, value='sell').grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Price:").grid(row=3, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(form_frame)
        self.price_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Quantity:").grid(row=4, column=0, padx=5, pady=5)
        self.quantity_entry = tk.Entry(form_frame)
        self.quantity_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Button(form_frame, text="Place Order", command=self.place_order).grid(row=5, columnspan=2, pady=10)

        # Market Data Display
        self.market_data_frame = tk.Frame(self.root)
        self.market_data_frame.pack(padx=10, pady=10)

        tk.Label(self.market_data_frame, text="Current Price:").grid(row=0, column=0)
        self.price_label = tk.Label(self.market_data_frame, text="N/A")
        self.price_label.grid(row=0, column=1)

        # Order Book Display
        self.order_book_frame = tk.Frame(self.root)
        self.order_book_frame.pack(padx=10, pady=10)

        tk.Label(self.order_book_frame, text="Buy Orders").grid(row=0, column=0)
        self.buy_order_list = tk.Listbox(self.order_book_frame, width=40, height=10)
        self.buy_order_list.grid(row=1, column=0)

        tk.Label(self.order_book_frame, text="Sell Orders").grid(row=0, column=1)
        self.sell_order_list = tk.Listbox(self.order_book_frame, width=40, height=10)
        self.sell_order_list.grid(row=1, column=1)

        # Trade Log
        self.trade_log_frame = tk.Frame(self.root)
        self.trade_log_frame.pack(padx=10, pady=10)

        tk.Label(self.trade_log_frame, text="Trade Log").grid(row=0, column=0)
        self.trade_log = tk.Listbox(self.trade_log_frame, width=80, height=10)
        self.trade_log.grid(row=1, column=0)

        # Initial Update
        self.update_order_book()
        self.update_trade_log()

    def place_order(self):
        try:
            order_id = int(self.order_id_entry.get())
            trader_id = int(self.trader_id_entry.get())
            order_type = self.order_type_var.get()
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())

            self.engine.place_order(order_id, trader_id, order_type, price, quantity)
            self.update_order_book()
            self.update_trade_log()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_market_data(self):
        """Update market data from the trading engine."""
        try:
            price = self.engine.fetch_live_data(self.ticker)
            self.price_label.config(text=f"${price:.2f}")
            self.root.after(60000, self.update_market_data)  # Update every minute
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch market data: {e}")

    def update_order_book(self):
        """Update the order book display."""
        self.buy_order_list.delete(0, tk.END)
        self.sell_order_list.delete(0, tk.END)

        for order in self.engine.order_book.buy_orders:
            self.buy_order_list.insert(tk.END, str(order))

        for order in self.engine.order_book.sell_orders:
            self.sell_order_list.insert(tk.END, str(order))

    def update_trade_log(self):
        """Update the trade log display."""
        self.trade_log.delete(0, tk.END)

        for trade in self.engine.get_trade_log():
            trade_details = f"Order ID: {trade['order_id']}, Trader ID: {trade['trader_id']}, Type: {trade['order_type']}, Price: {trade['trade_price']}, Quantity: {trade['quantity']}"
            self.trade_log.insert(tk.END, trade_details)

if __name__ == '__main__':
    root = tk.Tk()
    gui = TradingGUI(root)
    root.mainloop()
