def test():
    print("함수가 호출 되었습니다")
    print("C 지점")
    yield "first"

def main():
    print("A 지점")
    generator = test()
    
    # for 문으로 generator 사용
    for text in generator:
        print(text)  # 'first' 출력
    
    print("B 지점")
    
    # D 지점 추가
    print("함수가 호출 되었습니다")
    print("D 지점")
    print("second")

if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    main()
