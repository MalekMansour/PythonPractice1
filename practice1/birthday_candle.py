'''
You are in charge of the cake for a child's birthday. 
You have decided the cake will have one candle for each year of their total age. 
They will only be able to blow out the tallest of the candles. 
Count how many candles are tallest.
'''

def birthdayCakeCandles(candles):
    # Find the maximum height of candles
    max_height = max(candles)

    # Count the occurrences of the maximum height in the list
    tallest_candles_count = candles.count(max_height)

    return tallest_candles_count

# Example:
candles = [4, 4, 1, 3]
result = birthdayCakeCandles(candles)
print(result)
