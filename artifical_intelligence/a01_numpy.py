import numpy as np

def main():
    li1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
    test_array = np.array(li1, dtype=np.int8)  # li1을 test_array로 변환
    print(test_array.dtype)  # 데이터 타입 출력
    print(test_array.shape)   # 배열의 형태 출력
    print(test_array.ndim)    # 배열의 차원 출력
    print(test_array.size)     # 배열의 전체 요소 개수 출력
    
    for ele in test_array:  # 각 요소 출력
        print(ele)

if __name__ == "__main__":  
    # 직접 실행 시_main 함수 호출
    # Call main function when executed directly 
    main()
