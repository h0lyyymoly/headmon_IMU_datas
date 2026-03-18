#조건부 필터링

import pandas as pd

# 1. 데이터 불러오기 (작업하신 최종 파일명을 넣어주세요)
df = pd.read_csv('HeadMon_20260130_174348_timestamp_sec_label_10HZ.csv')

# ==========================================
# 2. 🎯 원하는 시간 구간과 남길 열(Column) 설정
# ==========================================
start_time = 140   # 시작 시간 (초 단위, 예: 10초부터)
end_time = 190    # 종료 시간 (초 단위, 예: 50초까지)

# 남기고 싶은 열의 이름만 리스트 안에 적어주세요. 
# (예: 가속도 데이터와 라벨만 남기고 싶을 때)
columns_to_keep = ['Timestamp', 'AccX', 'AccY', 'AccZ', 'GyroX' , 'GyroY', 'GyroZ' ,'Label']

# 3. 조건에 맞게 데이터 자르기
# Timestamp가 start_time 이상, end_time 이하인 조건(mask) 만들기
mask = (df['Timestamp'] >= start_time) & (df['Timestamp'] <= end_time)

# .loc[행 조건, 열 리스트]를 사용해 원하는 부분만 쏙 빼냅니다.
sliced_df = df.loc[mask, columns_to_keep].copy()

# ==========================================
# 4. ⭐️ Timestamp를 0초부터 시작하도록 초기화! (0.0, 0.1, 0.2 ...)
# ==========================================
# 잘라낸 데이터의 첫 번째 Timestamp 값을 기준점으로 잡습니다.
first_time = sliced_df['Timestamp'].iloc[0]

# 모든 Timestamp에서 첫 번째 값을 빼서 0으로 만들고, 소수점 찌꺼기를 방지합니다.
# (이전 단계에서 10Hz로 변환하셨기 때문에 자연스럽게 0.1초 간격이 됩니다.)
sliced_df['Timestamp'] = (sliced_df['Timestamp'] - first_time).round(3)

# 4. 자른 데이터를 새로운 파일로 저장하기
sliced_df.to_csv('HeadMon_20260130_174348_timestamp_sec_label_10HZ_50s.csv', index=False)

print(f"성공적으로 데이터를 잘랐습니다! 남은 데이터 크기(행, 열): {sliced_df.shape}")

