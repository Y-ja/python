def main():
    A = True
    B = False
    
    if A:
        print("A is True")
    elif B:  # B가 True일 경우
        print("A is False and B is True")
    else:
        print("A is False and B is False")  # A와 B가 모두 False일 때 출력

if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    main()
