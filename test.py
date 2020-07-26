import numpy as np
import pickle
from tqdm import tqdm

id_with_tag_mel_len_1876 = pickle.load(open('Data_preprocessing\id_with_tag\id_with_tag_mel_len_1876.list', 'rb'))

mini_meldata_0_251000 = np.zeros((1,6,1876,1))

for i in tqdm(range(100)):
    tem = np.load('Data_preprocessing\mel_preprocessing\mini_meldata_{}.npy'.format(i))
    mini_meldata_0_251000 = np.append(mini_meldata_0_251000, tem, axis=0)

mini_meldata_0_251000 = np.delete(mini_meldata_0_251000, (0), axis=0)
np.save('Data_preprocessing\\mel_preprocessing\\mini_meldata_0_251000', mini_meldata_0_251000)