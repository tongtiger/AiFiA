import json
import pickle

file = json.load(open("data\\train.json", 'rb'))

music_tag_dic = {}

for i in range(len(file)):
    for song in file[i]['songs']:
        music_tag_dic[song] = []
        for tag in file[i]['tags']:
            if tag not in music_tag_dic[song]:
                music_tag_dic[song].append(tag)
            else:
                pass

with open("music_tag_dic.p", "wb") as f:
    pickle.dump(music_tag_dic, f)
