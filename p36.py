import pandas as pd

# Load stock data from CSV file
data = pd.read_csv('stock_data.csv')  # Replace with your data source

# Extract the closing prices
closing_prices = data['ClosingPrice']

# Calculate the standard deviation of stock prices
std_deviation = closing_prices.std()

# Provide insights based on standard deviation
print("Stock Price Variability Analysis:")
print("---------------------------------")
print(f"Standard Deviation of Prices: {std_deviation:.2f}")

if std_deviation < 10:
    print("Low variability: The stock's price movements are relatively stable.")
elif std_deviation < 20:
    print("Moderate variability: The stock's price movements show moderate fluctuation.")
else:
    print("High variability: The stock's price movements are highly volatile.")

# Analyze price movements based on first and last closing prices
first_price = closing_prices.iloc[0]
last_price = closing_prices.iloc[-1]

print("\nPrice Movement Trends:")
print("-----------------------")
if first_price == last_price:
    print("The stock price hasn't changed over the specified period.")
elif first_price < last_price:
    print("The stock price has generally increased over the specified period.")
else:
    print("The stock price has generally decreased over the specified period.")
