"""
You are in charge of the cake for a child's birthday. 
You have decided the cake will have one candle for each year of their total age. 
They will only be able to blow out the tallest of the candles. 
Count how many candles are tallest.
"""

def birthdayCakeCandles(candles):
    # Write your code here
    tallest = 0
    for n in candles:
        if n > tallest:
            tallest = n
    return candles.count(tallest)
