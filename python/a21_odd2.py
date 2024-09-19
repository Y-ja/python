def main():
    try:
        grade = float(input("학점을 입력하세요 (0.0 ~ 4.5): "))
        
        # 학점이 4.5를 넘는 경우 에러 메시지 출력
        if grade > 4.5:
            print("학점은 4.5를 넘을 수 없습니다.")
            return
        
        if grade >= 4.5:
            print("신")
        elif grade >= 4.2:
            print("교수님의 사랑")
        elif grade >= 3.5:
            print("현 테제의 수호자")
        elif grade >= 2.8:
            print("일반인")
        elif grade >= 2.3:
            print("일탈을 꿈꾸는 소시민")
        elif grade >= 1.75:
            print("오락문화 선구자")
        elif grade >= 1.0:
            print("불가촉천민")
        elif grade >= 0.5:
            print("자벌레")
        elif grade >= 0:
            print("플랑크톤")
        else:
            print("시대를 앞서가는 혁명의 씨앗")
    
    except ValueError:
        print("유효한 숫자를 입력하세요.")

if __name__ == "__main__":  
    main()
