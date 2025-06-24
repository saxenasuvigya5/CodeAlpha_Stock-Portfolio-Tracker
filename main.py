# portfolio.py

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 320,
    "AMZN": 125
}

def get_user_portfolio():
    portfolio = {}
    print("📈 Enter your stock holdings (type 'done' to finish):")
    while True:
        stock = input("Stock symbol (e.g., AAPL): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("⚠️ Stock not found in the price list.")
            continue
        try:
            quantity = int(input(f"Quantity of {stock}: "))
            if quantity < 0:
                print("❌ Quantity cannot be negative.")
                continue
            portfolio[stock] = quantity
        except ValueError:
            print("❌ Please enter a valid number.")
    return portfolio

def calculate_total_investment(portfolio):
    total = 0
    for stock, qty in portfolio.items():
        total += stock_prices[stock] * qty
    return total

def display_portfolio(portfolio, total):
    print("\n📊 Your Portfolio Summary:")
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = qty * price
        print(f"{stock}: {qty} shares x ${price} = ${value}")
    print(f"\n💰 Total Investment: ${total}")

def save_to_file(portfolio, total, filename):
    ext = filename.split(".")[-1]
    try:
        with open(filename, "w") as f:
            if ext == "csv":
                f.write("Stock,Quantity,Price,Value\n")
                for stock, qty in portfolio.items():
                    price = stock_prices[stock]
                    value = qty * price
                    f.write(f"{stock},{qty},{price},{value}\n")
                f.write(f",,,Total,{total}\n")
            else:
                f.write("Stock Portfolio Summary\n")
                for stock, qty in portfolio.items():
                    price = stock_prices[stock]
                    value = qty * price
                    f.write(f"{stock}: {qty} x ${price} = ${value}\n")
                f.write(f"\nTotal Investment: ${total}")
        print(f"✅ Portfolio saved to '{filename}'")
    except Exception as e:
        print(f"❌ Failed to save file: {e}")

def main():
    portfolio = get_user_portfolio()
    total = calculate_total_investment(portfolio)
    display_portfolio(portfolio, total)

    save_choice = input("\nDo you want to save the result to a file? (yes/no): ").strip().lower()
    if save_choice == "yes":
        filename = input("Enter filename (e.g., result.txt or result.csv): ").strip()
        save_to_file(portfolio, total, filename)

if __name__ == "__main__":
    main()
