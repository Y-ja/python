import datetime

def main():
    # datetime을 활용해 month 데이터를 얻어와서 조건문으로 
    # 3~5월 포함 봄, 6~8월 여름, 9~11월은 가을, 나머지는 겨울을 출력하는 프로그램
    month = datetime.datetime.now().month  # 현재 월을 가져옵니다.

    if 3 <= month <= 5:
        print("봄")
    elif 6 <= month <= 8:
        print("여름")
    elif 9 <= month <= 11:
        print("가을")
    else:
        print("겨울")

if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    main()

