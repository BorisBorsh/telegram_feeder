import send_message
import show_log
import temperature


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

        else:
            send_message.send_text(chat_id, 'I dont get it.')

    else:
        unauthorized_user_message = 'Unauthorized user ' + str(chat_id)
        send_message.send_text(BORSH_ID, unauthorized_user_message)