class Parent:
    def __init__(self) -> None:
        self.value = "Parent_TEST"
        print("Parent_class의 __init__() 메소드 호출!")

    def test(self, test_string: str = ""):  # 기본 매개변수 추가
        print("Parent_Class의 test() 메소드 입니다", test_string)

class Child(Parent):
    def __init__(self) -> None:
        super().__init__()  # Parent의 __init__ 호출
        print("Child_Class 의 __init__() 메소드 호출됨!") 
                   
    def test(self, *args, **kwargs):
        super().test(*args, **kwargs)  # 괄호 수정
        print("Child_Class의 test() 메소드 입니다")
        
def main():
    child = Child() 
    child.test("Hello from Child!")  # 테스트 문자열 전달
    print(child.value)

if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    # Call main function when executed directly  
    main()
