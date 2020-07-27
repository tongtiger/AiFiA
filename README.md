# AiFiA

1. 파일명에 [Prepare]가 붙어있는 파일들은 '파레토 법칙' 팀이 협업하면서 작성한 코드들로, 최종 결과에 반영된 것도 있고 아닌 것도 있습니다. 
   해당 파일들은 확인해보지 않으셔도 될 듯 합니다.

2. 'FastText_training.py' 파일은 FastText 모델 학습에 필요한 데이터를 만들고, 이를 이용해 학습하는 코드입니다. 
   학습에 필요한 데이터는 카카오 아레나 대회에서 주어진 'train.json'에서 플레이리스트 이름과 태그를 추출하여 만들었습니다.
   이 때 만들어진 데이터는 다음과 같은 형식으로 만들어졌습니다.
   
   [['띄어쓰기로 구분된 플레이리스트 이름', '해당 플레이리스트에 속한 태그1', 
   '해당 플레이리스트에 속한 태그2', '해당 플레이리스트에 속한 태그3'],
    ['띄어쓰기로 구분된 플레이리스트 이름', '해당 플레이리스트에 속한 태그1',
    '해당 플레이리스트에 속한 태그2', '해당 플레이리스트에 속한 태그3'],
    ['띄어쓰기로 구분된 플레이리스트 이름', '해당 플레이리스트에 속한 태그1', 
    '해당 플레이리스트에 속한 태그2', '해당 플레이리스트에 속한 태그3'] .... ]

3. 'inference.py'에서 예측모델에 사용되는 자료는 다음과 같습니다. 

    1) tag_name.list: 학습 데이터에서 주어진 태그의 리스트입니다.
    2) music_tag.dic: 음악별로 할당된 태그를 {'음악1':[태그1, 태그2, 태그3, ...], 
    '음악2':[태그1, 태그2, 태그3, ...], ...} 형식의 딕셔너리로 정리한 자료입니다.
    3) tag_music_freq.dic: 태그별로 할당된 음악을 {'태그1':[음악1, 음악2, 음악3, ...],
    '태그2':[음악1, 음악2, 음악3, ...], ...} 형식의 딕셔너리로 정리한 자료입니다.
    
    위 자료들의 제작은 inference.py에 기재해놓았습니다.

4. 예측 모델 작동 원리

  저희 팀은 주어진 문제를 4가지 유형으로 분류했습니다. 
  
  1) Type1: 태그x, 이름x, 노래O
  2) Type2: 태그X, 이름O, 노래X
  3) Type3: 태그O, 이름X, 노래O
  4) Type4: 태그O, 이름O, 노래X
  
  4가지 유형으로 분류된 문제마다 다른 예측 방법을 적용했으며, 4가지 유형 모두 기본적으로 '투표' 원리를 사용했습니다.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

