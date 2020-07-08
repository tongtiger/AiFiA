import pandas as pd
import pickle



with open('C:\\Users\\tongt\\PycharmProjects\\kakao\\music_tag_dic.p', 'rb' ) as music_tag_dic:
    music_tag_dic = pickle.load(music_tag_dic)

with open('C:\\Users\\tongt\\PycharmProjects\\kakao\\tag_name_list.p', 'rb') as tag_name_list:
    tag_name_list = pickle.load(tag_name_list)


music_tags_frame = {}

for music in list(music_tag_dic.keys()):
    music_tags_frame[music] = []
    for i in range(len(tag_name_list)):
        music_tags_frame[music].append(0)
    for tag in music_tag_dic[music]:
        music_tags_frame[music][tag_name_list.index(tag)] = 1

music_tags_df = pd.DataFrame(music_tags_frame)

music_tags_df.to_csv("\\data\\music_tags_df.csv")
