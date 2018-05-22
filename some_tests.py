import unittest
import check_updates
import user_authentication
import portions_at_schedule
import send_message
# uncomment 'import commands' only for Raspberry Pi
# import commands

from telegram_config import AUTHORIZED_USER_CHAT_ID_LIST
from proxy_parser import Proxy


class CheckUpdatesTestCase(unittest.TestCase):
    """Checking check_update func return status code 200,
    returns last_update_id, proxies dict and check send_message
    func in one test to save some time during tests and not find proxies twice"""
    def test_check_updates_function_and_send_messege_fucntion(self):
        proxy = Proxy()
        proxies = proxy.get_availible_proxy_address()
        last_update_id = 0
        response, last_update_id, proxies = check_updates.check_updates_method_get(last_update_id, proxies)
        result = send_message.send_text(AUTHORIZED_USER_CHAT_ID_LIST[0], 'This is an autotest text message.', proxies)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(last_update_id), int)
        self.assertEqual(type(proxies), dict)
        self.assertEqual(result, 200)


class CheckUserAuthenticationTestCase(unittest.TestCase):
    def test_check_AUTHORIZED_USER_CHAT_ID_LIST_not_empty(self):
        result = len(AUTHORIZED_USER_CHAT_ID_LIST) > 0
        self.assertEqual(result, True)

    def test_user_authentication_return_true_for_all_users_in_AUTHORIZED_USER_CHAT_ID_LIST(self):
        for user_chat_id in AUTHORIZED_USER_CHAT_ID_LIST:
            result = user_authentication.user_in_authorized_user_chad_id_list(user_chat_id)
            self.assertEqual(result, True)


class PortionsAtScheduleTestCase(unittest.TestCase):
    def test_portions_at_schedule_return_dict(self):
        FEEDING_SCHEDULE = ['07:00', '13:00', '19:00']
        PORTIONS_TO_DISPENCE = [2, 1, 2]
        new_schedule = portions_at_schedule.create_portions_on_schedule_dict(FEEDING_SCHEDULE, PORTIONS_TO_DISPENCE)
        self.assertEqual(new_schedule, {'07:00' : 2, '13:00' : 1, '19:00' : 2})



# This module is reasonable to test on Raspberry Pi only, cause it has all necessary modules
# to test everything properly. Necessary modules are: RPI.GPIO, tempereture (includes Adafruit DHT library),
# subprocess (runs only on linux). Otherwise tests return error.
#
# class CheckCommandsTestCase(unittest.TestCase):
#     def test_command_feed(self):
#         chat_id = AUTHORIZED_USER_CHAT_ID_LIST[0]
#         command = '/feed'
#         result = commands.run_command(chat_id, command)
#         self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