5. 데이터 처리 문제로 최종 결과에는 반영되지 않았지만 위의 '투료'를 위해 train.json에 포함되지 않은 곡들(약 9~10만)의 태그를 예측하는 모델이 train.py로 재현 가능합니다.
   mel_spectrogram를 일부 추출하여 태그를 예측하도록 되어 있습니다.
   
   train.json로부터 포함되는 615142개의 노래에 대하여 '키'로 노래의 id, '값'으로 각 노래가 포함된 플레이리스트에 붙은 태그를 중복 없이 넣은 리스트를 갖는 딕셔너리(1) 파일을 만들었습니다.
   
   train.json에서 사용된 태그의 총 개수를 확인했으며 효율적인 처리와 정확도를 위해 train.json에서 10회 이상 사용된 태그(2780개)만을 사용하기로 했습니다.
   나머지 태그들은 gensim의 FastText를 사용하여 2780개의 대표 태그들 중 가장 가까운 태그를 구하여, 대표 태그를 '키'로 갖고 '값'으로 각 대표 태그와 가장 가깝다고 나온 태그들을 리스트로 갖는   딕셔너리(2) 파일을 만들었습니다.
   
   위의 딕셔너리의 '키'가 숫자가 아니라 태그 문자 상태였기 때문에 편의를 위해 대표 키들로만 이루어진 리스트를 sort()시켜 순서대로 0부터 2779의 숫자를 할당했고 앞서 생성한 딕셔너리를 가공하여 대   표태그도 각 '값'의 리스트에 넣어주고 키 값은 0~2779로 바꿔준 딕셔너리(3)를 다시 생성했습니다.
   
   처음에 만든 61만 곡의 딕셔너리(1)과 위의 딕셔너리(3)을 이용하여 61만 곡에 대해 각각 2780개의 대표 태그 중 어떤 태그를 갖는지 0과 1로 구분한 csv파일을 만들었습니다.
   대표 태그가 아닌 태그를 갖더라도 딕셔너리(3)을 이용하여 대표태그로 치환하여 해당 대표태그를 갖는다는 것으로 처리했습니다.
   완성된 csv파일은 index가 ('id', 0, 1, 2, ... , 2779)로 되어 있으며 각 'id'마다 0에서 2779의 대표 태그를 갖는 경우 1로 아니면 0으로 되어 있는 파일입니다.
   
   문의를 통해 mel_spectrogram이 각 노래의 20에서 50초 구간에 해당하는 데이터인 것을 알게 되었고, 대부분 (48, 1876)의 shape를 가지고 있었기 때문에 데이터 처리의 효율과 정확성을 위해 30초에 해   당하는 48에서 마지막 6개, 즉 3.75초에 해당하는 데이터를 사용하였습니다. 가요 등의 노래에서 주요 파트가 대부분 60~120초 사이에 등장하는 것으로 보고 주요 파트와 가장 근접한 마지막 구간을 택   했으며 1초나 4초가 가장 결과가 좋았다는 논문을 찾고 3.75초에 해당하는 데이터를 사용하기로 결정했습니다.
   
   61만 곡의 mel_spectrogram에서 마지막 6개만을 가져와 (615142, 6, 1876, 1)의 shape를 갖는 새로운 npy파일을 만드려고 했지만 61만 곡 전부가 (6, 1876)의 shape를 가지고 있지 않아서 이 곡들   은 train data에서 제외하게 되었습니다. 앞서 제외한 8만여 곡을 제외한 53만 곡을 train data로 하고 싶었지만 데이터 크기가 너무 커서 미처 처리를 할 수 없었고 53만 곡 중 처음 8만 5천여 곡만   을 train data로 사용하게 되었으며 이에 따라 앞서 만든 csv파일도 8만 5천여개로 개수를 맞춰주었습니다.
   
   모델은 mel_spectrogram을 X로 csv를 pandas로 불러올 때 index_col='id'로 하여 대표태그 해당 유무만을 갖는 npy파일을 Y로 하여 CNN을 사용하여 학습시켰으며 정확도를 알아보기 위해 0.5%는 테   스트로 분류하여 정확도를 측정했으며 99%이상의 정확도를 얻었습니다.
   
   학습시킨 모델에 train.json에 포함되지 않았던 9만여 곡의 mel_spectrogram을 넣어 태그를 예측하고 정확도가 높은 순으로 10개의 태그를 가져오도록 할 예정이었지만 이 과정에서 오류가 발생하면서   제출 기한에 맞춰 해결하지 못하고 마치게 되었습니다.
   
   하드웨어의 한계로 8만 5천여 곡만을 학습시키게 되었지만 원래 계획대로 53만여 곡을 학습시켰다면 정확도는 더 높아졌을 것으로 생각되며, 시간적인 문제로 callback을 사용하여 최적의 모델을 만들   수 없었고 1회 실행에서 이미 accuracy가 0.99이상이 되어 1회 실행시킨 모델을 사용하게 되었던 점, 그리고 최종적인 예측 과정에서 태그를 불러오는 곳에서 발생한 오류로 최종 결과에 반영시킬 수 없   었던 점이 아쉬웠습니다.
   
   
  
    
