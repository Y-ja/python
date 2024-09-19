import datetime
import time

def main():
    now = datetime.datetime.now()
    
    print(f"현재 날짜와 시간: {{\n"
          f"    연도: {now.year},\n"
          f"    월: {now.month},\n"
          f"    일: {now.day},\n"
          f"    시간: {now.hour},\n"
          f"    분: {now.minute},\n"
          f"    초: {now.second}\n"
          f"}}")
    
    print(time.time())

if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    main()
