import unittest
import check_updates


class CheckUpdatesTestCase(unittest.TestCase):
    def test_check_updates_function_status_code(self):
        last_update_id = 0
        response, last_update_id = check_updates.check_updates_method_post(last_update_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(last_update_id), int)


if __name__ == '__main__':
    unittest.main()
# current_date_time_info = current_date_time.get_time()
# print(' - Pets were fed' + str(current_date_time_info) + '  automatically.')
