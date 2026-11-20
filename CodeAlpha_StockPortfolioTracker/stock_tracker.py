
import csv


# Manually defined stock prices
stock_prices = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 420.00,
    "AMZN": 190.00
}


def display_available_stocks():
    """Display available stocks and their prices."""

    print("\nAVAILABLE STOCKS")
    print("-" * 35)

    for stock, price in stock_prices.items():
        print(f"{stock}: ${price:.2f}")

    print("-" * 35)


def add_stock(portfolio):
    """Allow users to add stocks to their portfolio."""

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Stock not found. Please select an available stock.")
            continue

        try:
            quantity = float(input(f"Enter quantity of {stock}: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

        print(f"{quantity:g} shares of {stock} added successfully!")


def display_portfolio(portfolio):
    """Calculate and display the portfolio investment."""

    print("\n" + "=" * 65)
    print("                 STOCK PORTFOLIO SUMMARY")
    print("=" * 65)

    print(f"{'STOCK':<12}{'QUANTITY':<15}{'PRICE':<18}{'VALUE':<15}")
    print("-" * 65)

    total_investment = 0

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment_value = quantity * price

        total_investment += investment_value

        print(
            f"{stock:<12}"
            f"{quantity:<15g}"
            f"${price:<17.2f}"
            f"${investment_value:<14.2f}"
        )

    print("-" * 65)
    print(f"TOTAL INVESTMENT VALUE: ${total_investment:,.2f}")
    print("=" * 65)

    return total_investment


def save_portfolio(portfolio, total_investment):
    """Save portfolio details to a CSV file."""

    filename = "portfolio.csv"

    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Stock",
                "Quantity",
                "Price Per Share",
                "Investment Value"
            ])

            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                value = quantity * price

                writer.writerow([
                    stock,
                    quantity,
                    price,
                    value
                ])

            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total_investment])

        print(f"\nPortfolio successfully saved to {filename}!")

    except OSError as error:
        print(f"Could not save portfolio: {error}")


def main():
    """Main function that runs the stock portfolio tracker."""

    portfolio = {}

    print("=" * 45)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 45)

    display_available_stocks()

    print("\nAdd the stocks you want to track.")
    print("Enter 'done' when you have finished.")

    add_stock(portfolio)

    if not portfolio:
        print("\nNo stocks were added to your portfolio.")
        return

    total_investment = display_portfolio(portfolio)

    save_choice = input("\nWould you like to save your portfolio? (yes/no): ").strip().lower()

    if save_choice in ["yes", "y"]:
        save_portfolio(portfolio, total_investment)
    else:
        print("\nPortfolio was not saved.")

    print("\nThank you for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
