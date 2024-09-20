def main():
    list_a = [1, 2, 3]
    print(list_a)
    
    # 리스트에 숫자를 추가
    list_a.append(4)
    list_a.append(5)
    print(list_a)
    
    # 리스트의 특정 위치에 요소 삽입
    list_a.insert(0, 0)
    list_a.insert(3, 2.5)
    print(list_a)
    
    # 첫 번째 요소 삭제
    del list_a[0]
    print(list_a)
    
    a = "a variable"
    list_a.insert(0, a)
    del list_a[0]
    print(list_a)
    print(a)  # 변수 a에 여전히 접근 가능
    
    del a  # 변수 a 삭제

    # pop
    list_a.append("last element")
    re = list_a.pop()  # 마지막 요소를 제거하고 반환
    print(list_a, re)
    
    # remove by value
    if re in list_a:
        list_a.remove(re)  # 방금 제거한 요소를 리스트에서 제거 (없을 경우 무시)
    print(list_a)
    
if __name__ == "__main__":  
    main()
