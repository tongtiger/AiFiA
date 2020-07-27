from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import ModelCheckpoint,EarlyStopping
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import pickle
from tqdm import tqdm

mini_meldata_0_100000 = np.load('Data_preprocessing\mel_preprocessing\mini_meldata_0_100000.npy')
tag_data = pd.read_csv('Data_preprocessing\\id_tag_0_100000.csv', index_col='id')
x = mini_meldata_0_100000
y = np.array(tag_data)
print(x.shape)
print(y.shape)
x = (x - float(np.min(x))) / float(np.max(x))
x = x.astype('float32')

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.005)

model = Sequential()
model.add(Conv2D(filters=16, kernel_size=(3, 3), activation="relu", input_shape=(6,1876,1)))
model.add(Dropout(0.25))
model.add(Conv2D(32, kernel_size=(2, 2), activation='relu'))
model.add(Dropout(0.25))
model.add(Conv2D(64, kernel_size=(2, 2), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2780, activation='sigmoid'))

'''
id_with_tag_1876_clean = pickle.load(open('Data_preprocessing\\id_with_tag_1876_clean.list', 'rb'))

for i in range(550):
    tag_data = pd.read_csv('Data_preprocessing\\id_tag_{}_{}.csv'.format(i*1000, (i+1)*1000), index_col='id')
    mini_meldata = np.zeros((1,6,1876,1))
    for id in id_with_tag_1876_clean[i*1000:(i+1)*1000]:
        f = np.load('Data_preprocessing\\mini_mel\\mini_{}'.format(id))
        mini_meldata = np.append(mini_meldata, f, axis=0)
    mini_meldata = np.delete(mini_meldata, (0), axis=0)
    x = mini_meldata
    y = np.array(tag_data)
'''

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test), batch_size=64)

model.save('model.h5')