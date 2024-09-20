def main():
    num = [10, 20, 30, 40, 50, 60, 70, 80]
    print(min(num))  # 리스트의 최소값 출력
    print(max(num))  # 리스트의 최대값 출력
    print(sum(num))  # 리스트의 합계 출력

    # 리스트를 뒤집는 리스트 컴프리헨션
    reversed_num = [num[i] for i in range(len(num) - 1, -1, -1)]
    print(reversed_num)  # 뒤집힌 리스트 출력

    num.reverse()  # 리스트를 제자리에서 뒤집기
    print(num)  # 뒤집힌 리스트 출력
    
    #list_comprehension
    fruits = ["apple", "banana", "cherry", "chocolate", "kiwi", "mango"]
    # "chocolate"가 포함되지 않은 과일 이름 리스트 만들기
    filtered_fruits = [fruit for fruit in fruits if fruit != "chocolate"]
    print(filtered_fruits)  # 필터링된 과일 리스트 출력
    
   # 삼항 연산자 사용
    output = "True" if True else "False"
    print(output)  # 결과 출력

    
    
if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    # Call main function when executed directly
    main()
