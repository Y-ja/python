class Myerror(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.args = ['⚠️ 이것은 내가 만든 에러 입니다! ⚠️']

def check_negative_num(num):
    if num < 0:
        raise Myerror()  # Myerror를 인스턴스화하여 발생시킴

def main():
    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try: 
        num = int(input("정수 입력 -> "))
        check_negative_num(num)
        print(lis[num]) 
    except Myerror as e:  # Myerror 예외를 처리
        print(type(e), e)
    except ValueError as e:
        print(type(e), e)
    except IndexError as e: 
        print(type(e), e) 
    except MemoryError as e:
        print(type(e), e)       
    finally:
        print("Program terminated.")
        
if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    # Call main function when executed directly  
    main()
