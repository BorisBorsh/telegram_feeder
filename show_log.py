import subprocess


def get_feed_log():
    """Show the last 10 feeding times from log"""
    LOG_FILE_NAME = 'feeder.log'
    try:
        last_ten_log_messages = subprocess.check_output(["tail", LOG_FILE_NAME],
                                                universal_newlines=True)
    except:
        return 'Fail to get log.'

    return last_ten_log_messages
