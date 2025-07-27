'''
Sloth's Meal Time
Sloth is a very habitual person. He eats breakfast at 7:00 a.m. each morning,
lunch at 12:00 p.m. and dinner at 7:00 p.m. in the evening.

Create a function that takes in the current time as a string and determines the
duration of time before Sloth's next meal.

Represent this as an array with the first and second elements representing hours
and minutes, respectively.

Examples
timeToEat("2:00 p.m.")
#5 hours until the next meal, dinner
output = [5, 0]

timeToEat("5:50 a.m.")
# 1 hour and 10 minutes until the next meal, breakfast
output = [1, 10]
'''
# Meals in minutes
BREAKFAST=7*60
LUNCH=12*60
DINNER=19*60

def time_encoder(time_str):
    time_part, meridian = time_str.strip().split(" ")
    hour_str, minute_str = time_part.split(":")
    hour = int(hour_str)
    minute = int(minute_str)
    meridian = meridian.lower()
    if meridian == "p.m." and hour != 12:
        hour += 12
    elif meridian == "a.m." and hour == 12:
        hour = 0
    return hour*60 + minute

def time_difference(current_minutes, meal_minutes):
    diff = meal_minutes - current_minutes
    if diff < 0:
        diff += 24 * 60
    hours = diff // 60
    minutes = diff % 60
    return [hours, minutes]

def timeToEat(s: str) -> list:
    if not s:
        return []
    current_time = time_encoder(s)
    if current_time < BREAKFAST:
        return time_difference(current_time, BREAKFAST)
    elif current_time < LUNCH:
        return time_difference(current_time, LUNCH)
    elif current_time < DINNER:
        return time_difference(current_time, DINNER)
    else:
        return time_difference(current_time, BREAKFAST + 24 * 60)

test_cases = {
    "12:00 a.m.": [7, 0],     # Midnight → until breakfast
    "6:59 a.m.": [0, 1],      # Just before breakfast
    "7:00 a.m.": [5, 0],      # Exactly breakfast time → until lunch
    "11:59 a.m.": [0, 1],     # Just before lunch
    "12:00 p.m.": [7, 0],     # Lunch → until dinner
    "6:59 p.m.": [0, 1],      # Just before dinner
    "7:00 p.m.": [12, 0],     # Dinner → until next day breakfast
    "11:59 p.m.": [7, 1],     # One minute to midnight → until breakfast
    "1:00 a.m.": [6, 0],      # After midnight → until breakfast
    "8:30 a.m.": [3, 30],     # Between breakfast and lunch
    "1:15 p.m.": [5, 45],     # After lunch → until dinner
    "10:00 p.m.": [9, 0],     # Night → until breakfast
    "12:01 a.m.": [6, 59],    # Just after midnight → until breakfast
    "12:00 p.m.": [7, 0],     # Exactly lunch time
    "7:00 a.m.": [5, 0],      # Breakfast just ended → until lunch
}

for time_str, expected in test_cases.items():
    result = timeToEat(time_str)
    print(f"timeToEat('{time_str}') = {result} | {'OK' if result == expected else 'NO Expected: ' + str(expected)}")
