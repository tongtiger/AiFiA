from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import pickle
from tqdm import tqdm

train = pd.read_csv('/content/drive/Shared drives/Kakao_Arena/train_0_8999_num_id_genre_tag.csv', index_col='num')
mini_meldata = np.load('/content/drive/Shared drives/Kakao_Arena/mini_meldata.npy')

mini_meldata = np.delete(mini_meldata, (0), axis=0)
drop_list = [612, 734, 1107, 1699, 2225, 2389, 3608, 4582, 4909, 5724, 5891, 6624, 6788, 6914, 7203, 7366, 7415]
for num in drop_list:
  train = train.drop(num)

x = np.array(mini_meldata)
y = np.array(train.drop(['id', 'genre'], axis=1))

print(x.shape)

x = x / 100
x = x.reshape(x.shape[0], 6, 1876, 1)

print(x.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.1)

model = Sequential()
model.add(Conv2D(filters=16, kernel_size=(5, 5), input_shape=(6, 1786, 1), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(filters=32, kernel_size=(5, 5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(filters=64, kernel_size=(5, 5), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(filters=64, kernel_size=(5, 5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(25, activation='sigmoid'))

model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test), batch_size=64)
