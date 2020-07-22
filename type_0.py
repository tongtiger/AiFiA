from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import ModelCheckpoint,EarlyStopping
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
from tqdm import tqdm

train = pd.read_csv('/content/drive/Shared drives/Kakao_Arena/train_0_8999_num_id_genre_tag.csv', index_col='num')
mini_meldata = np.load('/content/drive/Shared drives/Kakao_Arena/mini_meldata.npy')

drop_list = [612, 734, 1107, 1699, 2225, 2389, 3608, 4582, 4909, 5724, 5891, 6624, 6788, 6914, 7203, 7366, 7415]
for num in drop_list:
  train = train.drop(num)

x = mini_meldata
y = np.array(train.drop(['id', 'genre'], axis=1))

print(np.max(x))
print(np.min(x))
print(x.shape)

x = (x + 100) / 120
x = x.astype('float32')
print(np.max(x))
print(np.min(x))

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.1)

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
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(16, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(12897, activation='sigmoid'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

modelpath='/content/drive/Shared drives/Kakao_Arena/model/{epoch:02d}-{val_loss:.4f}.hdf5'
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True)
early_stopping_callback = EarlyStopping(monitor='val_loss', patience=5)

history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=30, batch_size=200, verbose=0, callbacks=[early_stopping_callback,checkpointer])

print("\n Test Accuracy: %.4f" % (model.evaluate(x_test, y_test)[1]))

y_vloss = history.history['val_loss']
y_loss = history.history['loss']

x_len = np.arange(len(y_loss))
plt.plot(x_len, y_vloss, marker='.', c='red', label='Testset_loss')
plt.plot(x_len, y_loss, marker='.', c='blue', label='Trainset_loss')
plt.legend(loc='upper right')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show
