import numpy as np

def main():
    x = np.arange(1,10).reshape(3,3)
    print(x)
    y = np.full((3,3),10)
    z = np.array([10,20,30]).reshape(-1,1)
    print(y)
    print(x+y)
    # broadcasting
    print(x + 10)
    print(x + z)

if __name__ == "__main__":  
    # 직접 실행 시_main 함수 호출
    # Call main function when executed directly  
    main() 
