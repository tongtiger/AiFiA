import pickle
from gensim import models
from tqdm import tqdm

tag_morethan_10 = pickle.load(open('Data_preprocessing\\tag_10\\tag_morethan_10.list', 'rb'))
tag_lessthan_10 = pickle.load(open('Data_preprocessing\\tag_10\\tag_lessthan_10.list', 'rb'))

tag_10_tag = {}

for tag in tag_morethan_10:
    tag_10_tag[tag] = []

ko_model = models.fasttext.load_facebook_model('cc.ko.300.bin')

for tag in tag_lessthan_10:
    similarity = {}
    for tag_10 in tag_morethan_10:
        similarity[tag_10] = m_fasttext.similarity(tag, tag_10)
    similarity = sorted(similarity.items(), key = lambda x : x[1], reverse=True)
    print(similarity)
