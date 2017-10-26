

from collections import deque

#def log_feeding_time(feed_time):
#    """Logging feeding time to console."""
#    message = feed_time + ' - Feeder fed a pet!'
#
#    try:
#        with open(filename, 'a') as f:
#            f.write('\n' + message)
#    except FileNotFoundError:
#        print('File not found!')
#    print(message)


def show_log():
    """Show the last 10 feeding timings from log."""
    with open(filename) as f:
        last_timings = list(deque(f, 10))
        last_timings_message = ''
        for line in last_timings:
            last_timings_message += line
        return last_timings_message
