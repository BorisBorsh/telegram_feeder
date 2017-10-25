from datetime import datetime


def get_time():
    """Return current time."""
    now = datetime.today()
    return now.strftime('%H:%M')


def get_date_time():
    """Return current date and time."""
    now = datetime.today()
    return now.strftime('%Y-%m-%d %H:%M')

