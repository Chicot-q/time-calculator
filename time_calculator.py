def add_time(start, duration, day_of_the_week=None):
    end_day = None

    time_part, am_pm = start.split()
    hours_start, minutes_start = map(int, time_part.split(':'))
    hours_duration, minutes_duration = map(int, duration.split(':'))

    if am_pm == 'PM' and not hours_start == 12:
        hours_start += 12    
    if am_pm == 'AM' and hours_start == 12:
        hours_start = 0
    
    total_minutes_start = hours_start * 60 + minutes_start
    total_minutes_duration = hours_duration * 60 + minutes_duration
    total_minutes = total_minutes_start + total_minutes_duration

    minutes_in_day = 1440
    final_days = total_minutes // 1440
    final_hours = int((total_minutes % 1440) / 60)
    final_minutes = (total_minutes % 1440) % 60

    am_pm = 'PM' if final_hours >= 12 else 'AM'
    final_hours %= 12

    final_hours = 12 if final_hours == 0 else final_hours
        
    if day_of_the_week:
        day_of_the_week = day_of_the_week.capitalize()
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        number_of_day = week.index(day_of_the_week)
        end_day = week[(number_of_day + final_days) % 7]
        
    new_time = f'{final_hours}:{final_minutes:02d} {am_pm}'

    if end_day:
        new_time += f', {end_day}'
    if final_days == 1:
        new_time += f' (next day)'
    if final_days > 1:
        new_time += f' ({final_days} days later)'

    return new_time

print(add_time())
