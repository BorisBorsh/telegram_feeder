import requests

from telegram_config import telegram_bot_token, telegram_api_url


def send_text(chat_id, text):
    """Sending text message."""
    data = {'chat_id': chat_id, 'text': text}
    try:
        url = telegram_api_url + telegram_bot_token + '/sendMessage'
        requests.post(url, data=data)
    except:
        print('Send message error.')
