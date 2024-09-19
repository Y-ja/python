def main():
    output_a = 0 
    print(output_a)
    
    while True: 
        output_a = "안녕안녕하세여...".find("안녕", output_a)
        if output_a == -1:  # 찾지 못했을 경우 종료
            break
        print(output_a)
        output_a += 2  # 다음 검색을 위해 인덱스를 증가시킵니다.

    print("안녕1" in "하세요")  # '안녕1'이 '하세요'에 포함되어 있는지 확인
    
    a = "10,20,30,40,50".split(",")  # 쉼표로 분리합니다.
    print(a)
    
    st1 = "\n1".join(a)  # 리스트를 줄바꿈으로 연결합니다.
    print(st1)

if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    main()

