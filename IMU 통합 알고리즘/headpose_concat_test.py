import pandas as pd

# 1. 합칠 파일들의 이름을 리스트로 묶어줍니다. (실제 파일 이름으로 바꿔주세요!)
file_names = [
    'headpose_part1.csv', 
    'headpose_part2.csv', 
    'headpose_part3.csv', 
    'headpose_part4.csv'
]

# 2. 빈 리스트를 만들고, 파일들을 하나씩 읽어서(DataFrame) 리스트에 담습니다.
df_list = []
for file in file_names:
    temp_df = pd.read_csv(file)
    df_list.append(temp_df)

# =======================================================
# 💡 [꿀팁] 위 2번 과정을 파이썬의 '리스트 컴프리헨션'으로 한 줄로 줄일 수도 있습니다!
# df_list = [pd.read_csv(file) for file in file_names]
# =======================================================

# 3. ⭐️ 대망의 병합! pd.concat()으로 4개의 데이터를 위아래로 촥! 붙입니다.
# ignore_index=True : 각 파일이 가지고 있던 출석번호(0,1,2..)를 무시하고 
# 0부터 끝까지 새로운 출석번호로 깔끔하게 덮어씌우는 핵심 옵션입니다!
headpose_df = pd.concat(df_list, ignore_index=True)

# 4. (선택사항이자 안전장치) 만약 파일 순서가 뒤죽박죽이었다면 시간 순서대로 정렬해줍니다.
# 'Timestamp' 부분은 실제 시간 열 이름으로 바꿔주세요.
headpose_df = headpose_df.sort_values(by='Timestamp')

# 5. 정렬하면서 엉킨 출석번호를 다시 리셋! 정렬하면서 처음 정해졌던 기준 인덱스가 같이 가기 떄문에 기준 인덱스가 꼬임. 그래서 다시 기준 인덱스를 정렬해줌. 
headpose_df = headpose_df.reset_index(drop=True)

# 6. 하나로 예쁘게 합쳐진 데이터를 확인합니다!
print(headpose_df.head()) # 첫 5줄 확인
print(f"총 데이터 개수: {len(headpose_df)}개")

# 원하신다면 합쳐진 통본을 저장해둘 수도 있습니다.
# headpose_df.to_csv('headpose_total.csv', index=False)