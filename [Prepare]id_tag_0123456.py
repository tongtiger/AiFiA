import pickle
from tqdm import tqdm

id_tag = pickle.load(open('Data_preprocessing\\id_tag\\id_tag.dic', 'rb'))

id_tag_0 = {}
id_tag_1 = {}
id_tag_2 = {}
id_tag_3 = {}
id_tag_4 = {}
id_tag_5 = {}
id_tag_6 = {}

for id in tqdm(id_tag):
    if (0 <= id <= 99999):
        id_tag_0[id] = id_tag[id]
    elif (100000 <= id <= 199999):
        id_tag_1[id] = id_tag[id]
    elif (200000 <= id <= 299999):
        id_tag_2[id] = id_tag[id]
    elif (300000 <= id <= 399999):
        id_tag_3[id] = id_tag[id]
    elif (400000 <= id <= 499999):
        id_tag_4[id] = id_tag[id]
    elif (500000 <= id <= 599999):
        id_tag_5[id] = id_tag[id]
    else:
        id_tag_6[id] = id_tag[id]

with open('Data_preprocessing\\id_tag\\id_tag_0.dic', 'wb') as f:
    pickle.dump(id_tag_0, f)

with open('Data_preprocessing\\id_tag\\id_tag_1.dic', 'wb') as f:
    pickle.dump(id_tag_1, f)

with open('Data_preprocessing\\id_tag\\id_tag_2.dic', 'wb') as f:
    pickle.dump(id_tag_2, f)

with open('Data_preprocessing\\id_tag\\id_tag_3.dic', 'wb') as f:
    pickle.dump(id_tag_3, f)

with open('Data_preprocessing\\id_tag\\id_tag_4.dic', 'wb') as f:
    pickle.dump(id_tag_4, f)

with open('Data_preprocessing\\id_tag\\id_tag_5.dic', 'wb') as f:
    pickle.dump(id_tag_5, f)

with open('Data_preprocessing\\id_tag\\id_tag_6.dic', 'wb') as f:
    pickle.dump(id_tag_6, f)