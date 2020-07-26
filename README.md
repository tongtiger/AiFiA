# AiFiA

1. 파일명에 [Prepare]가 붙어있는 파일들은 '파레토 법칙' 팀이 협업하면서 작성한 코드들로, 최종 결과에 반영된 것도 있고 아닌 것도 있습니다. 
   해당 파일들은 확인해보지 않으셔도 될 듯 합니다.

2. 'FastText_training.py' 파일은 FastText 모델 학습에 필요한 데이터를 만들고, 이를 이용해 학습하는 코드입니다. 
   학습에 필요한 데이터는 카카오 아레나 대회에서 주어진 'train.json'에서 플레이리스트 이름과 태그를 추출하여 만들었습니다.
   이 때 만들어진 데이터는 다음과 같은 형식으로 만들어졌습니다.
   
   [['띄어쓰기로 구분된 플레이리스트 이름', '해당 플레이리스트에 속한 태그1', '해당 플레이리스트에 속한 태그2', '해당 플레이리스트에 속한 태그3'],
    ['띄어쓰기로 구분된 플레이리스트 이름', '해당 플레이리스트에 속한 태그1', '해당 플레이리스트에 속한 태그2', '해당 플레이리스트에 속한 태그3'],
    ['띄어쓰기로 구분된 플레이리스트 이름', '해당 플레이리스트에 속한 태그1', '해당 플레이리스트에 속한 태그2', '해당 플레이리스트에 속한 태그3'] .... ]

3. 'inference.py'에서 예측모델에 사용되는 자료는 다음과 같습니다. 

    1) tag_name.list: 학습 데이터에서 주어진 태그의 리스트입니다.
    2) music_tag.dic: 음악별로 할당된 태그를 {'음악1':[태그1, 태그2, 태그3, ...], '음악2':[태그1, 태그2, 태그3, ...], ...} 형식의 딕셔너리로 정리한 자료입니다.
    3) tag_music_freq.dic: 태그별로 할당된 음악을 {'태그1':[음악1, 음악2, 음악3, ...], '태그2':[음악1, 음악2, 음악3, ...], ...} 형식의 딕셔너리로 정리한 자료입니다.
    
    위 자료들의 제작은 inference.py에 기재해놓았습니다.

4. 예측 모델 작동 원리

  저희 팀은 주어진 문제를 4가지 유형으로 분류했습니다. 
  
  1) Type1: 태그x, 이름x, 노래O
  2) Type2: 태그X, 이름O, 노래X
  3) Type3: 태그O, 이름X, 노래O
  4) Type4: 태그O, 이름O, 노래X
  
  4가지 유형으로 분류된 문제마다 다른 예측 방법을 적용했으며, 4가지 유형 모두 기본적으로 '투표' 원리를 사용했습니다. 
  
  

   
    
