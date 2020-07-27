import pickle

id_tag_token_0 = pickle.load(open('Data_preprocessing\\id_tag_token\\id_tag_token_0.dic', 'rb'))
id_tag_token_1 = pickle.load(open('Data_preprocessing\\id_tag_token\\id_tag_token_1.dic', 'rb'))
id_tag_token_2 = pickle.load(open('Data_preprocessing\\id_tag_token\\id_tag_token_2.dic', 'rb'))
id_tag_token_3 = pickle.load(open('Data_preprocessing\\id_tag_token\\id_tag_token_3.dic', 'rb'))
id_tag_token_4 = pickle.load(open('Data_preprocessing\\id_tag_token\\id_tag_token_4.dic', 'rb'))
id_tag_token_5 = pickle.load(open('Data_preprocessing\\id_tag_token\\id_tag_token_5.dic', 'rb'))
id_tag_token_6 = pickle.load(open('Data_preprocessing\\id_tag_token\\id_tag_token_6.dic', 'rb'))

id_tag_token = {}

id_tag_token.update(id_tag_token_0)
id_tag_token.update(id_tag_token_1)
id_tag_token.update(id_tag_token_2)
id_tag_token.update(id_tag_token_3)
id_tag_token.update(id_tag_token_4)
id_tag_token.update(id_tag_token_5)
id_tag_token.update(id_tag_token_6)

with open('Data_preprocessing\\id_tag_token\\id_tag_token.dic', 'wb') as f:
    pickle.dump(id_tag_token, f)