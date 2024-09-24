import numpy as np

def main():
    x = np.array([4, 6, 7, 3, 2])  # x 배열 정의
    cond = np.array([0, 1, 2, 3, 4, 0, 1, 2, 3, 4])  # 인덱스 배열
    cond2 = np.random.randint(0, 5, 30)  # 0부터 4 사이의 랜덤 인덱스 30개 생성
    print(x[cond])  # x에서 cond 인덱스의 요소 출력
    print(x[cond2])

if __name__ == "__main__":  
    main()  # main 함수 호출
