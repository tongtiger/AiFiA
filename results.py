import json
from gensim.models import FastText
import pickle

#필요한 자료 및 모델
val_data = json.load(open("data/val.json", "rb"))   #맞춰야 하는 데이터

with open("tag_name_list.p", "rb") as f:
    tag_list = pickle.load(f)   #태그 리스트

with open("music_tag_dic.p", "rb") as f:
    music_tag = pickle.load(f)  #태그를 음악에 따라 묶은 것


fasttext = FastText.load("FastText.model")


#예상 내용이 들어가는 리스트, 일단 태그 10개, 곡 100개 만족하는거는 나중에 따로 처리해주고, 일단 채워넣는 단계
results = []


#topn에 기반한 함수 정의

#def type1_presager(data, ...):

def type2_presager(topn):
    predictions = fasttext.most_similar(positive=[word for word in data['plylst_title'].split(" ")], topn=topn)
    for prediction in predictions:
        if prediction[0] in tag_list:
            result['tags'].append(prediction[0])
        else:
            pass

def type3_presager(topn):
    pre_predictions = []
    predictions = fasttext.most_similar(positive=[tag for tag in data['tags']], topn=topn)
    for prediction in predictions:
        if prediction[0] in tag_list:
            pre_predictions.append(prediction[0])
        else:
            pass
    song_tag_basket = []
    for song in data['songs']:
        if song not in song_tag_basket:
            song_tag_basket.append(song)
        else:
            pass
    for pre_prediction in pre_predictions:
        if pre_prediction not in song_tag_basket:
            song_tag_basket.remove(pre_prediction)
        else:
            pass

def type4_presager(topn):
    predictions = fasttext.most_similar(positive=[tag for tag in data['tags']], topn=topn)
    for prediction in predictions:
        if prediction[0] in tag_list:
            result['tags'].append(prediction[0])
        else:
            pass


#위에서 정의한 함수 4개는 아래와 같이 사용될 예정, topn만 조정하여 태그 개수 충족
'''for data in val_data:
    result = {'id': data['id'], 'songs': [], 'tags': []}    #results 안에 들어갈 데이터(딕셔너리)
    if data['tags'] == data['songs'] == []:
        predictions = fasttext.most_similar(positive=[word for word in data['plylst_title'].split(" ")], topn = 100)
        for prediction in predictions:
            if prediction[0] in tag_list:
                result['tags'].append(prediction[0])
            else:
                pass
        print("노래 불러와야 함")
        print('Type2')
    elif data['plylst_title'] != '' and data['tags'] != [] and data['songs'] == []: #Type3
        predictions = fasttext.most_similar(positive=[tag for tag in data['tags']], topn = 100)
        for prediction in predictions:
            if prediction[0] in tag_list:
                result['tags'].append(prediction[0])
            else:
                pass
        print("노래 불러오고, 플레이리스트 제목도 고려해줄지 생각해봐야함")
        print('Type4')
    elif data['tags'] == [] and data['plylst_title'] == '':
        print("딥러닝 학습 모델 넣어야함")
        print('Type1')
    else:
        pre_predictions = []
        predictions = fasttext.most_similar(positive=[tag for tag in data['tags']], topn=100)
        for prediction in predictions:
            if prediction[0] in tag_list:
                pre_predictions.append(prediction[0])
            else:
                pass
        song_tag_basket = []
        for song in data['songs']:
            if song not in song_tag_basket:
                song_tag_basket.append(song)
            else:
                pass
        for pre_prediction in pre_predictions:
            if pre_prediction not in song_tag_basket:
                song_tag_basket.remove(pre_prediction)
            else:
                pass
        print("얘도 노래 불러와야함.")
        print('Type3')
    results.append(result)'''


for data in val_data:

    result = {'id': data['id'], 'songs': [], 'tags': []}  # results 안에 들어갈 데이터(딕셔너리)

    if data['tags'] == data['songs'] == []:
        type2_presager(topn = 100)
    elif data['plylst_title'] != '' and data['tags'] != [] and data['songs'] == []:
        type4_presager(topn = 100)
    elif data['tags'] == [] and data['plylst_title'] == '':
        type1_presager()
    else:
        type3_presager(topn = 100)

    if len(result['tags']) > 10:
        result['tags'] = result['tags'][: 9+1]
    elif len(result['tags']) < 10:
        if data['tags'] == data['songs'] == []:
            type2_presager(topn=500)
        elif data['plylst_title'] != '' and data['tags'] != [] and data['songs'] == []:
            type4_presager(topn=500)
        elif data['tags'] == [] and data['plylst_title'] == '':
            type1_presager()
        else:
            type3_presager(topn=500)

    results.append(result)




