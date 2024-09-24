import numpy as np
import pandas as pd

def main():
    # 4x6 배열 생성
    x_1 = np.arange(1, 25).reshape(4, 6)
    df_1 = pd.DataFrame(x_1)
    print("DataFrame df_1:")
    print(df_1)
    
    # 첫 번째 열 출력
    print("\n첫 번째 열:")
    print(df_1[0])
    
    # 첫 번째 행 두 번째 요소 출력
    print("\n첫 번째 행의 두 번째 요소:")
    print(df_1.iloc[0, 1])
    
    # CSV 파일 읽기
    df_data = pd.read_csv("/home/test/Desktop/python/python/artifical_intelligence/data/test.csv")
    
    # CSV 데이터 출력
    print("\nCSV 데이터:")
    print(df_data)

if __name__ == "__main__":  
    main()
