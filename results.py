import json
from gensim.models import FastText
import pickle
from tqdm import tqdm

#필요한 자료 및 모델
val_data = json.load(open("data/val.json", "rb"))   #맞춰야 하는 데이터

with open("tag_name_list.p", "rb") as f:
    tag_list = pickle.load(f)   #태그 리스트

with open("music_tag_dic.p", "rb") as f:
    music_tag = pickle.load(f)  #태그를 음악에 따라 묶은 것

with open("data/tag_music_freq.dic", "rb") as f:
    tag_music_freq = pickle.load(f)

fasttext = FastText.load("FastText.model")


#예상 내용이 들어가는 리스트, 일단 태그 10개, 곡 100개 만족하는거는 나중에 따로 처리해주고, 일단 채워넣는 단계
results = []




#def type1_presager(data, ...):

def type2_presager(topn):
    predictions = fasttext.most_similar(positive=[word for word in data['plylst_title'].split(" ")], topn=topn)    
    z = 0    
    for prediction in predictions:
        while z <10:
            if prediction[0] in tag_list:
                result['tags'].append(prediction[0])
                z+=1
            else:
                pass

def type2_presager_ngram(topn):
    predictions = fasttext.most_similar(positive=[word for word in data['plylst_title'].split(" ")], topn=topn)
    for prediction in predictions:
        if prediction[0] in tag_list:
            if len(result['tags']) == 0:
                result['tags'].append(prediction[0])
            else:
                for begin_tag in result['tags']:
                    sim1, sim2 = diff_2gram(begin_tag, prediction[0])
                    if sim1 <= 0.5 and sim2 <= 0.5:
                        result['tags'].append(prediction[0])
                    else:
                        pass
        else:
            pass

def type2_vote(frequency):
    for song, freq in musics.items():
        if freq == frequency:
            answer_songs.append(song)
        else:
            pass

def type2_submit_answer():
    for answer_song in answer_songs[:99 + 1]:
        result['songs'].append(answer_song)

def ngram(s, num):
   res = []
   letter = 0
   slen = len(s) - num + 1
   for i in range(slen):
        ss = s[i:i + num]
        res.append(ss)
   return res


def diff_2gram(sa, sb):
    if len(sa) == 1 or len(sb) == 1:
        a = ngram(sa, 1)
        b = ngram(sb, 1)
    else:
        a = ngram(sa, 2)
        b = ngram(sb, 2)
    r = []
    count = 0
    for i in a:
        for j in b:
            if i == j:
                count += 1
                r.append(i)

    return count / len(a), count/len(b)

'''def type3_presager(topn):
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
            pass'''


#위에서 정의한 함수 4개는 아래와 같이 사용될 예정, topn만 조정하여 태그 개수 충족
for data in tqdm(val_data):
    result = {'id': data['id'], 'songs': [], 'tags': []}    #results 안에 들어갈 데이터(딕셔너리)

    #type1 problem
    if data['tags'] == [] and data['plylst_title'] == '':

    #type2 problem
    elif data['tags'] == data['songs'] == []:
        type2_presager_ngram(topn=20)
        if len(result['tags']) >= 10:
            result['tags'] = result['tags'][:9 + 1]
        else:
            result['tags'].clear()
            type2_presager_ngram(topn=30)
            if len(result['tags']) >= 10:
                result['tags'] = result['tags'][:9 + 1]
            else:
                result['tags'].clear()
                type2_presager_ngram(topn=40)
                if len(result['tags']) >= 10:
                    result['tags'] = result['tags'][: 9 + 1]
                else:
                    result['tags'].clear()
                    type2_presager_ngram(topn=50)
                    if len(result['tags']) >= 10:
                        result['tags'] = result['tags'][: 9 + 1]
                    else:
                        result['tags'].clear()
                        type2_presager_ngram(topn=100)
                        if len(result['tags']) >= 10:
                            result['tags'] = result['tags'][: 9 + 1]
                        else:
                            result['tags'].clear()
                            type2_presager_ngram(topn=150)
                            if len(result['tags']) >= 10:
                                result['tags'] = result['tags'][: 9 + 1]
                            else:
                                result['tags'].clear()
                                type2_presager(topn=4000)

        # 투표
        musics = {}
        for tag in result['tags']:
            for song in tag_music_freq[tag]:
                if song not in musics:
                    musics[song] = 1
                else:
                    musics[song] += 1

        # 투표 결과 반영
        answer_songs = []
        type2_vote(frequency=10)
        if len(answer_songs) >= 100:
            type2_submit_answer()
        else:
            type2_vote(frequency=9)
            if len(answer_songs) >= 100:
                type2_submit_answer()
            else:
                type2_vote(frequency=8)
                if len(answer_songs) >= 100:
                    type2_submit_answer()
                else:
                    type2_vote(frequency=7)
                    if len(answer_songs) >= 100:
                        type2_submit_answer()
                    else:
                        type2_vote(frequency=6)
                        if len(answer_songs) >= 100:
                            type2_submit_answer()
                        else:
                            type2_vote(frequency=5)
                            if len(answer_songs) >= 100:
                                type2_submit_answer()
                            else:
                                type2_vote(frequency=4)
                                if len(answer_songs) >= 100:
                                    type2_submit_answer()

                                else:
                                    type2_vote(frequency=3)
                                    if len(answer_songs) >= 100:
                                        type2_submit_answer()
                                    else:
                                        type2_vote(frequency=2)
                                        if len(answer_songs) >= 100:
                                            type2_submit_answer()
                                        else:
                                            type2_vote(frequency=1)
                                            type2_submit_answer()

    #type3 problem
    elif data['tags'] != [] and data['songs'] != [] and data['plylst_title'] = '':
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

    #type4 problem
    else:
        predictions = fasttext.most_similar(positive=[tag for tag in data['tags']], topn = 100)
        for prediction in predictions:
            if prediction[0] in tag_list:
                result['tags'].append(prediction[0])
            else:
                pass
        print("노래 불러오고, 플레이리스트 제목도 고려해줄지 생각해봐야함")
        print('Type4')

    results.append(result)





with open("data/results.json", "wb", encoding='UTF8') as f:
    json.dump(results, f, ensure_ascii=False)

