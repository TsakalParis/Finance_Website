import yfinance as yf
import datetime
import pandas as pd



def get_stock_data(tickers, start_date, end_date):
    # Check if all tickers are valid
    for ticker in tickers:
        try:
            yf.Ticker(ticker)
        except:
            return "invalid ticker: {}".format(ticker)

    # Make sure start_date and end_date are in the correct format
    try:
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        return "incorrect date format. Use year-month-day (e.g. 2022-01-31)"

    # Retrieve stock data for each ticker in the given date range
    stock_data = {}
    for ticker in tickers:
        stock_info = yf.Ticker(ticker)
        data = stock_info.history(start=start_date, end=end_date)
        stock_data[ticker] = data
        stock_name = list(stock_data.keys())

    # Check if there is data for all of the tickers for the given date range
    missing_tickers = [ticker for ticker, data in stock_data.items() if data.empty]
    if missing_tickers:
        return "there is no data for the range that you asked for, for the following tickers: {}".format(", ".join(missing_tickers))

    # Return the stock data and date range
    return stock_data[stock_name[0]].head(), stock_data[stock_name[1]].head()

    #for multiple stocks -> for i in stock name: return stock_data[stock_name[i]]
    