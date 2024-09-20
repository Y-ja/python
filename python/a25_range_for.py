def main():
    # 0부터 9까지 반복
    for i in range(10):
        print(f"{i}번째 반복!")
        
    lis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # 리스트의 요소 반복
    for i in lis:
        print(f"{i}번째 반복!") 
    
    # 1부터 9까지 홀수 반복
    for i in range(1, 10, 2):
        print(f"{i}번째 반복!")
             
    #문자열 출력
    lis2 = ['banana' , 'apple' , 'grape' , 'mango' , 'peach']
    for ele in lis2 :
        print(ele)
    
             
if __name__ == "__main__":  
    main()
