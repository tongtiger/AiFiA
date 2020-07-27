import json
import pickle
from tqdm import tqdm

train_data = json.load(open('Data\\train.json', 'rb'))
id_with_tag = pickle.load(open('Data_preprocessing\\id_with_tag\\id_with_tag.list', 'rb'))

id_tag = {}

for id in id_with_tag:
    id_tag[id] = []

for playlist in tqdm(train_data):
    for id in playlist['songs']:
        for tag in playlist['tags']:
            id_tag[id].append(tag)

for id in id_tag:
    id_tag[id] = list(set(id_tag[id]))
    id_tag[id].sort()

with open('Data_preprocessing\\id_tag\\id_tag.dic', 'wb') as f:
    pickle.dump(id_tag, f)