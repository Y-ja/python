import pandas as pd
from sklearn.linear_model import LinearRegression

def main():
    # housing.tab 파일 읽기, 탭으로 구분된 데이터
    df_1 = pd.read_csv("/home/test/Desktop/python/python/artifical_intelligence/data/housing.tab", delimiter="\t")
    print(df_1.head())  # 첫 몇 줄 출력
    print(df_1.info())
    
    model = LinearRegression()
    target = 'MEDV'
    feature = ['CRIM', 'RM', 'AGE', 'TAX', 'NOX']  # 추가 특성 포함

    # 모델 학습을 위한 데이터 준비
    X = df_1[feature]
    y = df_1[target]

    # 모델 학습
    model.fit(X, y)

    # 예측 (예시로 첫 5개 데이터 예측)
    predictions = model.predict(X.head())
    print("Predictions:", predictions)

    # 모델의 절편 출력
    print("Intercept:", model.intercept_)

if __name__ == "__main__":
    # 직접 실행 시 main 함수 호출
    # Call main function when executed directly   
    main()
