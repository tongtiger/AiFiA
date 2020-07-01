#train_곡별빈도수
import json
import operator

#train.json에서 곡별 빈도수, 노래 id가 'songs' 안에 리스트로 수록
with open('C:/Users/tongt/PycharmProjects/Melon/data/train.json', encoding='UTF8') as train_data:
    train_data = json.load(train_data)

#빈도수 기록 딕셔너리
how_often = {}

#반복문 활용 정리
for i in range(len(train_data)):
    for j in range(len(train_data[i]['songs'])):
        if train_data[i]['songs'][j] in how_often:
            how_often[train_data[i]['songs'][j]] +=1
        else:
            how_often[train_data[i]['songs'][j]] =1

#전부 출력
for song, frequency in how_often.items():
    print("Song Id: {}".format(song), "Frequency: {}".format(frequency))



#빈도수 x 이상 출력
for song, frequency in how_often.items():
    if frequency <= x:
       pass
    else:
        print("Song Id: {}".format(song), "Frequency: {}".format(frequency))

#빈도수 오림차순 정리
frequency_distribution = sorted(how_often.items(), reverse = True, key = operator.itemgetter(1))

#빈도수 x 이상인 곡들의 개수
basket = {}

for song, frequency in how_often.items():
    if frequency <= 500:
        pass
    else:
        basket[song] = frequency

print(len(basket))
