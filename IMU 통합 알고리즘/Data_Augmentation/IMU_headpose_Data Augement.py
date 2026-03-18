import numpy as np

# 1: 스케일링 (Scaling) - 팀원분 코드 베이스
def augment_scaling(data, sigma=0.1):
    """
    [효과] 운전자의 조작 '강도' 변화 시뮬레이션 (과격한 운전 vs 얌전한 운전)
    데이터 전체에 0.9 ~ 1.1 사이의 값을 곱해 크기를 키우거나 줄임.
    """
    scalar = np.random.normal(1.0, sigma)
    return data * scalar

# 2: 지터링 (Jittering) - 노이즈 추가
def augment_jittering(data, noise_level=0.05):
    """
    [효과] 노면 상태(방지턱, 비포장도로)에 따른 차체 진동 및 센서 잡음 시뮬레이션
    원본 데이터 위에 미세한 가우시안 노이즈(백색 소음)를 얹음.
    """
    noise = np.random.normal(0, noise_level, size=data.shape)
    return data + noise

# 3: 타임 마스킹 (Time Masking) - 센서 유실 시뮬레이션
def augment_time_masking(data, mask_ratio=0.1):
    """
    [효과] 통신 불량이나 센서 오류로 인해 찰나의 순간(예: 0.3초) 데이터가 끊긴 최악의 상황 시뮬레이션
    윈도우의 특정 구간을 0으로 지워버림. 모델이 일부 데이터가 없어도 문맥을 파악하게 만듦.
    """
    aug_data = data.copy()
    window_length = len(aug_data)
    mask_size = int(window_length * mask_ratio) # 윈도우의 10% 구간 계산
    
    # 지워버릴 랜덤 시작점 찾기
    mask_start = np.random.randint(0, window_length - mask_size)
    aug_data[mask_start : mask_start + mask_size] = 0.0 # 해당 구간을 0으로 덮어씀
    
    return aug_data