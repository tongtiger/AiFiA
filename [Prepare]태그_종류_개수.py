#태그 종류 및 개수 파악
import json

#train 데이터 읽기
with open('C:\\Users\\tongt\\PycharmProjects\\Melon\\data\\train.json', encoding='UTF8') as train_data:
    train_data = json.load(train)

#태그 꾸러미
tag_basket = []

for i in range(len(train_data)):
    for tag in train_data[i]['tags']:
        if tag in tag_basket:
            pass
        else:
            tag_basket.append(tag)

#태그 꾸러미 출력
print(tag_basket)

#태그 개수
print(len(tag_basket))


















