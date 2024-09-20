def print_n_times(n: int, value1: str = "HELLO", value2: str = "✨PYTHON✨") -> str:
    result = []
    for _ in range(n):
        result.append(f"{value1} {value2}")
    return "\n".join(result)  # 결과를 문자열로 반환

def print_custom_message(n: int, value1: str, value2: str) -> str:
    result = []
    for _ in range(n):
        result.append(f"{value1}{value2}")
    return "\n".join(result)  # 결과를 문자열로 반환

def main():
    output1: str = print_n_times(n=3)  # 디폴트 매개변수 사용, 키워드 매개변수로 호출
    print(output1)  # 결과 출력

    output2: str = print_custom_message(n=3, value1="HELLLO , 🐍P🐍Y🐍T🐍H🐍O🐍N🐍", value2="  ✨PYTHON✨")  # 키워드 아규먼트로 호출
    print(output2)  # 결과 출력

if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    # Call main function when executed directly  
    main()
