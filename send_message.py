import requests

from telegram_config import TELEGRAM_BOT_TOKEN, TELEGRAM_API_URL
from telegram_config import AUTHORIZED_USER_CHAT_ID_LIST


def send_text(chat_id, text):
    """Sending text message"""
    data = {'chat_id': chat_id, 'text': text}
    proxies = dict(http='socks5://148.251.34.12:1080', https='socks5://148.251.34.12:1080')
    try:
        url = telegram_api_url + TELEGRAM_BOT_TOKEN + '/sendMessage'
        response = response = requests.get(url, params=data, proxies=proxies)
    except:
        print('Send message error.')


def send_text_to_all_users(text):
    """Send text message to all users in USER_CHAT_ID_LIST """
    for user in AUTHORIZED_USER_CHAT_ID_LIST:
        send_text(user, text)

if __name__ == '__main__':
    send_text_to_all_users('This is test tex message for all users')
