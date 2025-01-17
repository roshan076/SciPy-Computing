def add_time(start, duration, day = None):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    periods = ['AM', 'PM']
    
    # Split the start time and period
    start_time, start_period = start.split()

    # Split time into hours and minutes
    hours, minutes = map(int, start_time.split(':'))
    dur_hours, dur_minutes = map(int, duration.split(':'))
    
    # Calculate the new time
    total_minutes = minutes + dur_minutes
    new_minutes = total_minutes % 60
    additional_hours = total_minutes // 60

    total_hours = hours + dur_hours + additional_hours
    new_hours = total_hours % 12
    period_count = total_hours // 12

    if new_hours == 0:
        new_hours = 12
    
    new_period = start_period
    if period_count % 2 != 0:
        new_period = periods[periods.index(start_period) - 1]

    new_time = f'{new_hours}:{new_minutes:02d} {new_period}'

    #Calculate the new day
    days_later =  total_hours // 24

    if start_period == 'PM' and new_period == 'AM':
        days_later += 1

    if day:
        day = day.lower().capitalize()
        new_day_index = (days.index(day) + days_later) % 7
        new_day = days[new_day_index]
        new_time += f", {new_day}"

    if days_later == 1:
        new_time += ' (next day)'

    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
    

# Examples:
print('Start time: 3:00 PM, Duration: 3:10')
print(add_time('3:00 PM', '3:10'))  
# Returns: 6:10 PM

print('\nStart time: 11:30 AM, Duration: 2:32, Day: Monday')
print(add_time('11:30 AM', '2:32', 'Monday'))  
# Returns: 2:02 PM, Monday

print('\nStart time: 11:43 AM, Duration: 00:20')
print(add_time('11:43 AM', '00:20'))  
# Returns: 12:03 PM

print('\nStart time: 10:10 PM, Duration: 3:30')
print(add_time('10:10 PM', '3:30'))  
# Returns: 1:40 AM (next day)

print('\nStart time: 11:43 PM, Duration: 24:20, Day: tueSday')
print(add_time('11:43 PM', '24:20', 'tueSday'))  
# Returns: 12:03 AM, Thursday (2 days later)

print('\nStart time: 6:30 PM, Duration: 205:12')
print(add_time('6:30 PM', '205:12'))  
# Returns: 7:42 AM (9 days later)
