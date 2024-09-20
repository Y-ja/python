# 딕셔너리 선언 및 초기화
# - name: 제품 이름
# - type: 제품 타입
# - ingredient: 재료 목록
# - origin: 원산지
# - price: 가격
# - quantity: 수량

def main():
    dictionary = {
        "name": "jerry",
        "type": "sugar",
        "ingredient": ["mango", "sugar"],
        "origin": "hawaii",
        "price": 5.99,
        "quantity": 10
    }
    
    # 딕셔너리의 각 항목 출력
    for key, value in dictionary.items():
        if key == "ingredient":
            print(f"{key} -> {', '.join(value)}")  # 재료 출력
        else:
            print(f"{key} -> {value}")  # 다른 항목 출력
    
    # 이름 수정
    dictionary["name"] = "apple_mango"
    
    # 절취선 출력
    print("-" * 30)  
    
    # 키 입력 및 값 출력
    key = input("키를 입력해주세욥 -> ")
    print(f"value -> {dictionary.get(key, '키가 없음ㅋ')}")  # get 메서드 사용
    
    # name 항목을 pop으로 제거
    removed_name = dictionary.pop("name", None)
    if removed_name:
        print(f"Removed name: {removed_name}")
    
    print(dictionary)  # 남은 딕셔너리 출력

if __name__ == "__main__":
    main()
