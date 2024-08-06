from trading_engine import TradingEngine

if __name__ == '__main__':
    # Create an instance of TradingEngine
    engine = TradingEngine()

    # Load historical data for a specific stock ticker
    engine.fetch_live_data('AAPL')  # Fetch live data to initialize current price

    # Simulate trades based on the historical data
    # Uncomment if you have a
