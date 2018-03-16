import requests
import current_date_time
import send_message
import portions_at_schedule
import temperature
import motor
import show_log
import show_schedule
import commands

from telegram_config import TELEGRAM_BOT_TOKEN, TELEGRAM_API_URL
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
        url = TELEGRAM_API_URL + TELEGRAM_BOT_TOKEN + '/getUpdates'
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

        if message == '/schl':
            schedule_message = show_schedule.get_schedule_and_portions_message(portions_on_schedule_dict)
            send_message.send_text(chat_id, schedule_message)
        else:
            commands.run_command(chat_id, message)


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
