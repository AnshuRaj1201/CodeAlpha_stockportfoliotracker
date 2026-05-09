# ============================================
# Stock Portfolio Tracker
# ============================================

# --- 1. Our stock price database ---
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 185,
    "MSFT": 420
}

print("=== Stock Portfolio Tracker ===")
print("Available stocks:", list(stock_prices.keys()))
print()

# --- 2. Collect user input ---
portfolio = {}

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print(f"  ⚠ '{stock}' not found. Available: {list(stock_prices.keys())}\n")
        continue
    
    quantity = int(input(f"  How many shares of {stock}? "))
    portfolio[stock] = quantity
    print()

# --- 3. Calculate and display ---
if not portfolio:
    print("No stocks entered. Goodbye!")
else:
    print("\n--- Portfolio Summary ---")
    total = 0
    
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total += value
        print(f"  {stock:6s}: {quantity:3d} shares × ${price:>6} = ${value:>8,}")
    
    print(f"\n  Total Portfolio Value: ${total:,}")
    
    # --- 4. Save to file ---
    save = input("\nSave results to file? (yes/no): ").lower()
    
    if save == "yes":
        with open("portfolio.txt", "w") as f:
            f.write("Portfolio Summary\n")
            f.write("=" * 30 + "\n")
            for stock, quantity in portfolio.items():
                value = stock_prices[stock] * quantity
                f.write(f"{stock}: {quantity} shares = ${value}\n")
            f.write(f"Total: ${total}\n")
        print("✓ Saved to portfolio.txt")