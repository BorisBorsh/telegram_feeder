def create_portions_on_schedule_dict(FEEDING_SCHEDULE, PORTIONS_TO_DISPENCE):
    """Function is generating dictionary where key is time and value
    is portion counter."""
    portions_dict = {}
    for time in FEEDING_SCHEDULE:
        portions_dict[time] = PORTIONS_TO_DISPENCE[FEEDING_SCHEDULE.index(time)]
    return portions_dict
