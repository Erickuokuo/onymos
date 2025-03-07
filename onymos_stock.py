import threading
import random
import time
# Eric Kuo
class Order
    def __init__(self, order_type, ticker, quantity, price):
        self.order_type = order_type  
        self.ticker = ticker
        self.quantity = quantity
        self.price = price

class OrderBook:
    def __init__(self):
        self.buy_orders = []  
        self.sell_orders = []  
        self.lock = threading.Lock() 

    def addOrder(self, order):
        with self.lock:
            if order.order_type == 'Buy':
                self._insert_order(self.buy_orders, order, desc=True)
            else:
                self._insert_order(self.sell_orders, order, desc=False)

    def _insert_order(self, order_list, order, desc):
        i = len(order_list) - 1
        while i >= 0 and ((desc and order_list[i].price < order.price) or (not desc and order_list[i].price > order.price)):
            i -= 1
        order_list.insert(i + 1, order)

    def matchOrder(self):
        with self.lock:
            buy_index, sell_index = 0, 0

            while buy_index < len(self.buy_orders) and sell_index < len(self.sell_orders):
                buy_order = self.buy_orders[buy_index]
                sell_order = self.sell_orders[sell_index]

                if buy_order.ticker == sell_order.ticker and buy_order.price >= sell_order.price:
                    trade_quantity = min(buy_order.quantity, sell_order.quantity)
                    print(f"Trade executed: {trade_quantity} shares of {buy_order.ticker} at {sell_order.price}")

                    # Update quantities
                    buy_order.quantity -= trade_quantity
                    sell_order.quantity -= trade_quantity
                    if buy_order.quantity == 0:
                        buy_index += 1
                    if sell_order.quantity == 0:
                        sell_index += 1
                else:
                    if buy_order.ticker < sell_order.ticker:
                        buy_index += 1
                    else:
                        sell_index += 1

            self.buy_orders = self.buy_orders[buy_index:]
            self.sell_orders = self.sell_orders[sell_index:]

stop_simulation = False

def simulate_orders(order_book, tickers):
    while not stop_simulation:
        order_type = random.choice(['Buy', 'Sell'])
        ticker = random.choice(tickers)
        quantity = random.randint(1, 100)
        price = random.randint(1, 1000)
        order = Order(order_type, ticker, quantity, price)
        order_book.addOrder(order)
        order_book.matchOrder()  
        time.sleep(random.uniform(0.1, 0.5))

# Main function
if __name__ == "__main__":
    tickers = ["APPLE", "TSLA"] 
    order_book = OrderBook()

    threads = []
    for _ in range(2):  # 2 threads
        thread = threading.Thread(target=simulate_orders, args=(order_book, tickers))
        thread.start()
        threads.append(thread)

    # Run the simulation for 10 seconds
    simulation_duration = 10  
    print(f"Simulation running for {simulation_duration} seconds...")
    time.sleep(simulation_duration)

    stop_simulation = True
    print("Stopping simulation...")

    for thread in threads:
        thread.join()

    print("Simulation stopped.")