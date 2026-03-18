# IMU 데이터 불러와서 50hz -> 10hz으로 평균으로 통합 후 Timestamp 재설정. 
# Label  소수점에서 int로 바꾸기.
# NULL이 있을시 선형보간


import pandas as pd
import numpy as np 

#def max_abs(x):     #절댓값 가장 큰 값을 찾는 함수.. x가 Series 클래스의 객체여야함.. 즉 x는 1차원 데이터(ex. 행(튜플))
#    if len(x) == 0:
#        return np.nan
#    return x.iloc[x.abs().argmax()]


# 데이터 불러오기
imu_df = pd.read_csv('HeadMon_20260130_174348_timestamp_sec_label.csv') #IMU csv 불러오기
#imu_df는 DataFrame(클래스)의 객체

# Timestamp (단위가 초(s)이기 때문에 unit = 's'... 내 Timestamp를 datetime으로 변환...숫자들(Timestanp)이 초 단위(unit='s')라는걸 알려주는거임. 
imu_df['Timestamp'] = pd.to_datetime(imu_df['Timestamp'], unit = 's')

# (datetime으로 바뀐)Timestamp을 기준열(index)로 설정
imu_df = imu_df.set_index('Timestamp')

# 새로운 imu_10df .. imu_df 보존 .. resample된 imu_df = imu_10df
# 밀리초(ms)와 초(s)의 관계 -> 1초(s) = 1000밀리초(ms) .. 1밀리초(ms) = 0.001초(s)
imu_10df = imu_df.resample('100ms').mean()
#imu_10df = imu_df.resample('100ms').agg({
    # 주행 동작: 부드러운 흐름
    #'GyroZ': 'mean',   # 좌우 회전율
    #'AccY': 'mean',    # 앞뒤 가속도
    #'AccX': 'mean',    # 좌우 원심력
    #'AccZ': 'mean',    # 위아래 최대 충격량 + 위아래 진동(거칠기)
    #'GyroY': 'mean',   # 앞뒤 끄덕임 최대치 (방지턱)
    #'GyroX': 'mean'    # 좌우 뒤뚱거림 최대치 (비포장)
    
    # 주행 환경: 순간 충격 & 흔들림
    #'Acc_Z': [max_abs, 'std'],   # 위아래 최대 충격량 + 위아래 진동(거칠기)
    #'Gyro_Y': max_abs,           # 앞뒤 끄덕임 최대치 (방지턱)
    #'Gyro_X': max_abs            # 좌우 뒤뚱거림 최대치 (비포장)
    #})

# 만약 결측값(NaN)이 있을경우 linear(선형 방식)으로 보간한다. 
imu_10df = imu_10df.interpolate(method = 'linear', limit = 3)
#결측값(NaN) 선형 보간 (limit = 3은 너무 긴 끊김은 위험하므로 3칸까지만 허용)
#imu_10df = imu_10df.interpolate(method='linear', limit=3) 

# 지금 기준 index가 Timestamp. 그래서 Timestamp를 일반 column으로 바꿔주고 기준 index를 다시 0,1,2,3...으로 만들어주기
imu_10df = imu_10df.reset_index()

# 열 : Timestamp가 지금은 datetime 형태로 있기 때문에 다시 초(s) 형태로 바꾸기
imu_10df['Timestamp'] = (imu_10df['Timestamp'] - pd.to_datetime(0,unit='s')).dt.total_seconds() 

# 소수점 찌꺼기 제거. 반올림. 소수점 여섯번째자리
imu_10df = imu_10df.round(6)

# 평균 계산과 선형 보간 때문에 소수점으로 변한 Label 값을 반올림 후 정수(int)로 변환
imu_10df['Label'] = imu_10df['Label'].round().astype(int)

# 이제 Timestamp까지 다 정리하고 전처리된(50hz->10hz) 데이터들의 파일(csv) 저장
imu_10df.to_csv('HeadMon_20260130_174348_timestamp_sec_label_10HZ.csv',index = False)

print(f"(행, 열) : {imu_10df.shape}")