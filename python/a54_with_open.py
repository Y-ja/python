import os

def main():
    print("os.path:", os.path)
    print("현재 파일 경로:", __file__)
    print("현재 작업 디렉토리:", os.getcwd())
    
    # 디렉토리 변경
    os.chdir("/home/test/Desktop/python/python/python/data")

    # 파일 이름
    filename = "basic.txt"

    # 파일이 존재할 때까지 반복
    while True:
        if os.path.exists(filename):
            print("파일이 이미 존재합니다.")
            # 파일 읽기
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                print("파일 내용:\n", content)
            break  # 파일을 읽었으면 반복 종료
        else:
            # 파일 쓰기
            with open(filename, 'w', encoding='utf-8') as file:
                file.write("This is File Save Data! 1 \n")
                file.write("This is File Save Data! 2 \n")
            print("파일이 성공적으로 작성되었습니다.")
            break  # 파일을 썼으면 반복 종료

    # 내용 추가하기
    with open(filename, 'a', encoding='utf-8') as file:
        file.write("This is File Save Data! 1 \n")
        file.write("This is File Save Data! 2 \n")
    print("파일에 내용이 추가되었습니다.")

    # 파일 다시 읽어 출력
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("추가된 파일 내용:\n", content)

if __name__ == "__main__":
    # 직접 실행 시 main 함수 호출
    main()
