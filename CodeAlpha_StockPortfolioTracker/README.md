# CodeAlpha Stock Portfolio Tracker

A simple Python-based Stock Portfolio Tracker that allows users to manage their stock investments, calculate the total value of their portfolio, and save portfolio details to a CSV file.

## Project Overview

This project was developed as part of the CodeAlpha Python Programming Internship.

The Stock Portfolio Tracker allows users to select stocks from a predefined list, enter the quantity of shares they own, and calculate the total investment value based on manually defined stock prices.

## Features

- Displays a list of available stocks and their prices.
- Allows users to add multiple stocks to their portfolio.
- Accepts stock quantities from users.
- Validates stock symbols and quantity inputs.
- Calculates the investment value of each stock.
- Displays the total portfolio investment value.
- Saves portfolio details to a CSV file.

## Technologies Used

- Python 3
- CSV module
- VS Code

## Available Stocks

The program currently supports the following stocks:

| Stock Symbol | Price |
|---|---:|
| AAPL | $180.00 |
| TSLA | $250.00 |
| GOOGL | $140.00 |
| MSFT | $420.00 |
| AMZN | $190.00 |

*Note: These are manually defined sample prices and are not live stock market prices.*

## Project Structure

```text
CodeAlpha_StockPortfolioTracker/
│
├── stock_tracker.py
├── README.md
└── portfolio.csv  (generated when saving a portfolio)
```

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/adekeyeomowumi65-tech/CodeAlpha_StockPortfolioTracker.git
```

2. Navigate into the project folder:

```bash
cd CodeAlpha_StockPortfolioTracker
```

3. Run the Python program:

```bash
python stock_tracker.py
```

## How to Use

1. Run the program.
2. View the available stocks and their prices.
3. Enter a stock symbol.
4. Enter the quantity of shares you want to track.
5. Repeat for additional stocks.
6. Type `done` when you have finished adding stocks.
7. View your portfolio summary and total investment value.
8. Choose whether to save your portfolio as a CSV file.

## Concepts Practiced

- Python dictionaries
- Functions
- Loops and conditional statements
- User input and data validation
- Exception handling
- File handling
- CSV file operations

## Internship

**Program:** CodeAlpha Python Programming Internship

**Project:** Stock Portfolio Tracker

**GitHub:** [adekeyeomowumi65-tech](https://github.com/adekeyeomowumi65-tech)

---

Developed as part of my Python programming learning journey.