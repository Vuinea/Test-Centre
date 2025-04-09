from datetime import datetime, timedelta

def get_friday_of_week():
    today = datetime.now()
    # Get the current weekday (0 = Monday, 6 = Sunday)
    current_weekday = today.weekday()
    # Calculate the number of days until Friday (4 = Friday)
    days_until_friday = 5 - current_weekday
    # If today is after Friday, calculate the Friday of the next week
    if days_until_friday < 0:
        days_until_friday += 7
    # Get the Friday date
    friday = today + timedelta(days=days_until_friday)
    return friday.date()
