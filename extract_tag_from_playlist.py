#FastText가 학습가능한 input 형태로 데이터 처리

import pickle
import json

with open("playlist_name_list.p", "rb") as f:
    playlists = pickle.load(f)

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




#FastText 이용하여 플레이리스트로부터 태그 추출

from gensim.models import FastText
import pickle
import json

with open("playlists_splitted.list", "rb") as f:
    playlist = pickle.load(f)

with open("tag_name_list.p", "rb") as f:
    tags = pickle.load(f)

#FastText 기본 모델, 기본적으로 Word2Vec과 비슷한 원리로 작동함
model = FastText(playlist, min_count=1)

#FastText 모델 저장
model.save("FastText.model")

val_data = json.load(open("data\\val.json", "rb"))

#val 데이터로부터 유추한 태그들(Type2 유형)
playlist_to_tags = {}

for data in val_data:
    # 플레이리스트만 주어진 유형(Type2)에 대해 진행
    if data['plylst_title'] != "" and data['tags'] == [] and data['songs'] ==[]:
        playlist_to_tags[data['plylst_title']] = []
        #val.json의 type 2 문제에서 플레이리스트 제목을 띄어쓰기로 구분한 각각의 요소가 공통으로 가까운 단어를 50개 가져오기
        recommends = model.most_similar(positive=[word for word in data['plylst_title'].split(" ")], topn= 50)
        #위에서 가져온 단어(recommends) 중 태그만을 playlist_to_tags에 추가
        for recommend in recommends:
            if recommend[0] in tags:
                for begin_tag in playlist_to_tags[data['plylst_title']] :
                    sim1, sim2 = diff_2gram(begin_tag, recommend[0])
                    if sim1 <= 0.5 and sim2 <= 0.5 :
                        playlist_to_tags[data['plylst_title']].append(recommend)
                    else : pass
            else:
                pass
    else:
        pass

with open("playlist_to_tags.dic", "wb") as f:
    pickle.dump(playlist_to_tags, f)

with open("playlist_to_tags.dic", "rb") as f:
    tags = pickle.load(f)

#json으로 저장할 때, ensure_ascii에 False를 할당해주지 않으면 유니코드 16진수로 적혀짐.
tags_json = json.dumps(tags, ensure_ascii=False)


with open("[TEST]val_playlist_to_tags.json", "w", encoding='UTF8') as f:
    json.dump(tags, f, ensure_ascii=False)



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
