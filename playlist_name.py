import json

with open('C:/Users/tongt/PycharmProjects/Melon/data/train.json', encoding='UTF8') as train_data:
    train_data = json.load(train_data)

playlist_basket = []

#플레이리스트 이름을 txt파일로 전환하기 위해 txt 파일 생성
playlist_to_txt = open("C:/Users/tongt/PycharmProjects/Melon/data/playlist.txt", "w", encoding="UTF8") 

#반복문, 조건문을 이용해 객체에 플레이리스트를 저장함과 동시에 txt 파일에 작성, 제목간 구분을 위해서 /n 삽입
for i in range(len(train_data)):
    if train_data[i]['plylst_title'] in playlist_basket:
        pass
    else:
        playlist_basket.append(train_data[i]['plylst_title'])
        playlist_to_txt.write(train_data[i]['plylst_title'])
        playlist_to_txt.write("/n")
        
playlist_to_txt.close()


