import sentencepiece as spm
import pickle

'''
#모델 Hyperparameter 설정
templates= '--input={} \
--pad_id={} \
--bos_id={} \
--eos_id={} \
--unk_id={} \
--model_prefix={} \
--vocab_size={} \
--character_coverage={} \
--model_type={}'

#소설 파일로 학습
train_input_file = "C:\\Users\\tongt\\PycharmProjects\\Melon\\data\\4BE00006.txt"
pad_id=0  #<pad> token을 0으로 설정
vocab_size = 770 # vocab 사이즈
prefix = 'train_spm' # 저장될 tokenizer 모델에 붙는 이름
bos_id=1 #<start> token을 1으로 설정
eos_id=2 #<end> token을 2으로 설정
unk_id=3 #<unknown> token을 3으로 설정
character_coverage = 1.0 # to reduce character set
model_type ='unigram' # Choose from unigram (default), bpe, char, or word

cmd = templates.format(train_input_file,
                pad_id,
                bos_id,
                eos_id,
                unk_id,
                prefix,
                vocab_size,
                character_coverage,
                model_type)

#Tokenizer 학습
#'trainer_interface.cc(452) LOG(INFO) Found null character. The corpus must be encoded in utf-8.'라는 예외가 발생할 수 있는데,
#Tokenizer 학습에 영향을 미치지 않기에 그냥 무시하면 된다고 한다.
#학습이 완료되면 'True'를 반환함과 동시에, 'prefix.model'과 'prefix.vocab'이 생성된다.
spm.SentencePieceTrainer.Train(cmd)
'''

#학습된 Tokenizer 모델 불러오기
sp = spm.SentencePieceProcessor()
sp.Load('train_spm.model')

# 문장 양 끝에 <s> , </s> 추가, 'SetEncodeExtraOptions'를 이용하는 대신 모든 데이터에 일일이 <s>,</s>를 추가해도 됨.
sp.SetEncodeExtraOptions('bos:eos')


#pickle 이용하여 플레이리스트 제목으로 이루어진 리스트 불러오기
with open("C:\\Users\\tongt\\PycharmProjects\\Melon\\playlist_name_list.p", "rb") as playlist_name_list:
    playlist = pickle.load(playlist_name_list)

#문자열로 Tokenize하기
tokens = []

for i in range(len(playlist)):
    if i == 0:
        token = sp.EncodeAsPieces(playlist[i])
        tokens.append(token)
    else:
        tokens.append(sp.EncodeAsPieces(playlist[i]))

#첫번째 플레이리스트에만 오작동하는 현상 수정을 위한 코드
'''
for i in range(len(tokens)):
    if type(tokens[i]) != list:
       print("token[{}]".format(i), tokens[i])
    else:
       pass
'''

#ID로 Tokenize하기
token_ids = []

for i in range(len(playlist)):
    if i == 0:
        token_id = sp.EncodeAsIds(playlist[i])
        token_ids.append(token_id)
    else:
        token_ids.append(sp.EncodeAsIds(playlist[i]))

#첫번째 플레이리스트에만 오작동하는 현상 수정을 위한 코드
'''
for i in range(len(token_ids)):
    if type(token_ids[i]) != list:
       print("token_ids[{}]".format(i), token_ids[i])
    else:
       pass
'''

#딕셔너리 생성(Key: 플레이리스트 제목, Value: 문자열 토큰, 토큰 ID
tokenized_playlist = {}

for i in range(len(playlist)):
    tokenized_playlist[playlist[i]] = [tokens[i], token_ids[i]]

#플레이리스트 제목 토큰화 파일 저장
#python object to file
with open("C:\\Users\\tongt\\PycharmProjects\\Melon\\data\\tokenized_playlist_id.p", "wb") as tokenized_playlist_id:
    pickle.dump(token_ids, tokenized_playlist_id)
tokenized_playlist_id.close()

with open("C:\\Users\\tongt\\PycharmProjects\\Melon\\data\\tokenized_playlist_str.p", "wb") as tokenized_playlist_str:
    pickle.dump(tokens, tokenized_playlist_str)
tokenized_playlist_str.close()


