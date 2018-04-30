import requests

from telegram_config import TELEGRAM_BOT_TOKEN, TELEGRAM_API_URL


def check_updates_method_post(last_update_id):
    """Send request to telegram server."""
    data = {'offset': last_update_id + 1, 'limit': 5, 'timeout': 0}
    #It is possible to use proxies = dict(http='socks5://51.254.45.80:3128', socks5='https://51.254.45.80:3128')
    proxies = dict(http='http://51.254.45.80:3128', https='https://51.254.45.80:3128')
    try:
        url = TELEGRAM_API_URL + TELEGRAM_BOT_TOKEN + '/getUpdates'
        response = response = requests.get(url, params=data, proxies=proxies)
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
