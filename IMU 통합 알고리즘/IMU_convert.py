# Timestamp를 밀리초에서 초로 바꾸기

import pandas as pd

# 1. 데이터 불러오기
df = pd.read_csv('HeadMon_20260130_174348.csv')

# 2. 첫 번째 값을 0으로 맞추고 초(s) 단위로 변환
initial_timestamp = df['Timestamp'].iloc[0]
df['Timestamp'] = (df['Timestamp'] - initial_timestamp) / 1000.0

# 3. 원하는 소수점 형식으로 깔끔하게 고정하기 (문자열로 포맷팅)

# [추천] 소수점 셋째 자리(0.000)까지 표시 - IMU 데이터의 미세한 시간 간격 보존
df['Timestamp'] = df['Timestamp'].map('{:.3f}'.format)

# [옵션] 만약 무조건 소수점 첫째 자리(0.0)까지만 필요하시다면 아래 줄의 주석(#)을 풀고 위 줄을 지워주세요.
# df['Timestamp'] = df['Timestamp'].map('{:.1f}'.format)

# 4. 저장하기
df.to_csv('HeadMon_20260130_174348_timestamp_sec.csv', index=False)

print("소수점 정리가 완료되어 'sample_dummy_IMU_0sec_fixed.csv'로 저장되었습니다!")