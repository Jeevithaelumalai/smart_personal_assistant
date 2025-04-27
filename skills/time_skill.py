from datetime import datetime

def get_time():
    """Returns current time"""
    return f"The current time is {datetime.now().strftime('%H:%M')}"

def get_date():
    """Returns current date"""
    return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}"