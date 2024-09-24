import numpy as np

def main():
    x_1 = np.random.randint(1,100,10)
    x_2 = np.random.randint(1,100,10)
    print(x_1)
    print(x_2)
    print(x_1 > x_2)
    
    print(x_1[x_1 > x_2])

if __name__ == "__main__":  
    # 직접 실행 시_main 함수 호출
    # Call main function when executed directly  
    main() 
