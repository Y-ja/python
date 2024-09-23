import random
import time

def main():
    random.seed(time.time())
    num = [1, 2, 3, 4, 5, 6 ,7,8,9,10]  # 리스트 생성
    
    for _ in range(100):
        print(random.random())  # 0.0과 1.0 사이의 랜덤 실수 출력
        print(random.choice(num))  # 리스트에서 랜덤 요소 선택
        print(random.choices(num , k = 2))
        print(random.sample(num , 2))
        
        time.sleep(0.5)

if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    main()
