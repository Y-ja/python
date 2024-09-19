# 사용자가 여러 숫자를 쉼표로 구분하여 입력을 받습니다.. input
# ex) 10,20,30,abc
# 합계 평균 최대/최소값 을 계산 문자가 있을시 무시하고 출력
#문자만 있을시 유효한 숫자가 없습니다 즉 에러 처리 
#format을 써서 자릿수를 유효숫자 소수점3번째까지 출력
def main():
    user_input = input("숫자를 구분하여 입력 -> ")
    numbers = user_input.split(",")
    
    valid_numbers = []
    invalid_numbers = []  # 무시된 숫자를 저장할 리스트
    
    for num in numbers:
        try:
            valid_numbers.append(float(num))
        except ValueError:
            invalid_numbers.append(num)  # 무시된 값 추가
            
    if not valid_numbers:
        print("유효한 숫자가 없습니다.")
        return
    
    # 합계, 평균, 최대값, 최소값을 계산합니다.
    total = sum(valid_numbers)
    avg = total / len(valid_numbers)
    maximum = max(valid_numbers)
    minimum = min(valid_numbers)
    
    # 결과를 소수점 3자리까지 출력합니다.
    print("합계: {:.3f}".format(total))
    print("평균: {:.3f}".format(avg))
    print("최대값: {:.3f}".format(maximum))
    print("최소값: {:.3f}".format(minimum))
    
    # 무시된 값을 출력합니다.
    if invalid_numbers:
        print("무시된 값:", ", ".join(invalid_numbers))

if __name__ == "__main__":  
    main()
