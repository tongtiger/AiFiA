import json
# import pickle
import gzip

with open('DataSet/train.json', encoding='UTF8') as train_data:
    train = json.load(train_data)

tag_list = []

for i in range(len(train)):
    if len(train[i]["tags"]) == 1:
        pass
    else:
        tag_list.append(train[i]["tags"])

print(tag_list)

'''
# save
with open('DataSet/tag_from_train_data.pickle', 'wb') as f:
    pickle.dump(tag_list, f, pickle.HIGHEST_PROTOCOL)
'''

# save and compress
with gzip.open('DataSet/tag_from_train_data.pickle', 'wb') as f:
    pickle.dump(tag_list, f)
