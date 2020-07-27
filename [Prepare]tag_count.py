import json
import pickle
from tqdm import tqdm

train_data = json.load(open('Data\\train.json', 'rb'))

tag_count = {}

for playlist in tqdm(train_data):
    for tag in playlist['tags']:
        if tag in tag_count:
            tag_count[tag] += 1
        else:
            tag_count[tag] = 1

with open('Data_preprocessing\\tag_count\\tag_count.dic', 'wb') as f:
    pickle.dump(tag_count, f)