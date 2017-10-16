import requests

from config import token, url
from time import sleep
from feeder_functions import feed_pet, log_feeding_time, get_time
from feeder_functions import get_date_time, get_temp, show_log


# Time interval for checking_updates().
check_updates_interval = 3
# Store updates id.
offset = 0
# Feeding schedule.
feeding_time = ('07:46', '13:14', '16:00', '17:33')


def check_updates():
    """Cheking new incoming messages."""
    global offset
    global chat_id
    data = {'offset': offset + 1, 'limit': 5, 'timeout': 0}

    try:
        request = requests.post(url + token + '/getUpdates', data=data)
    except:
        print('Error getting updates.')

    if not request.status_code == 200:
        print('Server connection error')

    if not request.json()['ok']:
        print('JSON request fail.')

    for update in request.json()['result']:
        offset = update['update_id']
        chat_id = update['message']['chat']['id']
        message = update['message']['text']
        parameters = (chat_id, message)

        run_command(*parameters)


def run_command(chat_id, command):
    """Perform recieved commands."""
    if command == '/feed':
        feed_pet(servo_rotate_time=3)
        current_date_time = get_date_time()
        log_feeding_time(current_date_time)
        send_text(chat_id, 'I fed pets, master!')
    elif command == '/test':
        send_text(chat_id, 'Hello! I am feeder bot and I can read ya!')
    elif command == '/temp':
        temp_message = get_temp()
        send_text(chat_id, temp_message)
    elif command == '/log':
        timings_message = show_log()
        print(timings_message)
        send_text(chat_id, timings_message)
    else:
        send_text(chat_id, 'I dont get it.')


def send_text(chat_id, text):
    """Sending text message."""
    data = {'chat_id': chat_id, 'text': text}
    try:
        requests.post(url + token + '/sendMessage', data=data)
    except:
        print('Send message error.')


if __name__ == '__main__':
    while True:
        try:
            check_updates()
            current_time = get_time()
            current_date_time = get_date_time()

            if current_time in feeding_time:
                feed_pet()
                try:
                    send_text(chat_id, str(current_date_time) +
                              ' - Pets were fed automatically.')
                except:
                    print('Send messege error after auto feed.')
                log_feeding_time(current_date_time)
                sleep(60)

            sleep(check_updates_interval)

        except KeyboardInterrupt:
            print('Aborted by user.')
            break
