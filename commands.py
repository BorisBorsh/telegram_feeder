import send_message
import show_log
import temperature
import motor
import user_authentication


def run_command(chat_id, command):
    """Perform recieved commands."""
    if user_authentication.user_in_authorized_user_chad_id_list(chat_id):

        if command == '/feed':
            motor.dispence_food()
            send_message.send_text(chat_id, 'I fed pets, master!')
            return True

        elif command == '/help':
            help_message = ''
            help_message += '/feed - feed pets out of schedule'
            help_message += '\n/temp - get temperature readings'
            help_message += '\n/log - last 10 log messages of feeding'
            #help_message += '\n/schl - show schedule and portions'
            send_message.send_text(chat_id, help_message)
            return True

        elif command == '/temp':
           tempereture_message = temperature.get_tempereture_message()
           send_message.send_text(chat_id, tempereture_message)
           return True

        elif command == '/log':
            last_ten_log_messages = show_log.get_feed_log()
            send_message.send_text(chat_id, last_ten_log_messages)
            return True

        else:
            send_message.send_text(chat_id, 'I dont get it.')
            return True

    else:
        return
