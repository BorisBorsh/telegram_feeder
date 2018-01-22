def get_schedule_message(FEEDING_SCHEDULE):
    """Show current feeding schedule"""
    msg = ''
    for time in FEEDING_SCHEDULE:
        msg += ' ' + time + ','
    
    return 'Schedule: {}.'.format(msg[:-1])
