from math import tan, sin, radians
import math as m 
import numpy as np

def main():
    try:
        angle = 30  # 각도
        # 각도를 라디안으로 변환하고 삼각 함수 호출
        radians_angle = radians(angle)  # math의 radians 사용
        print(tan(radians_angle))  # math의 tan 사용
        print(sin(radians_angle))   # math의 sin 사용
        
        # numpy를 사용한 계산 (추가 예시)
        print(np.tan(np.radians(angle)))  # numpy의 tan과 radians 사용
        print(np.sin(np.radians(angle)))   # numpy의 sin과 radians 사용
    except Exception as e:
        print(f"기타 오류: {e}")

if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    # Call main function when executed directly  
    main()
