import yfinance as yf

# Define the ticker symbol for Reliance Industries
ticker = 'RELIANCE.NS'  # '.NS' is used for NSE (National Stock Exchange of India)

# Define the start and end dates
start_date = '2010-01-01'
end_date = '2019-12-31'

# Download the data from Yahoo Finance
data = yf.download(ticker, start=start_date, end=end_date)

# Modify the date column to show only the date (without time)
data.index = data.index.date

# Save the data to a CSV file
csv_filename = f'{ticker}.csv'
data.to_csv(csv_filename)

print(f"Data for {ticker} from {start_date} to {end_date} has been saved to {csv_filename}")
