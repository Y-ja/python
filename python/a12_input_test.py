def main():
    str_input = input("숫자를 넣으시오 100를 더해서 출력ㅋ-> \n")
    # print(str_input)
    # print(type(str_input))
    # print(int(str_input) + 100)
    
    if str_input.isdigit():
        print(int(str_input) + 100)
    else:
        print("숫자가 아니무리다!")    

if __name__ == "__main__":  
    # 직접 실행 시_main 함수 호출
    main() 
