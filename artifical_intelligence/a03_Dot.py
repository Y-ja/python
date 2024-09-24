import numpy as np

def main():
    x_1 = np.arange(1,7).reshape(2,3)
    x_2 = np.arange(1,7).reshape(3,2)
    x_3 = x_1.dot(x_2)
    
    print(x_3)

if __name__ == "__main__":  
    # 직접 실행 시_main 함수 호출
    # Call main function when executed directly  
    main() 
