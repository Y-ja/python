def main():
   str1 =  "this is Python class^^!"
   print(str1.upper())
   print(str1.lower())
   print(str1)
   
   str1 = "   this is Python class^^!   "
   print(str1.strip() , "end")
   print(str1.lstrip() , "end")
   print(str1.rstrip() , "end")
   
if __name__ == "__main__":  
    # 직접 실행 시_main 함수 호출
    main() 
