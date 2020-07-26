import numpy as np
import csv
import pickle
from tqdm import tqdm

id_with_tag = pickle.load(open('Data_preprocessing\id_with_tag\id_with_tag.list', 'rb'))

err = []

for id in tqdm(id_with_tag):
    j = int(id/1000)
    f = np.load('Data\\arena_mel\\{}\\{}.npy'.format(j, id))
    f = f[42:47+1,]
    try:
        f = f.reshape(1,6,1876,1)
        np.save(('Data_preprocessing\\mini_mel\\mini_{}'.format(id)), f)
    except:
        err.append(id)

for id in tqdm(err):
    id_with_tag.remove(id)

with open('Data_preprocessing\\id_with_tag_1876_clean.list', 'wb') as f:
    pickle.dump(id_with_tag, f)

del id_with_tag
del err

id_with_tag_1876_clean = pickle.load(open('Data_preprocessing\\id_with_tag_1876_clean.list', 'rb'))
id_tag_token = pickle.load(open('Data_preprocessing\id_tag_token\id_tag_token.dic', 'rb'))

fieldnames = ['id'] + list(range(2780))

for i in range(550):
    f = open('Data_preprocessing\\id_tag_{}_{}.csv'.format(i*1000, (i+1)*1000), 'wt', newline='')
    a = csv.DictWriter(f, fieldnames=fieldnames)
    a.writeheader()
    for id in tqdm(id_with_tag_1876_clean[i*1000:(i+1)*1000]):
        dic = {'id': id}
        for i in range(2780):
            dic[i] = id_tag_token[id][i]
        a.writerow(dic)