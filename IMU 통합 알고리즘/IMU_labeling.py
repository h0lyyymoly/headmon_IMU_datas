import pandas as pd

# 1. 파일 불러오기
df = pd.read_csv('HeadMon_20260130_174348_timestamp_sec.csv')

# 'Label' 열이 없다면 새로 생성 (기본값 0)
if 'Label' not in df.columns:
    df['Label'] = 0

# ==========================================
# 2. 🎯 라벨링할 구간들을 리스트로 설정하세요!
# ==========================================
# 형식: {'start': 시작시간, 'end': 종료시간, 'label': 넣을라벨}
intervals = [
    {'start': 98, 'end': 102, 'label': 1},
    {'start': 131, 'end': 135, 'label': 2},
    {'start': 144, 'end': 149, 'label': 2},
    {'start': 156, 'end': 161, 'label': 1},
    {'start': 183, 'end': 187, 'label': 2},
    {'start': 225, 'end': 231, 'label': 2},
    {'start': 245, 'end': 250, 'label': 2},
    {'start': 277, 'end': 280, 'label': 1},
    {'start': 288, 'end': 291, 'label': 1},
    {'start': 303, 'end': 308, 'label': 1},
    {'start': 337, 'end': 342, 'label': 2},
    {'start': 374, 'end': 380, 'label': 1},
    {'start': 391, 'end': 396, 'label': 1}
    # 필요하신 만큼 위 형식에 맞춰 계속 추가하시면 됩니다!
]

# 3. 반복문을 돌면서 설정한 구간들에 라벨 값을 한 번에 적용
for item in intervals:
    mask = (df['Timestamp'] >= item['start']) & (df['Timestamp'] <= item['end']+1)
    df.loc[mask, 'Label'] = item['label']

# 4. 결과를 새로운 파일로 저장하기
df.to_csv('HeadMon_20260130_174348_timestamp_sec_label.csv', index=False)

print(f"총 {len(intervals)}개 구간의 라벨링이 완료되어 'sample_dummy_IMU_multi_labeled.csv'로 저장되었습니다!")