def add_time(start, duration, day_of_week=None):
    # Days of the week list to handle the day calculation
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Split start time
    start_h = int(start.split(':')[0])
    start_m = int(start.split(':')[1].split()[0])
    start_period = start.split()[1]  # AM or PM

    # Split duration time
    duration_h = int(duration.split(':')[0])
    duration_m = int(duration.split(':')[1])

    # Add minutes and handle overflow
    new_m = start_m + duration_m
    if new_m >= 60:
        duration_h += 1  # Add the extra hour
        new_m -= 60

    # Add hours and handle AM/PM transitions
    new_h = start_h + duration_h
    days_passed = 0  # Count how many days pass

    while new_h >= 12:
        if new_h == 12:
            # Exactly 12 should switch between AM and PM
            if start_period == 'AM':
                start_period = 'PM'
            else:
                start_period = 'AM'
                days_passed += 1  # Add a day when transitioning from PM to AM
            break
        else:
            new_h -= 12
            if start_period == 'AM':
                start_period = 'PM'
            else:
                start_period = 'AM'
                days_passed += 1  # Add a day when transitioning from PM to AM
    
    # Handle the case when the time is exactly 12:00 (midday or midnight)
    if new_h == 0:
        new_h = 12

    # Adjust the day of the week if provided
    if day_of_week:
        day_of_week = day_of_week.capitalize()  # Make input case-insensitive
        start_day_index = days_of_week.index(day_of_week)
        result_day_index = (start_day_index + days_passed) % 7
        result_day = days_of_week[result_day_index]
    else:
        result_day = None

    # Format the new minutes with two digits
    new_m = f'{new_m:02}'

    # Handle "next day" or "n days later" scenarios
    day_result = ''
    if days_passed == 1:
        day_result = ' (next day)'
    elif days_passed > 1:
        day_result = f' ({days_passed} days later)'

    # Build the result
    if result_day:
        final_result = f"{new_h}:{new_m} {start_period}, {result_day}{day_result}"
    else:
        final_result = f"{new_h}:{new_m} {start_period}{day_result}"

    return final_result
