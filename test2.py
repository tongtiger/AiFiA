import pandas as pd
import pickle
from tqdm import tqdm

id_with_tag_mel_len_1876 = pickle.load(open('Data_preprocessing\id_with_tag\id_with_tag_mel_len_1876.list', 'rb'))
id_tag = pd.read_csv('Data_preprocessing\id_tag.csv', index_col='id')

a = []

for id in tqdm(id_with_tag_mel_len_1876):
    if id < 100000:
        a.append(id)

print(len(a))

for id in a:
    id_with_tag_mel_len_1876.remove(id)

for id in tqdm(id_with_tag_mel_len_1876):
     id_tag.drop(id)

with open('Data_preprocessing\\id_tag_0_100000.csv', 'wt') as f:
    pickle.dump(id_tag, f)