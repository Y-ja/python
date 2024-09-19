def main():
    a = "{}만원".format(500)
    b = "파이썬 공부 열심히 해서 {}만원 만들기".format(5000)
    c = "{2:5.2f}\n{1:10.2f}\n{0:015d}".format(3000, 4000, 5000)  # 인덱스 수정
    d = "{} {} {}".format(1, "문자열", True)
    e = "{:05d}".format(-52)
    
    # 출력
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    main()
