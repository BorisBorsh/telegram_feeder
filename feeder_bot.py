import requests
import servo
import current_date_time
import temperature


from telegram_config import telegram_bot_token, telegram_api_url
from time import sleep

last_update_id = 0


#
#from feeder_functions import feed_pet, log_feeding_time, 
from feeder_functions import show_log


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
        parameters = (chat_id, message)
        
        run_command(chat_id, message)




def run_command(chat_id, command):
    """Perform recieved commands."""
    if command == '/feed':
        servo.feed_pet()
        send_text(chat_id, 'I fed pets, master!')
    elif command == '/test':
        send_text(chat_id, 'Hello! I am feeder bot and I can read ya!')
    elif command == '/temp':
        temp_message = temperature.get_temp_message()
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
        url = telegram_api_url + telegram_bot_token + '/sendMessage'
        requests.post(url, data=data)
    except:
        print('Send message error.')


if __name__ == '__main__':
    
    FEEDING_SCHEDULE = ['10:30', '12:00', '16:00', '17:00']
    
    CHECK_UPDATES_INTERVAL_SEC = 3
    
    while True:
        try:
            check_updates()
            current_time = current_date_time.get_time()

            if current_time in FEEDING_SCHEDULE:
                servo.feed_pet()
                current_date_time = current_date_time.get_date_time()
                try:
                    send_text(chat_id, str(current_date_time) +
                                      ' - Pets were fed automatically.')
                except:
                    print('Send messege error after auto feed.')
                sleep(60)
            sleep(CHECK_UPDATES_INTERVAL_SEC)

        except KeyboardInterrupt:
            print('Aborted by user.')
            break
