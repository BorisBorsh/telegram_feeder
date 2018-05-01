import current_date_time
import portions_at_schedule
import motor
#import show_schedule
import check_updates
import send_message
import parse_and_run_command

from time import sleep
from proxy_parser import Proxy

CHECK_UPDATES_INTERVAL_SEC = 10

FEEDING_SCHEDULE = ['07:00', '13:00', '19:00']
PORTIONS_TO_DISPENCE = [2, 1, 2]
portions_on_schedule_dict = portions_at_schedule.create_portions_on_schedule_dict(FEEDING_SCHEDULE, PORTIONS_TO_DISPENCE)


def main():
    last_update_id = 0
    proxy = Proxy()
    proxies = proxy.get_availible_proxy_address()

    while True:
        try:
            response, last_update_id, proxies = check_updates.check_updates_method_get(last_update_id, proxies)
            if response.json()['result']:
                parse_and_run_command.parse_response_and_run_command(response)

            current_time = current_date_time.get_time()

            if current_time in FEEDING_SCHEDULE:

                motor.dispence_food(portions_to_dispence=portions_on_schedule_dict[current_time])
                current_date_time_info = current_date_time.get_date_time()
                send_message.send_text_to_all_users('Pets were fed ' + str(current_date_time_info) + ' automatically.')
                sleep(60) # whait 60 sec to avoid multiple food dispence at feeding schedule time

            sleep(CHECK_UPDATES_INTERVAL_SEC)

        except KeyboardInterrupt:
            print('Aborted by user.')
            break


if __name__ == '__main__':
    main()
