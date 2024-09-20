def print_n_times(n : int, *value):
    for _ in range(n):
        for ele in value:
            print(ele , end="")
        print()    

def main():
    print_n_times(3,"HELLLO , 🐍P🐍Y🐍T🐍H🐍O🐍N🐍" , "  ✨PYTHON✨")

if __name__ == "__main__":  
    # 직접 실행 시_main 함수 호출
    # Call main function when executed directly  
    main() 
