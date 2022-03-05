import requests

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
                if main_float < 0.02:
                    print(item, name, ":", main_float)