import numpy as np
import pickle
from tqdm import tqdm

id_with_tag = pickle.load(open('Data_preprocessing\id_with_tag\id_with_tag.list', 'rb'))

for id in tqdm(id_with_tag):
    j = int(id/1000)
    f = np.load('Data\\arena_mel\\{}\\{}.npy'.format(j, id))
    f = f[42:47+1,]
    try:
        f = f.reshape(1,6,1876,1)
    except:
        id_with_tag.remove(id)

with open('Data_preprocessing\\id_with_tag_1876_clean.list', 'wb') as f:
    pickle.dump(id_with_tag, f)

for id in tqdm(id_with_tag[160000:]):
    j = int(id/1000)
    f = np.load('Data\\arena_mel\\{}\\{}.npy'.format(j, id))
    f = f[42:47+1,]
    f = f.reshape(1,6,1876,1)
    np.save(('Data_preprocessing\\mini_mel\\mini_{}'.format(id)), f)