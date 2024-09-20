def main():
    li = [123,456,7.7,'next_8']
    # li = li()
    print(type(li))
    print(li)
    print(li[0])
    print(li[1])
    print(li[2:4])
    li[1] = "구구구구구"
    print(li)
    
    # 리스트 연산자
    list_a = [1,2,3]
    list_b = [4,5,6]
    
    print(list_a + list_b)
    list_a.extend(list_b)
    print(list_a * 3)
    print(len(list_a))

if __name__ == "__main__":  
    # 직접 실행 시_main 함수 호출
    main() 
