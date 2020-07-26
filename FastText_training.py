#FastText가 학습가능한 input 형태로 데이터 처리

import pickle
import json

train = json.load(open("data/train.json", "rb"))

#플레이리스트 제목 중 띄어쓰기가 되어있는 것들은 띄어쓰기로 구분된 단어들과 태그들의 집합 만들기
playlists_splitted = []

k = 0

for data in train:
    #플레이리스트 제목을 띄어쓰기한 리스트로 변환하여 playlists_splitted에 첨가
    playlists_splitted.append(data['plylst_title'].split(" "))
    #플레이리스트에 속한 태그를 이어서 첨가
    for tag in data['tags']:
        playlists_splitted[k].append(tag)
    k += 1

with open("playlists_splitted.list", "wb") as f:
    pickle.dump(playlists_splitted, f)
