def create_portions_on_schedule_dict(FEEDING_SCHEDULE, PORTIONS_TO_DISPENCE):
    """Function is generating dictionary where key is time and value
    is portion counter. For FEEDING_SCHEDULE = ['07:00', '13:00', '19:00'] and
    PORTIONS_TO_DISPENCE = [2, 1, 2] zip function would
    create dict {'07:00' : 2, '13:00' : 1, '19:00' : 2}"""
    portions_dict = dict(zip(FEEDING_SCHEDULE, PORTIONS_TO_DISPENCE))
    return portions_dict
