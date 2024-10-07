import datetime


def get_next_day(input_date: datetime.date) -> datetime.date:
    """
    Given a date object, returns the next day as a date object.
    """
    return input_date + datetime.timedelta(days=1)


def get_previous_trading_day(date_str: str) -> str:
    # Parse the input date string into a datetime object
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")

    # Subtract one day to start
    previous_day = date_obj - datetime.timedelta(days=1)

    # If the previous day is Sunday, subtract one more day to get to Saturday
    if previous_day.weekday() == 6:  # Sunday
        previous_day -= datetime.timedelta(days=1)

    # If the now-updated previous day is Saturday, subtract one more day to get to Friday
    if previous_day.weekday() == 5:  # Saturday
        previous_day -= datetime.timedelta(days=1)

    # Convert the datetime object back to the desired string format
    return previous_day.strftime("%Y-%m-%d")


def get_next_trading_day(date_str: str) -> str:
    # Parse the input date string into a datetime object
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    # Add one day to start
    next_day = date_obj + datetime.timedelta(days=1)

    # If the next day is Saturday, add two days to get to Monday
    if next_day.weekday() == 5:  # Saturday
        next_day += datetime.timedelta(days=2)

    # If the now-updated next day is Sunday, add one more day to get to Monday
    if next_day.weekday() == 6:  # Sunday
        next_day += datetime.timedelta(days=1)

    # Convert the datetime object back to the desired string format
    return next_day.strftime("%Y-%m-%d")


def datetime_to_iso8601(date):
    return date.strftime("%Y-%m-%dT%H:%M:%SZ")
