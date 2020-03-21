import time
import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()




def get_status(user_id):
    params = {
        'fields': "online",
        'user_ids': user_id,
        'access_token': os.getenv('vk_token'),
        'v': 5.92
    }
    response = (requests.post('https://api.vk.com/method/users.get', params=params).json().get('response'))[0]
    return response['online']  # Верните статус пользователя в ВК


def sms_sender(sms_text):
    account_token = os.getenv('token')
    account_sid = os.getenv('sid')
    client = Client(account_sid, account_token)
    message = client.messages.create(
                              body=sms_text,
                              from_=os.getenv('phone_from'),
                              to=os.getenv('phone_to'),
                          )
    return message.sid  # Верните sid отправленного сообщения из Twilio

# vk_id = input("Введите id ")
# get_status(vk_id)
if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
