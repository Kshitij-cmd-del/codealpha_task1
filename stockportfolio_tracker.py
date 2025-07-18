import os

def stock_portfolio_tracker():
    # Hardcoded dictionary to define stock prices
    stock_prices = {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "GOOG": 150.00,
        "MSFT": 220.00,
        "AMZN": 130.00
    }

    portfolio = {}
    total_investment = 0.0

    print("Welcome to the Stock Portfolio Tracker!")
    print("Available stocks and their prices:")
    for stock, price in stock_prices.items():
        print(f"  {stock}: ${price:.2f}")

    while True:
        stock_name = input("\nEnter stock name (or 'done' to finish, 'list' to see available stocks): ").upper()

        if stock_name == 'DONE':
            break
        elif stock_name == 'LIST':
            print("Available stocks and their prices:")
            for stock, price in stock_prices.items():
                print(f"  {stock}: ${price:.2f}")
            continue

        if stock_name not in stock_prices:
            print("Stock not found. Please choose from the available stocks or add it to the hardcoded list.")
            continue

        while True:
            try:
                quantity = int(input(f"Enter quantity for {stock_name}: "))
                if quantity <= 0:
                    print("Quantity must be a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a whole number for quantity.")

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print(f"Added {quantity} shares of {stock_name} to your portfolio.")

    print("\n--- Your Portfolio Summary ---")
    if not portfolio:
        print("Your portfolio is empty.")
    else:
        for stock, quantity in portfolio.items():
            current_price = stock_prices.get(stock, 0)
            value = current_price * quantity
            total_investment += value
            print(f"{stock}: {quantity} shares @ ${current_price:.2f} = ${value:.2f}")
        print(f"\nTotal Investment Value: ${total_investment:.2f}")

    # Optional: Save the result to a file
    save_option = input("\nDo you want to save the portfolio summary to a file? (yes/no): ").lower()
    if save_option == 'yes':
        file_type = input("Enter file type (txt/csv): ").lower()
        if file_type == 'txt':
            filename = "portfolio_summary.txt"
            with open(filename, 'w') as f:
                f.write("--- Stock Portfolio Summary ---\n")
                if not portfolio:
                    f.write("Your portfolio is empty.\n")
                else:
                    for stock, quantity in portfolio.items():
                        current_price = stock_prices.get(stock, 0)
                        value = current_price * quantity
                        f.write(f"{stock}: {quantity} shares @ ${current_price:.2f} = ${value:.2f}\n")
                    f.write(f"\nTotal Investment Value: ${total_investment:.2f}\n")
            print(f"Portfolio summary saved to {os.path.abspath(filename)}")
        elif file_type == 'csv':
            filename = "portfolio_summary.csv"
            with open(filename, 'w') as f:
                f.write("Stock,Quantity,Price,Value\n")
                if portfolio:
                    for stock, quantity in portfolio.items():
                        current_price = stock_prices.get(stock, 0)
                        value = current_price * quantity
                        f.write(f"{stock},{quantity},{current_price:.2f},{value:.2f}\n")
                f.write(f"\nTotal Investment Value,,,{total_investment:.2f}\n")
            print(f"Portfolio summary saved to {os.path.abspath(filename)}")
        else:
            print("Invalid file type. Not saving.")
    else:
        print("Portfolio summary not saved to file.")

if __name__ == "__main__":
    stock_portfolio_tracker()