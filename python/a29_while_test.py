import time

def main():
    num = 0
    fps = 60
    delay_time = 1 / fps  # 프레임당 시간 (1초를 FPS로 나눈 값)

    target_tick = time.time() + 5  # 5초 후의 시간 설정
    while time.time() < target_tick:
        num += 1  # tick 카운트
        time.sleep(delay_time)  # FPS에 맞춰 대기

    print(f"num of ticks in 5 seconds -> {num}")  # 문자열 포맷팅

if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    # Call main function when executed directly  
    main()
