import json
import pandas as pd
from gensim.models import FastText
from tqdm import tqdm

train_data = json.load(open('Data\\train.json', 'rb'))

tag_list = []
for playlist in train_data:
    for tag in playlist['tags']:
        tag_list.append(tag)
tag_list.sort()

tag_count = {}
for tag in tag_list:
    if tag in tag_count:
        tag_count[tag] += 1
    else:
        tag_count[tag] = 1

morethan_10 = {}
lessthan_10 = []
for tag, count in tag_count.items():
    if count >= 10:
        morethan_10[tag] = []
    else:
        lessthan_10.append(tag)

fasttext = FastText.load("FastText.model")

def most_similar_to_given(tag, given_tags, FastText_model):
    similarity = {}
    for given_tag in given_tags:
        similarity[given_tag] = FastText_model.similarity(tag, given_tag)
    similarity_sorted = sorted(similarity.items(), key = lambda x : x[1], reverse=True)
    return similarity_sorted[0][0]

for tag in tqdm(lessthan_10):
    prediction = most_similar_to_given(tag, morethan_10, fasttext)
    tag_frequency_morethan_10[prediction].append(tag)



