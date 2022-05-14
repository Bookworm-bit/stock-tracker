import yfinance as yf
import matplotlib.pyplot as plt
import string
import os

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
        profile_navigation = input(
            "What would you like to do with your profile?")
        if profile_navigation == "1":
            print("Portfolio management coming soon!")

    if navigation == "8":
        print("Goodbye!")
        break
