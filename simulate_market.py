from trading_engine import TradingEngine

import random

def simulate_market(engine, num_orders):
    """Simulate market activity with random orders."""
    for _ in range(num_orders):
        order_type = random.choice(['buy', 'sell'])
        price = round(random.uniform(95.0, 105.0), 2)  # Random price between 95 and 105
        quantity = random.randint(1, 10)  # Random quantity between 1 and 10
        order_id = random.randint(1000, 9999)  # Random order ID
        trader_id = random.randint(1, 100)  # Random trader ID

        engine.place_order(order_id, trader_id, order_type, price, quantity)

# Example usage
engine = TradingEngine()
simulate_market(engine, 10)  # Simulate 10 random orders
print(engine)
