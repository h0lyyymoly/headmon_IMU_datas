# 데이터 증강 기법
import pandas as pd
import numpy as np


def apply_scaling(df, sensor_cols, sigma=0.1):
    """
    [기법 1] 스케일링 (Scaling)
    - 효과: 전체 데이터의 진폭을 키우거나 줄여서 '과격한 운전'과 '얌전한 운전'을 시뮬레이션합니다.
    """
    aug_df = df.copy()
    # 센서 종류별로 0.9 ~ 1.1 사이의 랜덤한 스케일(배수)을 하나씩 뽑아서 전체에 곱해줍니다.
    # (평행우주의 다른 운전자가 운전한 것처럼 만들어버림!)
    scalars = np.random.normal(1.0, sigma, size=len(sensor_cols))
    aug_df[sensor_cols] = aug_df[sensor_cols] * scalars
    return aug_df

def apply_jittering(df, sensor_cols, noise_level=0.05):
    """
    [기법 2] 지터링 (Jittering) 
    - 효과: 비포장도로나 차체 진동, 저가형 센서의 '미세한 떨림(백색 소음)'을 시뮬레이션합니다.
    """
    aug_df = df.copy()
    # 센서 데이터의 모든 칸(row x col)마다 자잘한 노이즈를 생성해서 얹어줍니다.
    noise = np.random.normal(0, noise_level, size=aug_df[sensor_cols].shape)
    aug_df[sensor_cols] = aug_df[sensor_cols] + noise
    return aug_df

# ==========================================
# 🚀 메인 실행 부분
# ==========================================
if __name__ == "__main__":
    # 1. 반드시 시간순(8:2)으로 잘라둔 Train 데이터 파일명을 적어주세요!
    input_file = 'HeadMon_20260206_164002_headpose_imu_merge.csv' 
    output_file = 'HeadMon_20260206_164002_headpose_imu_merge_augmentation.csv'
    
    # 2. 증강을 적용할 순수 센서 컬럼들 (데이터에 맞게 수정 가능)
    # 팀의 IMU와 Headpose 컬럼명을 정확히 적어주세요.
    sensor_columns = ['AccX', 'AccY', 'AccZ', 'GyroX', 'GyroY', 'GyroZ', 'yaw', 'pitch', 'roll']

    try:
        print(f"📥 1. [{input_file}] 원본 데이터 읽어오는 중...")
        orig_df = pd.read_csv(input_file)
        
        print("🪄 2. 스케일링(과격/얌전 운전) 데이터 생성 중...")
        scaled_df = apply_scaling(orig_df, sensor_columns)
        
        print("🪄 3. 지터링(울퉁불퉁 도로/센서 노이즈) 데이터 생성 중...")
        jittered_df = apply_jittering(orig_df, sensor_columns)
        
        print("🔗 4. [원본 1배 + 스케일링 1배 + 지터링 1배] 합체 중!!!")
        # 3개의 표를 위아래로 길게 이어 붙입니다.
        final_augmented_df = pd.concat([orig_df, scaled_df, jittered_df], ignore_index=True)
        
        # 새로운 CSV로 저장
        final_augmented_df.to_csv(output_file, index=False)
        
        print("\n🎉 [대성공] 3배 뻥튀기 증강 완료!")
        print(f"원본 데이터 길이: {len(orig_df)}줄")
        print(f" 최종 데이터 길이: {len(final_augmented_df)}줄 (정확히 3배!)")
        print(f" 저장된 파일명: {output_file}")
        
    except FileNotFoundError:
        print(f"🚨 에러: '{input_file}' 파일을 찾을 수 없습니다. 파일명과 위치를 확인해주세요!")