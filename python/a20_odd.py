def main():
    a = int(input("숫자를 넣으세요 -> "))
    if a % 2 == 0:
        print(f"{a}는 짝수 입니다")
    else:
        print(f"{a}는 홀수 입니다")    

if __name__ == "__main__":  
    # 직접 실행 시_main 함수 호출
    main() 
