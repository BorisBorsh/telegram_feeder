import requests
import current_date_time
import send_message
import portions_at_schedule
import motor
import show_schedule
import check_updates

from telegram_config import AUTHORIZED_USER_CHAT_ID_LIST, BORSH_ID
from time import sleep


last_update_id = 0

FEEDING_SCHEDULE = ['07:00', '13:00', '19:30']
PORTIONS_TO_DISPENCE = [2, 1, 2]
portions_on_schedule_dict = portions_at_schedule.create_portions_on_schedule_dict(FEEDING_SCHEDULE, PORTIONS_TO_DISPENCE)


if __name__ == '__main__':

    CHECK_UPDATES_INTERVAL_SEC = 3

    while True:
        try:
            response, last_update_id = check_updates.check_updates_method_post(last_update_id)
            if response:
                parse_response_and_run_command(response)

            current_time = current_date_time.get_time()

            if current_time in FEEDING_SCHEDULE:

                motor.dispence_food(portions_to_dispence=portions_on_schedule_dict[current_time])
                current_date_time_info = current_date_time.get_date_time()
                send_message.send_text_to_all_users('Pets were fed ' + str(current_date_time_info) + ' automatically.')
                sleep(60)

            sleep(CHECK_UPDATES_INTERVAL_SEC)

        except KeyboardInterrupt:
            print('Aborted by user.')
            break
