import requests

from telegram_config import TELEGRAM_BOT_TOKEN, TELEGRAM_API_URL


def check_updates_method_post(last_update_id):
    """Send request to telegram server."""
    data = {'offset': last_update_id + 1, 'limit': 5, 'timeout': 0}
    try:
        url = TELEGRAM_API_URL + TELEGRAM_BOT_TOKEN + '/getUpdates'
        response = requests.post(url, data=data)
        print(response.json()['result'])
    except requests.exceptions.RequestException as e:
        print('Exception after update happend: ', e)
        return None, last_update_id

    if response.status_code == 200:
        if response.json()['result']:
            """If we have a new update with new update id, we save it.
               Else we return previous last_update_id."""
            last_update_id = response.json()['result'][0]['update_id']
            return response, last_update_id
        else:
            return response, last_update_id
    else:
        print('Something is wrong with server response')
        return None, last_update_id
