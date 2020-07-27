import json
import pickle
from tqdm import tqdm

train_data = json.load(open('Data\\train.json', 'rb'))

id_with_tag = []

for playlist in tqdm(train_data):
    for id in playlist['songs']:
        id_with_tag.append(id)

id_with_tag = list(set(id_with_tag))
id_with_tag.sort()


id_without_tag = list(range(707988+1))
for id in tqdm(id_with_tag):
    id_without_tag.remove(id)

with open('Data_preprocessing\\id_with_tag\\id_without_tag.list', 'wb') as f:
    pickle.dump(id_without_tag, f)
