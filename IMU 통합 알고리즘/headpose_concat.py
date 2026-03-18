# headpose 값 끼리 통합시키기.

import pandas as pd

#file_names = ['HeadMon_20260206_163732__/HeadMon_20260206_163732_headpose_1.csv',
            #'HeadMon_20260206_163732__/HeadMon_20260206_163732_headpose_2.csv',
            #'HeadMon_20260206_163732__/HeadMon_20260206_163732_headpose_3.csv',
            #'HeadMon_20260206_163732__/HeadMon_20260206_163732_headpose_4.csv']


file_names = ['HeadMon_20260206_164002_/HeadMon_20260206_164002_headpose_1.csv',
            'HeadMon_20260206_164002_/HeadMon_20260206_164002_headpose_2.csv',
            'HeadMon_20260206_164002_/HeadMon_20260206_164002_headpose_3.csv',
            'HeadMon_20260206_164002_/HeadMon_20260206_164002_headpose_4.csv']

#file_names안에 있는 csv 파일들을 DataFrame의 객체로 바꾸기. 잘 분석하고 전처리하기 위해 표의 속성을 바꾸는 과정 
df_list = [pd.read_csv(temp) for temp in file_names ]
#df_list안에는 file_names에 있는 csv 파일이 DataFrame 형태로 표 통째로 들어있음.

#df_list 안에 있는 표(DataFrame)들 병합.
df_imu_headpose = pd.concat(df_list, ignore_index = True)

#timestamp 수정. 첫번째부터(0.0) 0.1씩 늘리기. 그리고 반올림. 
#통합 timestamp
df_imu_headpose['timestamp'] = (df_imu_headpose.index * 0.1).round(1)

#이때 'timestamp' 열 이름을 'Timestamp'로 바꾸기
df_imu_headpose = df_imu_headpose.rename(columns = {'timestamp' : 'Timestamp'})

# to_csv() : csv로 export
df_imu_headpose.to_csv('HeadMon_20260206_164002_headpose_concat.csv', index = False)

print("첫 10줄\n")
print(df_imu_headpose.head(10))
print("\n마지막 10줄\n")
print(df_imu_headpose.tail(10))

print(f"\n(행, 열) : {df_imu_headpose.shape}")

