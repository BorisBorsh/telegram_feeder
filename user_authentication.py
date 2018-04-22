from telegram_config import AUTHORIZED_USER_CHAT_ID_LIST


def user_in_authorized_user_chad_id_list(chat_id):
    """Checking if current user in authorized_user_chat_id_list"""
    if chat_id in AUTHORIZED_USER_CHAT_ID_LIST:
        return True
    else:
        # TODO may be send unauthorized user name instead of chat_id?
        unauthorized_user_message = 'Unauthorized user ' + str(chat_id)
        send_message.send_text(BORSH_ID, unauthorized_user_message)
        return False