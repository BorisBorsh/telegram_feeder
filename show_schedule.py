import portions_at_schedule


def get_schedule_message(FEEDING_SCHEDULE):
    """Show current feeding schedule"""
    message = ''
    for time in FEEDING_SCHEDULE:
        message += ' ' + time + ','
    
    return 'Schedule: {}.'.format(message[:-1])

def get_schedule_and_portions_message(portions_on_schedule_dict):
    """Show current feeding schedule with assigned portions"""
    message =''
    for key_time in sorted(portions_on_schedule_dict.keys()):
        message += ' ' + key_time + ' (portions - ' + str(portions_on_schedule_dict[key_time]) + '),'
    return 'Schedule: {}.'.format(message[:-1])


if __name__ == '__main__':
    FEEDING_SCHEDULE = ['07:00', '13:00', '19:30']
    PORTIONS_TO_DISPENCE = [2, 1, 2]
    portions_on_schedule_dict = portions_at_schedule.create_portions_on_schedule_dict(FEEDING_SCHEDULE, PORTIONS_TO_DISPENCE)
    print(get_schedule_and_portions_message(portions_on_schedule_dict))
