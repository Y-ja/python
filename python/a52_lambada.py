def call_10_times(func):
    """주어진 함수를 10번 호출합니다."""
    for i in range(10):
        func()

def print_hello():
    """'HELLO'를 출력합니다."""
    print("HELLO")

def power(item):
    """입력값의 제곱을 반환합니다."""
    return item * item

def under_3(item):
    """입력값이 3보다 작은지 확인합니다."""
    return item < 3

def main():
    # 리스트 정의
    li1 = [1, 2, 3, 4, 5]
    print("리스트:", li1)
    
    # power 함수를 사용하여 리스트의 각 요소를 제곱
    squared_li1 = list(map(power, li1))
    print("각 요소의 제곱:", squared_li1)

    # print_hello 함수 객체 출력
    print("print_hello 함수 객체:", print_hello)
    
    # print_hello와 동일한 람다 함수
    ph = lambda: print("HELLO")
    print("람다 함수 객체:", ph)
    
    # print_hello 함수를 10번 호출
    call_10_times(print_hello)

if __name__ == "__main__":
    # 직접 실행할 때 main 함수 호출
    main()
