import json

with open('C:/Users/tongt/PycharmProjects/Melon/data/train.json', encoding='UTF8') as train_data:
    train_data = json.load(train_data)

playlist_basket = []

for i in range(len(train_data)):
    if train_data[i]['plylst_title'] in playlist_basket:
        pass
    else:
        playlist_basket.append(train_data[i]['plylst_title'])

print(playlist_basket)



