import requests

from telegram_config import telegram_bot_token, telegram_api_url
from telegram_config import USER_CHAT_ID_LIST


def send_text(chat_id, text):
    """Sending text message"""
    data = {'chat_id': chat_id, 'text': text}
    try:
        url = telegram_api_url + telegram_bot_token + '/sendMessage'
        requests.post(url, data=data)
    except:
        print('Send message error.')


def send_text_to_all_users(text):
    """Send text message to all users in USER_CHAT_ID_LIST """
    for user in USER_CHAT_ID_LIST:
        send_text(user, text)

if __name__ == '__main__':
    send_text_to_all_users('This is test tex message for all users')
