import requests
from api_keys_loot import *
import time


gun = u'\U0001F52B'


def send_message_item_hunter_loot(message):
    try:
        requests.get(f'https://api.telegram.org/bot{brain_storm_key}/sendMessage?chat_id={brain_storm_chat_id}&text=' + message +'&parse_mode=html')
    except Exception as error:
        print("Telegram api has some problems, in line 7 error is: " + str(error))
        print("bot will go sleep for 60 seconds!")
        time.sleep(60)


item_dict = set()

while True:
    response = requests.get('https://loot.farm/botsInventory_730.json')
    data = response.json()

    for item in data['result']:
        name = data['result'][item]['n']
        list_item = data['result'][item]['u']
        for x in list_item:
            for y in list_item[x]:
                item_float = y['f']
                if isinstance(item_float, str) and ":" in item_float:
                    split_data = item_float.split(":")
                    while len(split_data[0]) < 5:
                        split_data[0] = "0" + split_data[0]
                    main_float = float("0." + split_data[0])
                    if main_float < 0.01:
                        if item not in item_dict:
                            message = f"{gun} {name} , float: {main_float}"
                            send_message_item_hunter_loot(message)
                            item_dict.add(item)

    time.sleep(10 * 60)
