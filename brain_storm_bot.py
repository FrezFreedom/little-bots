import requests
import time
from api_keys import *

green_circle = u'\U0001F7E2'
lollipop = u'\U0001F36D'
doughnut = u'\U0001F369'
rocket = u'\U0001F680'
construction_sign = u'\U0001F6A7'


def send_message_to_brain_storm(message):
    try:
        requests.get(f'https://api.telegram.org/bot{brain_storm_key}/sendMessage?chat_id={brain_storm_chat_id}&text=' + message +'&parse_mode=html')
    except Exception as error:
        print("Telegram api has some problems, in line 7 error is: " + str(error))
        print("bot will go sleep for 60 seconds!")
        time.sleep(60)


message = f'''
{rocket} <b>BrainStorm Time</b>
Hey man, Think about <b>ideas</b>.
You are the <b>best</b> thinker in The global.
So you can find <b>awesome</b> ideas.
Please send at least an idea till <b>12</b> hours later.
Thanks!
'''

while True:
    send_message_to_brain_storm(message)
    time.sleep(12 * 60 * 60)
