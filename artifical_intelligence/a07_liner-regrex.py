import pandas as pd
from sklearn.linear_model import LinearRegression

def main():
    # housing.tab 파일 읽기, 탭으로 구분된 데이터
    df_1 = pd.read_csv("/home/test/Desktop/python/python/artifical_intelligence/data/housing.tab", delimiter="\t")
    print(df_1.head())  # 첫 몇 줄 출력
    print(df_1.info())
if __name__ == "__main__":  
    main()
