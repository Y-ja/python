import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

def main():
    # 데이터 로드
    df_1 = pd.read_csv("/home/test/Desktop/python/python/artifical_intelligence/data/iris.tab", delimiter="\t")
    print(df_1.head())
    print(df_1.info())
    
    # 모델 설정
    model = LogisticRegression(penalty='l2', C=1e42, solver='liblinear')
    
    # 목표 변수 및 특성 설정
    target = 'iris'  # 실제 목표 변수 열 이름 확인 필요
    feature = df_1.columns.drop(target)

    # 모델 학습
    model.fit(df_1[feature], df_1[target])

    # 결과 출력
    print("Classes:", model.classes_)
    print("Coefficients:", model.coef_)

    # 예측
    df_2 = pd.read_csv("/home/test/Desktop/python/python/artifical_intelligence/data/iris.tab", delimiter="\t")
    fitted = model.predict(df_2[feature])
    print("Predictions:", fitted)

    # 혼동 행렬 생성
    cm = confusion_matrix(df_2[target], fitted)
    print("Confusion Matrix:")
    print(cm)

if __name__ == "__main__":
    main()
