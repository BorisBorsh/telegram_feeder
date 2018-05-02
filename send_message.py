import requests

from telegram_config import TELEGRAM_BOT_TOKEN, TELEGRAM_API_URL
from telegram_config import AUTHORIZED_USER_CHAT_ID_LIST
from proxy_parser import Proxy

def send_text(chat_id, text):
    """Sending text message"""
    data = {'chat_id': chat_id, 'text': text}
    #Find availible working proxy to send message reliably
    proxy = Proxy()
    proxies = proxy.get_availible_proxy_address()
    print('Preparing to send message.')
    try:
        url = TELEGRAM_API_URL + TELEGRAM_BOT_TOKEN + '/sendMessage'
        response = response = requests.get(url, params=data, proxies=proxies)
        return response.status_code
    except requests.exceptions.RequestException as e:
        proxy = Proxy()
        proxies = proxy.get_availible_proxy_address()
        send_text(chat_id, text)
        print('Exception after send_text happend: ', e)


def send_text_to_all_users(text):
    """Send text message to all users in USER_CHAT_ID_LIST """
    for user in AUTHORIZED_USER_CHAT_ID_LIST:
        send_text(user, text)

if __name__ == '__main__':
    send_text_to_all_users('This is test tex message for all users')
