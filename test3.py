import numpy as np
import pandas as pd

mini = np.load('Data_preprocessing\mel_preprocessing\mini_meldata_0_100000.npy')

print(mini)
print(mini.shape)

id_tag = pd.read_csv('Data_preprocessing\id_tag_0_100000.csv', index_col='id')

print(id_tag)