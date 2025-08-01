'''
Birthday Cake Candles
You are in charge of the cake for a child's birthday.
It will have one candle for each year of their total age.
They will only be able to blow out the tallest of the candles.

Your task is to count how many candles are the tallest.

Examples
birthdayCakeCandles([4,4,1,3])
output = 2
// The tallest candles are 4. There are 2 candles with this height, so the function should return 2.
birthdayCakeCandles([1, 1, 1, 1])
output = 4
// All candles are the same height, so all are the tallest.
birthdayCakeCandles([])
output = 0
// No candles, so nothing to blow out.
'''
def birthdayCakeCandles(lst: list) -> int:
    if not lst:
        return 0
    max_val=max(lst)
    return lst.count(max_val)

print(birthdayCakeCandles([4,4,1,3])) #2
print(birthdayCakeCandles([1, 1, 1, 1])) #4
print(birthdayCakeCandles([])) #0

