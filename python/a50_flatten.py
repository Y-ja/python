def flatten(data):
    output = []  # output을 함수 내부로 이동
    if not data:  # 데이터가 비어 있는지 확인
        return output  # 비어 있으면 빈 리스트 반환

    for ele in data:
        if isinstance(ele, list):  # 요소가 리스트인지 확인
            output.extend(flatten(ele))  # 재귀 호출 후 결과를 추가
        else:
            output.append(ele)  # 리스트가 아니면 output에 추가
    return output

def main():
    example = [1, 2, 3, [4, 5, 6], [7, [8, 9]]]
    print(flatten(example))

    empty_example = []  # 빈 리스트 예시
    print(flatten(empty_example))  # 빈 리스트의 경우

if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    # Call main function when executed directly  
    main()
