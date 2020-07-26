import csv
import pickle
from tqdm import tqdm

id_with_tag_mel_len_1876 = pickle.load(open('Data_preprocessing\id_with_tag\id_with_tag_mel_len_1876.list', 'rb'))
id_tag_token = pickle.load(open('Data_preprocessing\id_tag_token\id_tag_token.dic', 'rb'))

f = open('Data_preprocessing\id_tag_0_100000.csv', 'wt', newline='')

fieldnames = ['id'] + list(range(2780))

id_tag_csv = csv.DictWriter(f, fieldnames=fieldnames)

id_tag_csv.writeheader()

for id in tqdm(id_with_tag_mel_len_1876):
    if id < 100000:
        dic = {'id': id}
        for i in range(2780):
            dic[i] = id_tag_token[id][i]
        id_tag_csv.writerow(dic)
    else:
        pass