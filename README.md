# Real-time Stock Trading Engine

This project implements a real-time stock trading engine designed to match stock buy orders with sell orders.

## Features

1. **`addOrder` function**:
   - **Parameters**: 
     - `Order Type` (Buy or Sell)
     - `Ticker Symbol`
     - `Quantity`
     - `Price`
   - **Functionality**: 
     - Supports 1,024 tickers (stocks) being traded.
     - A wrapper function simulates active stock transactions by executing `addOrder` with randomly generated parameter values.

2. **`matchOrder` function**:
   - **Matching Criteria**:
     - A Buy price for a particular ticker must be greater than or equal to the lowest Sell price available.
   - **Concurrency Handling**:
     - Code handles race conditions where multiple threads modify the stock order book, simulating real-life stock transactions handled by multiple stockbrokers.
     - Uses lock-free data structures to manage order matching.

3. **Constraints**:
   - **No Dictionary or Map Usage**: 
     - The implementation avoids using dictionaries, maps, or equivalent data structures that provide dictionary-like functionality (i.e., `import` or `include` constructs relevant to the programming language that provide map or dictionary capabilities).
     - The implementation focuses on custom, lock-free data structures to manage stock orders.

4. **Performance**:
   - The `matchOrder` function is optimized to run with a time complexity of **O(n)**, where `n` is the number of orders in the stock order book.

## Requirements

- **Programming Language**: Choose a language that supports multi-threading and concurrency (e.g., Python, Java, C++).
- **Concurrency**: Proper handling of race conditions without relying on high-level language constructs for data structure management.
- **Lock-Free Data Structures**: Implementation of custom data structures to ensure thread safety.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Erickuokuo/onymos.git
