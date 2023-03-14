# Zigzag-Recursive
Python version of  Recursive Zigzag pine script indicator
This script imports necessary libraries (ccxt, pandas, numpy, and a custom zigzag module) and fetches historical OHLC data for the BTC/USDT trading pair from Binance using the CCXT library. Then it calculates the ZigZag pivots and trend direction using a recursive approach with a custom recursive_zigzag function.

The main steps of the script are:

Define the CCXT exchange and trading pair symbol (BTC/USDT in this case).
Fetch the OHLC data using CCXT and store it in a pandas DataFrame.
Define the recursive_zigzag function, which calculates ZigZag pivots and trend direction using a recursive approach.
Calculate the ZigZag pivots and trend direction for the OHLC data with the recursive_zigzag function.
Display the results in a DataFrame.
When run, this script will fetch historical OHLC data for the specified trading pair, calculate the ZigZag pivots and trend direction using a recursive approach, and print the results in a DataFrame with columns for timestamp, open, high, low, close, pivots, and trend direction.

Please note that you'll need to have the custom zigzag module available in your working environment. You can create a file named zigzag.py and put the previously provided ZigZag indicator function in there.
