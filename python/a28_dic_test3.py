# 딕셔너리 선언 및 초기화
# - name: 기사
# - level: 12
# - sword: 불꽃의 검 
# - item: 
#     - armor: 불꽃레이트
#     - skills: ["베기", "세게 베기", "아주 세게 베기"]

def main():
    character = {
        "name": "기사",
        "level": 12,
        "sword": "불꽃의 검",
        "item": {  
            "armor": "불꽃레이트",
            "skills": ["베기", "세게 베기", "아주 세게 베기"]
        }
    }
    
    # 딕셔너리 출력
    for key, value in character.items():
        if key == "item":
            for sub_key, sub_value in value.items():
                if isinstance(sub_value, list):
                    output = f"{sub_key} -> {', '.join(sub_value)}"
                else:
                    output = f"{sub_key} -> {sub_value}"
                print(output)
        else:
            if not isinstance(value, dict):  # item이 아닌 경우
                print(f"{key} -> {value}")
    
    # 이름 수정
    character["name"] = "전사"
    print(f"name -> {character['name']}")
    
    # 절취선 출력
    print("-" * 30)
    
    # name 항목을 pop으로 제거
    removed_name = character.pop("name", None)
    if removed_name:
        print(f"Removed name: {removed_name}")
    
    # 남은 딕셔너리 출력
    print(character)

if __name__ == "__main__":
    main()
