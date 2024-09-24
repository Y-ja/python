import numpy as np
import pandas as pd

def main():
    sr = pd.Series([1, 2, 3, 4, 5], name="num", dtype=np.int8, index=list("abcde"))
    print(sr)
    print(sr.iloc[0])  # 위치 기반 접근에 iloc 사용
    x_1 = np.arange(1,20)
    sr2 = pd.Series(x_1 , name = "x_1")
    print(sr2)
    
if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    main()
