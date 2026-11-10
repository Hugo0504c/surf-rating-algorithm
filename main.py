
print("----------Surf Wave Algorithm----------")

# Define functions for data collection and processing
def ask_num(message):
    while True:
        try:
            num = float(input(message))
            return num
        except ValueError:
            print("Error: please enter a number (e.g. 3.5)")


def ask_str(message):
    string = input(message).strip().lower()
    while string not in ["on", "of", "ot"]:
        print("Error: please enter a valid value (on, of, ot)")
        string = input(message).strip().lower()
    return string


def rate_conditions(height, period, speed, direction):
    # 1. Wave height score (ft)
    if height < 2:
        height_score = 1
    elif height < 3:
        height_score = 5
    elif height < 6:
        height_score = 9
    elif height < 10:
        height_score = 7
    else:
        height_score = 3

    # 2. Wave period score (s)
    if period < 6:
        period_score = 2
    elif period < 9:
        period_score = 5
    elif period < 12:
        period_score = 8
    else:
        period_score = 10

    # 3. Wind speed score (kn)
    if speed < 5:
        wind_score = 10
    elif speed < 10:
        wind_score = 6
    elif speed < 15:
        wind_score = 3
    else:
        wind_score = 1

    # 4. Wind direction adjusts the wind score
    if direction == "of":
        wind_score = wind_score * 1
    elif direction == "ot":
        wind_score = wind_score * 0.8
    else:
        wind_score = wind_score * 0.5

    # 5. Weighted average: height 40%, period 30%, wind 30%
    score = height_score * 0.4 + period_score * 0.3 + wind_score * 0.3

    # Keep the score between 1 and 10
    score = max(1, min(10, score))
    return round(score, 1)


# Ask for the different variables using the previous scripted functions
wave_height = ask_num("Introduce wave height (ft): ")
wave_period = ask_num("Introduce wave period (s): ")
wind_speed = ask_num("Introduce wind speed (kn): ")
print("of: offshore, on: onshore, ot: other")
wind_direction = ask_str("Introduce wind direction: ")

# Rate the conditions and show the result
score = rate_conditions(wave_height, wave_period, wind_speed, wind_direction)
print(f"\nScore: {score}/10")

if score >= 8:
    print("Epic day, go surf!")
elif score >= 6:
    print("Good day, worth it.")
elif score >= 4:
    print("Surfable, but nothing special.")
else:
    print("Stay at home.")
