def get_schedule_message(FEEDING_SCHEDULE):
    """Show current feeding schedule"""
    message = ''
    for time in FEEDING_SCHEDULE:
        message += ' ' + time + ','
    
    return 'Schedule: {}.'.format(message[:-1])
