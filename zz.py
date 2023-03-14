import ccxt
import pandas as pd
import numpy as np
from typing import Tuple
from zigzag import zigzag

# Define CCXT exchange and symbol
exchange = ccxt.binance()
symbol = 'BTC/USDT'

# Fetch OHLC data with CCXT
ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1d')
columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
df = pd.DataFrame(ohlcv, columns=columns)
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')


# Define recursive_zigzag function
def recursive_zigzag(df: pd.DataFrame, length: int = 5, depth: int = 200) -> Tuple[np.ndarray, np.ndarray]:
    """
    Returns zigzag pivots and trend direction using recursive approach.

    Parameters:
    df (pd.DataFrame): OHLC data
    length (int): Length of the zigzag
    depth (int): Maximum depth of the zigzag

    Returns:
    tuple of two numpy arrays: Zigzag pivots and trend direction
    """

    # Calculate zigzag pivots and trend direction for each level
    levels = range(depth)
    pivots = np.zeros((len(df), len(levels)))
    trend_direction = np.zeros((len(df), len(levels)))
    for i, level in enumerate(levels):
        deviation = np.std(df['close'] - df['close'].rolling(length).mean())
        deviation *= 2 ** i
        pivots[:, i], trend_direction[:, i] = zigzag(df['close'].values, deviation=deviation)

    # Remove zigzag pivots that are too close to each other
    for i in range(1, len(levels)):
        min_distance = np.std(df['close'] - df['close'].rolling(length).mean())
        min_distance *= 2 ** (i - 1)
        for j in range(1, len(df) - 1):
            if abs(pivots[j, i] - pivots[j - 1, i]) < min_distance:
                pivots[j, i] = pivots[j - 1, i]
                trend_direction[j, i] = trend_direction[j - 1, i]

    return pivots, trend_direction


# Calculate zigzag pivots and trend direction for the OHLC data
length = 5
depth = 200
pivots, trend_direction = recursive_zigzag(df, length=length, depth=depth)

# Display the results in a dataframe
df['pivots'] = pivots[:, -1]
df['trend_direction'] = trend_direction[:, -1]
df = df[['timestamp', 'open', 'high', 'low', 'close', 'pivots', 'trend_direction']]
print(df.head())
