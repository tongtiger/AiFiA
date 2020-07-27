import numpy as np
import pickle
from tqdm import tqdm

id_without_tag = pickle.load(open('Data_preprocessing\id_with_tag\id_without_tag.list', 'rb'))

for id in tqdm(id_without_tag):
    j = int(id/1000)
    f = np.load('Data\\arena_mel\\{}\\{}.npy'.format(j, id))
    f = f[42:47+1,]
    try:
        f = f.reshape(1,6,1876,1)
    except:
        id_without_tag.remove(id)

with open('Data_preprocessing\\id_without_tag_clean.list', 'wb') as f:
    pickle.dump(id_without_tag, f)

mini_meldata_unknowns = np.zeros((1,6,1876,1))

for id in tqdm(id_without_tag):
    j = int(id/1000)
    f = np.load('Data\\arena_mel\\{}\\{}.npy'.format(j, id))
    f = f[42:47+1,]
    f = f.reshape(1,6,1876,1)
    mini_meldata_unknowns = np.append(mini_meldata_unknowns, f, axis=0)

mini_meldata_unknowns = np.delete(mini_meldata_unknowns, (0), axis=0)
np.save('Data_preprocessing\\mel_preprocessing\\mini_meldata_unknowns', mini_meldata_unknowns)