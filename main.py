import yfinance as yf
import matplotlib.pyplot as plt
import string
import os
portfolio_file = open("portfolio.txt", "r+")

while True:
    print("-" * 20)
    print("Welcome to the Stock Market!")
    print("""
    1. Search for a stock
    2. Get info on a stock
    3. Get a stock's historical data
    4. Get a stock's history
    5. Get custom information from a stock
    6. Directory management
    7. Portfolio management
    8. Exit
    """)
    navigation = input("Please enter a number corresponding to an action: ")

    if navigation == "1":
        ticker_input = input("Please enter a ticker: ")

        try:
            ticker = yf.Ticker(ticker_input)
            past_day = ticker.history(period="1d")
            print(f'Regular Market Price: {ticker.info["regularMarketPrice"]}')
            print(f'Last Recorded Value: {past_day["Close"].iloc[-1]}')
        except:
            print('Invalid ticker')

    if navigation == "2":
        ticker_input = input("Please enter a ticker: ")
        ticker = yf.Ticker(ticker_input)
        print(ticker.info)

    if navigation == "3":
        ticker_input = input("Please enter a ticker: ")
        ticker = yf.Ticker(ticker_input)
        print(ticker.history(period="max"))

    if navigation == "4":
        ticker_input = input("Please enter a ticker: ")
        ticker = yf.Ticker(ticker_input)

        ticker.history(period="max")['Close'].plot()
        plt.title(f"{ticker.info['shortName']} Price History")
        plt.show()

    if navigation == "5":
        ticker_input = input("Please enter a ticker: ")
        ticker = yf.Ticker(ticker_input)
        try:
            print("Your options are:")
            print(str(key) for key in ticker.info.keys())
            ticker_option = input("Please enter a ticker option: ")
            print(ticker.info[ticker_option])
        except:
            print("Invalid value or ticker")

    if navigation == "6":
        print("Directory management coming soon!")

    if navigation == "7":
        print("""
        1. Add a stock to your portfolio
        2. Remove a stock from your portfolio
        3. View your portfolio
        4. View your portfolio's value
        5. View your portfolio's growth
        6. View your portfolio's growth over time
        7. View your portfolio's value over time
        8. View your portfolio's value over time (graph)
        9. Clear your portfolio
        """)
        profile_navigation = input(
            "What would you like to do with your profile? Please enter a number corresponding to an action: ")
        if profile_navigation == "1":
            portfolio_file.write(
                f'{input("Please enter a ticker: ")}: {input("Please enter an amount: ")}')

        if profile_navigation == "2":
            removed_stock = input("Please enter the ticker of the stock you would like to remove: ")
            amount = input("Please enter the amount of the stock you would like to remove: ")
            for line in portfolio_file:
                if removed_stock in line:
                    try:
                        int(amount)
                    except:
                        print("Invalid amount")
                    
                    if int(amount) > int(line.split(':')[1].strip()):
                        print("You don't have that much of that stock!")

                    else:
                        portfolio_file.seek(0)
                        portfolio_file.truncate()
                        for line in portfolio_file:
                            if removed_stock not in line:
                                portfolio_file.write(line)
                            if removed_stock in line:
                                portfolio_file.write(
                                    f'{line.split(":")[0]}: {str(int(line.split(":")[1].strip()) - int(amount))}')
                        print("Stock removed!")

        if profile_navigation == "3":
            print("Not implemented yet")

        if profile_navigation == "4":
            print(
                f"Your portfolio's value is: {sum(float(line.split(':')[1]) * yf.Ticker(line.split(':')[0]).info['regularMarketPrice'] for line in portfolio_file)}")

        if profile_navigation == "5":
            print("Not implemented yet")

        if profile_navigation == "6":
            print("Not implemented yet")

        if profile_navigation == "7":
            print("Not implemented yet")

        if profile_navigation == "8":
            print("Not implemented yet")

        if profile_navigation == "9":
            portfolio_file.truncate(0)

    if navigation == "8":
        print("Goodbye!")
        break
