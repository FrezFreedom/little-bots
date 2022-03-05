import requests
import time
from api_keys import *


def send_message_to_brain_storm(message):
    try:
        requests.get(f'https://api.telegram.org/bot{brain_storm_key}/sendMessage?chat_id={brain_storm_chat_id}&text=' + message +'&parse_mode=html')
    except Exception as error:
        print("Telegram api has some problems, in line 7 error is: " + str(error))
        print("bot will go sleep for 60 seconds!")
        time.sleep(60)


send_message_to_brain_storm("hey")