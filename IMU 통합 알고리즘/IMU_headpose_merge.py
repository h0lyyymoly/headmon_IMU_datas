# IMU데이터랑 headpose 데이터값 하나의 csv로 (Timestamp)통합시키기
import pandas as pd

imu_df = pd.read_csv('HeadMon_20260130_174348_timestamp_sec_label_10HZ_50s.csv')

headpose_df = pd.read_csv('d7_headpose.csv')

# 'Timestamp'를 기준으로 교집합(how = 'inner') 병합
# inner은 교집합. 즉 Timestamp에서 속성값이 똑같은 값들끼리만 merge. 아니라면 버려짐
final_dataset = pd.merge(headpose_df, imu_df, on='Timestamp', how='inner')

# Label 열의 0.0, 1.0, 2.0 들을 깔끔한 정수 0, 1, 2 로 강제 변환!
final_dataset['Label'] = final_dataset['Label'].astype(int)

# 잘 바뀌었는지 확인!
print(final_dataset['Label'].head())

# 2. 데이터가 잘 합쳐졌는지 검사하기
print(f"완성된 데이터셋 크기 (행, 열): {final_dataset.shape}")

# 3. 혹시라도 빈칸(NaN)이 숨어있는지 탐지기 돌리기 (안전제일!)
print("\n결측치(NULL) 개수 확인:")
print(final_dataset.isnull().sum())

# 4. 합쳐진 표의 앞부분 스윽 구경하기
print("\n----최종 데이터 미리보기----")
print(final_dataset.head())

# =====================================================================
# 💾 최종 머신러닝/딥러닝용 CSV 파일로 굽기!
# =====================================================================
final_dataset.to_csv('sample.csv', index=False)
print("\n****파일이 성공적으로 저장되었습니다****")