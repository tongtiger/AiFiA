import json

with open('C:\\Users\\tongt\\PycharmProjects\\Melon\\data\\train.json', encoding='UTF8') as train_data:
    train_data = json.load(train_data)

with open('C:\\Users\\tongt\\PycharmProjects\\Melon\\data\\song_meta.json', encoding='UTF8') as song_data:
    song_data = json.load(song_data)

#음악 ID-장르 관계
music_with_genre = {}


for i in range(len(song_data)):
    music_with_genre[song_data[i]['song_name']] = []
    music_with_genre[song_data[i]['song_name']].append(song_data[i]['song_gn_dtl_gnr_basket'])


#음악 ID-태그 관계
music_with_tags = {}

for i in range(len(train_data)):
    for j in range(len(train_data[i]['songs'])):
        if train_data[i]['songs'][j] in music_with_tags:
            for k in range(len(train_data[i]['tags'])):
                music_with_tags[train_data[i]['songs'][j]].append(train_data[i]['tags'][k])
        else:
            music_with_tags[train_data[i]['songs'][j]] = []
            for k in range(len(train_data[i]['tags'])):
                music_with_tags[train_data[i]['songs'][j]].append(train_data[i]['tags'][k])



#태그 - 음악 ID 관계
tags_with_music = {}

for i in range(len(train_data)):
    for j in range(len(train_data[i]['tags'])):
        if train_data[i]['tags'][j] in tags_with_music:
            for k in range(len(train_data[i]['songs'])):
             tags_with_music[train_data[i]['tags'][j]].append(train_data[i]['songs'][k])
        else:
            tags_with_music[train_data[i]['tags'][j]] = []
            for k in range(len(train_data[i]['songs'])):
                tags_with_music[train_data[i]['tags'][j]].append(train_data[i]['songs'][k])








