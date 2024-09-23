from functools import lru_cache

# 팩토리얼 호출 횟수 카운터
factorial_counter = 0

def factorial(n):
    global factorial_counter
    factorial_counter += 1  # 호출 시마다 카운터 증가
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

@lru_cache(maxsize=None)  # 무제한 캐시 크기
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    # 팩토리얼 출력
    print(f"1! -> {factorial(1)}") 
    print(f"2! -> {factorial(2)}") 
    print(f"3! -> {factorial(3)}") 
    print(f"4! -> {factorial(4)}") 
    print(f"5! -> {factorial(5)}") 

    # 팩토리얼 호출 횟수 출력
    print(f"팩토리얼 호출 횟수: {factorial_counter}")

if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    main()
