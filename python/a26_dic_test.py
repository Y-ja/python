def main():
    # 선언 (Declaration)
    dict_a = {}
    set_a = set()
    set_b = {1, 2, 3}
    
    print(type(dict_a))
    print(type(set_a))
    print(type(set_b))
    print(dict_a, set_a, set_b)
    
    # 요소 추가 (Adding elements)
    dict_a['b'] = 456
    dict_a['a'] = '123'
    
    print(dict_a)
    
    # 요소 접근 (Accessing elements)
    print(dict_a['a'], dict_a['b'])
    print(dict_a.get('c'))
    
if __name__ == "__main__":
    # 직접 실행 시 main 함수 호출 
    #Call main function when executed directly 
    main() 
    