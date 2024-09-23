import os
import sys

def main():
    print(os.path)
    print(__file__)
    print(os.getcwd())
    os.chdir("/home/test/Desktop/python/python/python/data")
    
    if os.path.exists("basic.txt"):
        print("파일이 이미 있습니다")
    else:
      with open('basic.txt' , 'w' , encoding='utf-8') as file:      
        file = open("basic.txt" , "w")
        file.write("This is File Save Data! fiest \n")
        file.write("This is File Save Data! second \n")
        file.close()
    
if __name__ == "__main__":  
    # 직접 실행 시_main 함수 호출
    # Call main function when executed directly  
    main() 
