import json
import csv
import pickle
from tqdm import tqdm

#
train_data = json.load(open('Data\\train.json', 'rb'))
id_with_tag = pickle.load(open('Data_preprocessing\\id_with_tag\\id_with_tag.list', 'rb'))
id_tag_0 = pickle.load(open('Data_preprocessing\\id_tag\\id_tag_0.dic', 'rb'))
id_tag_1 = pickle.load(open('Data_preprocessing\\id_tag\\id_tag_1.dic', 'rb'))
id_tag_2 = pickle.load(open('Data_preprocessing\\id_tag\\id_tag_2.dic', 'rb'))
id_tag_3 = pickle.load(open('Data_preprocessing\\id_tag\\id_tag_3.dic', 'rb'))
id_tag_4 = pickle.load(open('Data_preprocessing\\id_tag\\id_tag_4.dic', 'rb'))
id_tag_5 = pickle.load(open('Data_preprocessing\\id_tag\\id_tag_5.dic', 'rb'))
id_tag_6 = pickle.load(open('Data_preprocessing\\id_tag\\id_tag_6.dic', 'rb'))
tag_morethan_10 = pickle.load(open('Data_preprocessing\\tag_10\\tag_morethan_10.list', 'rb'))
tag_10_tag = pickle.load(open('Data_preprocessing\\tag_10_tag\\tag_10_tag.dic', 'rb'))

#
for tag in tqdm(tag_10_tag):
    tag_10_tag[tag].append(tag)

#
tag_10_tag_num = {}
for i in tqdm(range(2780)):
    tag_10_tag_num[i] = tag_10_tag[tag_morethan_10[i]]

#
'''
id_tag_token = {}
for id in tqdm(id_tag_0):
    a = [0] * 2780
    for tag in id_tag_0[id]:
        for i in range(2780):
            if tag in tag_10_tag_num[i]:
                a[i] = 1
            else:
                pass
    id_tag_token[id] = a

with open('Data_preprocessing\\id_tag_token\\id_tag_token_0.dic', 'wb') as f:
    pickle.dump(id_tag_token, f)
'''

#
id_tag_token = {}
for id in tqdm(id_tag_1):
    a = [0] * 2780
    for tag in id_tag_1[id]:
        for i in range(2780):
            if tag in tag_10_tag_num[i]:
                a[i] = 1
            else:
                pass
    id_tag_token[id] = a

with open('Data_preprocessing\\id_tag_token\\id_tag_token_1.dic', 'wb') as f:
    pickle.dump(id_tag_token, f)

#
id_tag_token = {}
for id in tqdm(id_tag_2):
    a = [0] * 2780
    for tag in id_tag_2[id]:
        for i in range(2780):
            if tag in tag_10_tag_num[i]:
                a[i] = 1
            else:
                pass
    id_tag_token[id] = a

with open('Data_preprocessing\\id_tag_token\\id_tag_token_2.dic', 'wb') as f:
    pickle.dump(id_tag_token, f)

#
id_tag_token = {}
for id in tqdm(id_tag_3):
    a = [0] * 2780
    for tag in id_tag_3[id]:
        for i in range(2780):
            if tag in tag_10_tag_num[i]:
                a[i] = 1
            else:
                pass
    id_tag_token[id] = a

with open('Data_preprocessing\\id_tag_token\\id_tag_token_3.dic', 'wb') as f:
    pickle.dump(id_tag_token, f)

#
id_tag_token = {}
for id in tqdm(id_tag_4):
    a = [0] * 2780
    for tag in id_tag_4[id]:
        for i in range(2780):
            if tag in tag_10_tag_num[i]:
                a[i] = 1
            else:
                pass
    id_tag_token[id] = a

with open('Data_preprocessing\\id_tag_token\\id_tag_token_4.dic', 'wb') as f:
    pickle.dump(id_tag_token, f)

#
id_tag_token = {}
for id in tqdm(id_tag_5):
    a = [0] * 2780
    for tag in id_tag_5[id]:
        for i in range(2780):
            if tag in tag_10_tag_num[i]:
                a[i] = 1
            else:
                pass
    id_tag_token[id] = a

with open('Data_preprocessing\\id_tag_token\\id_tag_token_5.dic', 'wb') as f:
    pickle.dump(id_tag_token, f)

id_tag_token = {}
for id in tqdm(id_tag_6):
    a = [0] * 2780
    for tag in id_tag_6[id]:
        for i in range(2780):
            if tag in tag_10_tag_num[i]:
                a[i] = 1
            else:
                pass
    id_tag_token[id] = a

with open('Data_preprocessing\\id_tag_token\\id_tag_token_6.dic', 'wb') as f:
    pickle.dump(id_tag_token, f)