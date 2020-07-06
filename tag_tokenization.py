import json
from numpy import array
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

with open('/workspace/Pareto/train.json') as train_data:
	train = json.load(train_data)
	
tag_basket = []

for i in range(len(train)):
	for tag in train[i]['tags']:
		if tag in tag_basket:
			pass
		else:
			tag_basket.append(tag)

token = Tokenizer()
token.fit_on_texts(tag_basket)

y = 0

for i in range(len(train)):
    x = token.texts_to_sequences(train[i]['tags'])
    padded_x = pad_sequences(x, 11)
    print(padded_x, ',')