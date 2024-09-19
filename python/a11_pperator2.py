import math

def main():
    pi = 3.141592 
    print(pi)
    print(math.pi)

    r = 10
    print(f"원주율 -> {pi}\n반지름 -> {r}\n"
          f"원의 둘레 -> {2 * pi * r}\n"
          f"원의 넓이 -> {pi * r**2}")

    #복합 대입 연산자
    i = 0
    i += 1
    str1 = "이것은"
    str1 += "파이썬 입니다!"
    print(str1)
    

if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    main()
