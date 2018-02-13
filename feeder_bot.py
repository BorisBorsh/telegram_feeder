import requests
import current_date_time
import send_message
import portions_at_schedule
import temperature
import motor
import show_log
import show_schedule

from telegram_config import telegram_bot_token, telegram_api_url
from telegram_config import AUTHORIZED_USER_CHAT_ID_LIST, BORSH_ID
from time import sleep


last_update_id = 0

FEEDING_SCHEDULE = ['07:00', '13:00', '19:30']
PORTIONS_TO_DISPENCE = [2, 1, 2]
portions_on_schedule_dict = portions_at_schedule.create_portions_on_schedule_dict(FEEDING_SCHEDULE, PORTIONS_TO_DISPENCE)


def check_updates():
    """Cheking new incoming messages."""
    global last_update_id
    global chat_id
    data = {'offset': last_update_id + 1, 'limit': 5, 'timeout': 0}

    try:
        url = telegram_api_url + telegram_bot_token + '/getUpdates'
        response = requests.post(url, data=data)
    except:
        print('Error getting updates.')
        return

    if not response.status_code == 200:
        print('Server connection error')
        return

    for update in response.json()['result']:
        last_update_id = update['update_id']
        chat_id = update['message']['chat']['id']
        message = update['message']['text']

        run_command(chat_id, message)



def run_command(chat_id, command):
    """Perform recieved commands."""
    if chat_id in AUTHORIZED_USER_CHAT_ID_LIST:

        if command == '/feed':
            motor.dispence_food()
            send_message.send_text(chat_id, 'I fed pets, master!')

        elif command == '/help':
            help_message = ''
            help_message += '/feed - feed pets out of schedule'
            help_message += '\n/temp - get temperature readings'
            help_message += '\n/log - last 10 log messages of feeding'
            help_message += '\n/schl - show schedule and portions'
            send_message.send_text(chat_id, help_message)

        elif command == '/temp':
           tempereture_message = temperature.get_tempereture_message()
           send_message.send_text(chat_id, tempereture_message)

        elif command == '/log':
            last_ten_log_messages = show_log.get_feed_log()
            send_message.send_text(chat_id, last_ten_log_messages)

        elif command == '/schl':
            schedule_message = show_schedule.get_schedule_and_portions_message(portions_on_schedule_dict)
            send_message.send_text(chat_id, schedule_message)

        else:
            send_message.send_text(chat_id, 'I dont get it.')

    else:
        unauthorized_user_message = 'Unauthorized user ' + str(chat_id)
        send_message.send_text(BORSH_ID, unauthorized_user_message)


if __name__ == '__main__':

    CHECK_UPDATES_INTERVAL_SEC = 3

    while True:
        try:
            check_updates()
            current_time = current_date_time.get_time()

            if current_time in FEEDING_SCHEDULE:

                motor.dispence_food(portions_to_dispence=portions_on_schedule_dict[current_time])
                current_date_time_info = current_date_time.get_date_time()

                try:
                    send_message.send_text_to_all_users('Pets were fed ' + str(current_date_time_info) + ' automatically.')
                except:
                    print('Send messege error after auto feed.')
                sleep(60)

            sleep(CHECK_UPDATES_INTERVAL_SEC)

        except KeyboardInterrupt:
            print('Aborted by user.')
            break
